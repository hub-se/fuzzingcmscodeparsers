# Generate a report of classified errors in markdown format. 

from data_model import FuzzingRun, LogSet, ErrorCollection

CLASSIFIER_RATING = {'Critical' : 0, 
                     'Downstream' : 4, 
                     'Logical' : 1, 
                     'Semantic' : 2, 
                     'Syntactic' : 3, 
                     'Warning' : 5}

def add_to_string(string_, target_):
    target_ += string_
    target_ += "\n"
    return target_

def error_sort(classifier):
    return CLASSIFIER_RATING[classifier]

def main():
    vasp_runs = []
    for run_id in range(30):
        run = FuzzingRun(run_id, code = "vasp")
        vasp_runs.extend(run.logs)
    vasp_set = LogSet(logs = vasp_runs)

    vasp_collection = ErrorCollection.load("./final_vasp_error_collection_classified.json", ".")

    exciting_runs = []
    for run_id in range(30):
        run = FuzzingRun(run_id, code = "exciting")
        exciting_runs.extend(run.logs)
    exciting_set = LogSet(logs = exciting_runs)

    exciting_collection = ErrorCollection.load("./final_exciting_error_collection_classified.json", ".")

    aims_runs = []
    for run_id in range(30):
        run = FuzzingRun(run_id, code = "aims")
        aims_runs.extend(run.logs)
    aims_set = LogSet(logs = aims_runs)

    aims_collection = ErrorCollection.load("./final_aims_error_collection_classified.json", ".")

    espresso_runs = []
    for run_id in range(30):
        run = FuzzingRun(run_id, code = "espresso")
        espresso_runs.extend(run.logs)
    espresso_set = LogSet(logs = espresso_runs)

    espresso_collection = ErrorCollection.load("./final_espresso_error_collection_classified.json", ".")

    output = ""
    for coll_, code, error_set in zip([vasp_collection, exciting_collection, aims_collection, espresso_collection], ["vasp", "exciting", "aims", "espresso"], [vasp_set, exciting_set, aims_set, espresso_set]):
        output = add_to_string(f'## Errors for code: {code}\n', output)
        output = add_to_string("| Key | Description |\n| :--- | :--- |", output)
        last_classifier = ""
        error_counter = 0
        for error_data in sorted(coll_.get_all(), key = lambda x: error_sort(x["classifier"])):
            if last_classifier != error_data['classifier']:
                error_counter = 0
                last_classifier = error_data['classifier']
            else:
                error_counter+=1
            output = add_to_string(f"|**ID**| {code}:{error_data['classifier'].lower()}:{error_counter}|", output)
            output = add_to_string(f"|**Error class**| {error_data['classifier']}|", output)
            output = add_to_string(f"|**Comment**| {error_data['comment']}|", output)
            example = error_set.get_logs_by_error(error_data["error"])[0].unique_id
            output = add_to_string(f'|**Example file**| {code}/run-{example.split(":")[1]}/{example.split(":")[2]}', output)
            output = add_to_string("|**Details**| |", output)
            for key, value in error_data["error"].items():
                output = add_to_string(f"|**{key}**|{value}|", output)
            output = add_to_string("| | |", output)
            output = add_to_string("|**----**|**----**|", output)
            output = add_to_string("| | |", output)
        output = add_to_string("", output)

if __name__ == "__main__":
    main()