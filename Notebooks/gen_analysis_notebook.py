from data_model import FuzzingRun, LogSet
import numpy as np
import sys, json
from os.path import exists

def gen_header(metadata: str) -> list:
    header = [
        ["markdown", "This is an automatically generated notebook."],
        ["markdown", f"# Below are the NOMAD {metadata['code']} parser errors that are found using grammar based fuzzing."],
        ["markdown", "The data is loaded to the dictionary `collection` and can be accessed by: `collection[<status>][<exception id>][<stderr id>]`.\nIn the `LogSet()` objects in the dictionary have additional functions for in-depth analysis."],
        ["code", "from gen_analysis_notebook import load_data_collection_to_object_dict\nfrom data_model import ErrorCollection"],
        ["code", f"collection = load_data_collection_to_object_dict('{metadata['data_filename']}')"],
        ["markdown", "Use the `error_collection` below to analyse and store errors found in the data. The errors are displayed as a dictionary of the parsed STDERR of the fuzzing run."],
        ["markdown", "Usage:\n```python\nerror_collection.add({'<keys>' : '<string>, [...]'}, '<comment>')\n```"],
        ["code", "error_collection = ErrorCollection()"]
    ]
    return header

def load_data_collection_to_object_dict(filename: str) -> dict:
    with open(filename, "r") as f:
        collection_dict = json.load(f)
    collection = {}
    for status_key, status_data in collection_dict.items():
        collection[status_key] = {}
        for exception_key, exception_data in status_data.items():
            collection[status_key][exception_key] = {}
            for stderr_key, stderr_data in exception_data.items():
                collection[status_key][exception_key][stderr_key] = LogSet.from_serialized_list(stderr_data)
    return collection

class NotebookGenerator():
    
    def __init__(self, notebook_filename : str, 
                       data_filename : str, 
                       header = None, 
                       data_path = ".") -> None:
        self.notebook_filename = notebook_filename
        self.data_filename = data_filename
        self.header = header
        self.data_path = data_path

    def generate(self, log_set: LogSet) -> None:
        collection, cell_data = self.auto_generate_content(log_set)
        self.save_data_collection(collection)
        notebooks_cell_data = self.cell_data_to_notebook_cells(cell_data)
        self.write_new_notebook(notebooks_cell_data)
        
    def cell_data_to_notebook_cells(self, cell_data : list) -> list:
        notebook_cells = []
        for cell in cell_data:
            cell_type = "markdown" if cell["type"] != "code" else "code"
            notebook_cells.append([cell_type, self.gen_cell_content(cell)])
        return notebook_cells

    def save_data_collection(self, collection: dict) -> None:
        with open(self.data_filename, "w") as f:
            json.dump(collection, f)
    
    def write_new_notebook(self, notebook_data: list) -> None:
        # from: https://nbviewer.jupyter.org/gist/fperez/9716279
        import nbformat as nbf

        def gen_cell(cell_type, cell_content):
            if cell_type == "markdown":
                new_cell = nbf.v4.new_markdown_cell(cell_content)
            elif cell_type == "code":
                new_cell = nbf.v4.new_code_cell(cell_content)
            else:
                raise KeyError(f"Unrecognized cell type: {cell_type}.")                
            return new_cell

        nb = nbf.v4.new_notebook()
        cells = [] 
        if self.header != None:
            for cell_type, cell_content in self.header:
                cells.append(gen_cell(cell_type, cell_content))
        for cell_type, cell_content in notebook_data:
            cells.append(gen_cell(cell_type, cell_content))
        nb['cells'] = cells
        nbf.write(nb, f'{self.notebook_filename}.ipynb')
    
    def auto_generate_content(self, log_set: LogSet) -> dict:
        set_collection = {}
        cells = []
        for status_key, status_data in self.auto_split_status(log_set).items(): # locate splitted sets in a dict for easy access
            set_collection[status_key] = {}
            cells.append({"type" : "h1", "data" : f"Status: {status_key}"}) # generate a generic heading
            cells.append({"type" : "comment", "data" : status_data["comment"]}) # generate content for comment cells
            for exception_key, exception_data in self.auto_split_exception(status_data["set"]).items():
                set_collection[status_key][exception_key] = {}
                cells.append({"type" : "h2", "data" : f"Status: {status_key} Exception: {exception_key}"})
                cells.append({"type" : "comment", "data" : exception_data["comment"]})
                for stderr_key, stderr_data in self.auto_split_stderr(exception_data["set"]).items():
                    cells.append({"type" : "h3", "data" : f"Status: {status_key} Exception: {exception_key} STDERR: {stderr_key}"})
                    cells.append({"type" : "comment", "data" : stderr_data["comment"]})
                    cells.append({"type" : "code", "data" : f"collection['{status_key}']['{exception_key}']['{stderr_key}'].find_unknown_errors(error_collection)"})
                    cells.append({"type" : "code", "data" : f"collection['{status_key}']['{exception_key}']['{stderr_key}'].find_unknown_errors(error_collection)"})
                    set_collection[status_key][exception_key][stderr_key] = stderr_data["set"].serialize()
        return set_collection, cells
    
    
    #static methods
    
    @staticmethod
    def auto_split_status(log_set: LogSet) -> dict:
        success, failed, crashed = log_set.split_by_status()
        return {
            "success" : {
                "comment" : f"Found {len(success)} successfull runs.",
                "set" : success
            },
            "failed" : {
                "comment" : f"Found {len(failed)} failed runs.",
                "set" : failed
            },
            "crashed" : {
               "comment" : f"Found {len(crashed)} crashed runs.",
                "set" : crashed
            }
        }

    @staticmethod
    def auto_split_exception(log_set: LogSet) -> dict:
        sets = log_set.split_by_exception_hashes()
        data = {}
        for idx, set_ in enumerate(sets):
            data[str(idx)] = {
                "comment" : f"Found set of {len(set_)} logs with hashes: {set_.unique_exception_hashes}",
                "set" : set_
            }
        return data

    @staticmethod
    def auto_split_stderr(log_set: LogSet) -> dict:
        sets = log_set.split_by_stderr()
        data = {}
        for idx, set_ in enumerate(sets):
            stderrs = []
            for data_ in set_[0].parse_stderr():
                try:
                    stderrs.append(data_["message"])
                except KeyError:
                    stderrs.append("Uncaught exception")
            data[str(idx)] = {
                "comment" : f"Found set of {len(set_)} with stderrs: {stderrs}",
                "set" : set_
            }
        return data
    
    @staticmethod
    def gen_cell_content(data : dict) -> str:
        content = ''
        if data["type"] == "comment" or data["type"] == "code":
            content = data["data"]
        elif data["type"].startswith("h"):
            n_sharps = int(data["type"].strip()[1:])
            content = f"{n_sharps * '#'} {data['data']}"
        else:
            raise KeyError("Invalid data for cell content generation.")
        return content

def main():

    def handle_overwrites():
        answer = input("Overwrite (y/[n])?")
        if answer.strip() != "y":
            sys.exit("Aborting.")
    
    # basic CLI
    if len(sys.argv) != 5 or sys.argv[1] == "help":
        sys.exit("Usage: \npython gen_analysis_notebook.py <code> <notebook_filename> <data_filename> <path_to_fuzzing_runs>")
    code = sys.argv[1]
    notebook_filename = sys.argv[2]
    data_filename = sys.argv[3]
    run_folder_path = sys.argv[4]

    # check file existence
    if exists(f"{notebook_filename}.ipynb"):
        print(f"Notebook file {notebook_filename} exists.")
        handle_overwrites()
    if exists(data_filename):
        print(f"Data file {data_filename} exists.")
        handle_overwrites()

    # do the work
    header = gen_header({"code" : code, "data_filename" : data_filename})
    runs = [FuzzingRun(idx, code = code, path_kwargs={"run_path":run_folder_path}, log_block_kwargs={"run_path":run_folder_path}) for idx in range(30)]
    full_set = LogSet(logs = np.concatenate([run.logs for run in runs]))
    generator = NotebookGenerator(notebook_filename, data_filename, header)
    generator.generate(full_set)

if __name__ == "__main__":
    main()