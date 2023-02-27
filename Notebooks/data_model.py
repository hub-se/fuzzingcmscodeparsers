import os, re
import numpy as np
import json
from datetime import timedelta
from typing import List, Iterable

exciting_subpath = 'res/exciting_full'
vasp_subpath = 'res/vasp_full'
espresso_subpath = 'res/espresso_full'
aims_subpath = 'res/aims_full'

def is_block_start(line):
    # every text block starts with "Write Command" 
    if "Write Command" in line:
        return True
    return False

def dicts_match(candidate: dict, reference: dict):
    """
    Checks if all keys and values of the reference are the same in the candidate.
    The candidate can have additional items.
    """
    try:
        if not all([key in candidate.keys() for key in reference.keys()]):
            return False
        else:
            for key, value in reference.items():
                if isinstance(value, list):
                    if not isinstance(candidate[key], list):
                        raise TypeError(f"Types not matching: reference: {type(value)}, candidate: {candidate[key]}")
                    for item in value:
                        if not item in candidate[key]:
                            return False
                elif candidate[key] != value:
                    return False
    except (KeyError, AttributeError):
        return False
    return True

def get_file_content_path(log_block, suffix: str, run_path = "./run") -> str:
    """
    Function to get the path to the floatified input files. Uses the constant `run_path`.
    """
    return os.path.join(run_path, 
                        f"run-{log_block.run_id}", 
                        "floatified", 
                        log_block.code, 
                        "output", 
                        log_block.file_name + suffix)

class LogBlock():
    """
    Object containing all contents of a single parser execution.

    Attributes:

    * `prog_call`: Shell command that invoked the parser
    * `stderr`: standard error of the parser call
    * `stdout`: standard output of the parser call
    * `timestamp`: runtime of the parser execution
    * `rndnrs`: random numbers to reproduce the fuzzing run
    * `run_id`: identifier of the fuzzing run
    * `code`: parser of this code was used
    * `floatified_input_path`: path to the input file that was parsed
    """
    
    def __init__(self, text_block, run_id = None, code = None, run_path_generator = get_file_content_path, suffix = ".txt", run_path="./run"):
        if text_block == None: # Not a nice hack.
            return
        content = self._split_block_content(text_block)
        for name_, value_, ind_ in zip(["prog_call", "stderr", "stdout", "timestamp", "rndnrs"],
                                      content,
                                      [0, None, None, 0, 0]):
            self._set_value(name_, value_, ind_)
        self.run_id = run_id
        self.code = code
        self.floatified_input_path = run_path_generator(self, suffix, run_path=run_path)
    
    
    def _set_value(self, var, value: List[List[str]], index_ = None):
        """
        Set attributes. The `value` argument is a nested list of strings.
        Therefore, if only one string is expected, e.g. for the timestamp,
        the first entry of the list is used instead of the full data.
        """
        try:
            if index_ != None:
                self.__setattr__(var, value[index_])
            else:
                self.__setattr__(var, value)                
        except Exception as e:
            print(f"Unable to set {var}, set to None")
            self.__setattr__(var, None)

    def to_dict(self):
        data = {
            "prog_call" : self.prog_call,
            "stderr" : self.stderr,
            "stdout" : self.stdout,
            "timestamp" : self.timestamp,
            "rndnrs" : self.rndnrs,
            "run_id" : self.run_id,
            "code" : self.code,
            "floatified_input_path" : self.floatified_input_path,
        }
        return data

    @staticmethod 
    def from_dict(dict_):
        self = LogBlock(None)
        for attribute, value in dict_.items():
            self.__setattr__(attribute, value)
        return self

    def set_run_id(self, run_id):
        self.run_id = run_id
    
    def set_code(self, code):
        self.code = code
    
    def _split_block_content(self, text_block):
        # Assumes fixed block structure
        prog_call, stderr, stdout, timestamp, rndnrs = ([] for _ in range(5))
        line_buffer = []
        empty_list_counter = 0
        for idx, line in enumerate(text_block):
            if 'Write Command' in line:
                pass
            elif 'Write stderr' in line:
                prog_call = line_buffer
                line_buffer = []
            elif 'Write stdout' in line:
                stderr = line_buffer
                line_buffer = []
            elif 'Write timestamp' in line:
                stdout = line_buffer
                line_buffer = []
            elif 'Reproduce this' in line:
                timestamp = line_buffer
                line_buffer = []
            elif '-------------------------------------' in line:
                rndnrs = line_buffer
                break
            elif line.strip() == "[]," or line.strip() == "[]":
                empty_list_counter += 1
            else:
                if empty_list_counter > 0:
                    line_buffer.append(f'"{empty_list_counter} empty array elements"\n')
                    empty_list_counter = 0
                line_buffer.append(line)
        return prog_call, stderr, stdout, timestamp, rndnrs              
    
    def print_content(self):
        for part in [self.prog_call, self.stderr, self.timestamp]:
            for line in part:
                if "section_run" in line: # I do not want the parser output
                    break
                print(line, end = "")
    
    def parse_stderr(self):
        blocks = []
        in_block = False
        in_exception = False
        error_dict = {}
        exception_block = []
        for line in self.stderr:
            if re.search('\s+nomad.cli\s+', line) != None: # NOMAD CLI log start
                if in_block:
                    blocks.append(error_dict)
                    error_dict = {}
                in_block = True
                error_dict['message'] = ' '.join(line.strip().split()[3:])
                error_dict['error_type'] = line.strip().split()[0]
            else:
                if line.strip().startswith('- ') and not 'exception:' in line: # NOMAD CLI error handling, WARNING: Not a safe condiction.
                    if in_exception:
                        in_exception = False
                        error_dict['traceback'] = ''.join(exception_block)
                        exception_block = []
                    line_data = line.strip().strip('-').split(':',1)
                    error_dict[line_data[0].strip()] = line_data[1].strip()
                else: # Python exception
                    in_exception = True
                    exception_block.append(line)
        # add last entry
        if error_dict != {}:
            blocks.append(error_dict)
        # add uncaught exceptions
        if len(exception_block) != 0:
            blocks.append({"additional_exceptions" : exception_block})
        return blocks
    
    def get_file_content(self):
        if self.run_id == None or self.code == None:
            raise AttributeError("Run id and code must be set before catching the file content.")
        with open(self.floatified_input_path, "r") as f:
            data = f.readlines()
        return data

    def print_file_content(self, start_index = 0, stop_index = None):
        content = self.get_file_content()
        for line in content[start_index:stop_index]:
            print(line, end = "")
        return
            
    def get_last_tb_lines(self, n = 1): # TEST
        tb_lines = []
        for error_line in self.error_lines:
            for idx, line in enumerate(self.stderr):
                if line == error_line:
                    assert idx > 0, 'Unexpected behaviour: No traceback found.'
                    tb_lines.append(self.stderr[idx-n:idx]) #WARNING: assuming the error is not the first line in the content
        return tb_lines
    
    def get_error_passing_to_nomad(self, traceback_index = 0, n_tb = 20, n = 1):
        for idx, line in enumerate(self.stderr):
            if "nomad/metainfo" in line:
                return self.stderr[idx-n:idx]
    
    def get_stderr_lines_by_substring(self, string):
        return [line for line in self.stderr if string in line]
    
    def get_file_content_lines_by_substring(self, string, line_numbers = True):
        return [(line_number, line) if line_numbers else line for line_number, line in enumerate(self.get_file_content()) if string in line]
    
    def get_file_content_lines_by_regex(self, regex, line_numbers = True):
        file_content = self.get_file_content()
        matched_lines = []
        for line_nr, line in enumerate(file_content):
            if re.match(regex, line) != None:
                if line_numbers:
                    matched_lines.append((line_nr, line))
                else:
                    matched_lines.append(line)
        return matched_lines

    @property
    def runtime(self):
        hours, minutes, seconds = [float(x) for x in self.timestamp.strip().split(":")]
        return timedelta(hours = hours, minutes=minutes, seconds = seconds).total_seconds()
    
    
    @property
    def exception_hashes(self):
        hashes = []
        for line in self.stderr:
            if 'exception_hash' in line:
                hashes.append(line.split(':')[-1].strip()) # lazy parsing here
        return hashes
        
    @property
    def unique_id(self):
        return ":".join([str(self.code), str(self.run_id), self.file_name])
    
    @property
    def parser_output(self):
        try:
            output = json.loads(''.join(self.stdout) + '}')
        except json.JSONDecodeError as exep:
            output = None
        return output
    
    @property
    def file_name(self):
        return re.search('file\d*', self.prog_call).group()
    
    @property
    def successful(self): #TEST
        if self.crashed: # It can not be successful if it crashed.
            return False
        if self.parser_output == None: # There needs to be output.
            return False
        if len(self.stderr) != 0: # The stderr needs to be empty, or contains only warnings.
            for entry in self.parse_stderr():
                try:
                    if entry["error_type"].strip() == "ERROR":
                        return False
                except:
                    return False
        return True
    
    @property
    def crashed(self): # TEST
        # crashed means here that no output was produced
        return self.parser_output == None
    
    @property
    def error_lines(self): # TEST
        # returns all log lines that contain the word 'Error'
        error_lines = []
        for line in self.stderr:
            if re.search('Error', line) != None:
                if not line.startswith("WARNING"):
                    error_lines.append(line)
        return error_lines
    
    @property
    def warnings(self):
        # returns all log lines that contain the word 'WARNING'
        warnings = []
        for line in self.stderr:
            if re.search('WARNING', line) != None:
                warnings.append(line)
        return warnings
    
    @property
    def n_errors(self): # TEST
        n_errors = 0
        for error in self.parse_stderr():
            try:
                if not error["error_type"] == "WARNING":
                    n_errors += 1
            except KeyError:
                n_errors += 1
        return n_errors
    
    def __repr__(self):
        return f"LogBlock(id = {self.unique_id})"
    
from functools import partial

subpath_dict = {
    "exciting" : exciting_subpath,
    "aims" : aims_subpath,
    "espresso" : espresso_subpath,
    "vasp" : vasp_subpath
}

def get_full_result_path(run_number, run_path ='./run', code = "exciting"):
    return os.path.join(run_path, f'run-{run_number}', subpath_dict[code])

class FuzzingRun(): # --> Should this maybe become a function? It is called only once and acts as a parser of the execution traces.
    
    def __init__(self, 
                 run_id, 
                 code = "exciting", 
                 path_generator = get_full_result_path, 
                 path_kwargs = {'run_path' : './run'},
                 block_identifier = is_block_start, 
                 log_block_kwargs = {}):
        self.run_id = run_id
        self.code = code
        self.path_generator = partial(path_generator, code = code, **path_kwargs)
        self.block_identifier = block_identifier
        self.logs = [LogBlock(block, run_id=self.run_id, code = self.code, **log_block_kwargs) for block in self._read_text_blocks()]
        self._iter_index = 0
            
    @property
    def successful_runs(self):
        return [log for log in self.logs if log.successful]    
    
    @property
    def crashed_runs(self):
        return [log for log in self.logs if log.crashed]
    
    def get_unique_error_lines(self):
        unique_error_lines = []
        for log in self:
            for line in log.error_lines:
                if not line in unique_error_lines:
                    unique_error_lines.append(line)
        return unique_error_lines
        
    def __len__(self):
        return len(self.logs)
            
    def __iter__(self):
        self._iter_index = 0
        return self

    def __next__(self):
        if self._iter_index + 1 > len(self):
            self._iter_index = 0
            raise StopIteration
        else:
            self._iter_index += 1
            return self[self._iter_index-1]

    def __getitem__(self, index):
        return self.logs[index]
        
    def _read_text_blocks(self):
        # read full fuzzing logs and outputs individual executions of the nomad parser
        text_blocks = []
        with open(self.path_generator(self.run_id), 'r') as log_file:
            content = log_file.readlines() # this may fail for large files because of memory
            new_block = [] # every text block enters is a list of one-line strings
            for line in content:
                if self.block_identifier(line):
                    if len(new_block) > 0: # filter any empty list artifacts
                        text_blocks.append(new_block)
                    new_block = [] # start new text block after saving the old one
                new_block.append(line) # the regular case: just add another line to the current text block
            text_blocks.append(new_block) # the last block needs to be added manually
        return text_blocks
    
    
class LogSet():
    """
    Collection of LogBlock() objects for semi-automatic analysis of fuzzing results.
    Initialize with iterable of LogBlock() elements.
    Usage:
        * Split set by status
        * for each:
            * split by exception hash
            * for each:
                * split by stderr
                * analyse log entries
    """
    
    def __init__(self, logs = []):
        self._logs = list(logs)
        self._iter_index = 0
        self._codes = np.unique([log.code for log in self])
    
    # properties
    @property
    def logs(self):
        return self._logs
    
    @property
    def successful_runs(self):
        return LogSet(logs = [log for log in self._logs if log.successful])    
    
    @property
    def crashed_runs(self):
        return LogSet(logs = [log for log in self._logs if log.crashed])
    
    @property
    def unique_exception_hashes(self):
        return np.unique(np.concatenate([log.exception_hashes for log in self]))
    
    @property
    def unique_error_lines(self):
        return np.unique(np.concatenate([log.error_lines for log in self]))
    
    @property
    def is_unique(self):
        if len(np.unique([log.unique_id for log in self])) == len(self):
            return True
        return False
    
    # functions    
    def get_logs_by_exception_hash(self, exception_hash):
        return LogSet(logs = filter(lambda x: exception_hash in x.exception_hashes, self._logs))
    
    def split_by_exception_hashes(self) -> List[object]:
        """
        Split self into list of LogSet()s. Each of the generated LogSet()s will have 
        LogBlock()s with the same unique combination of exception hashes.
        """
        split_list = []
        for log in self:
            is_added = False
            for idx, set_ in enumerate(split_list):
                if ':'.join(sorted(log.exception_hashes)) == ':'.join(sorted(set_.unique_exception_hashes)):
                    split_list[idx] += log
                    is_added = True
                    break
            if not is_added:
                split_list.append(LogSet(logs = [log]))
        assert sum([len(list_) for list_ in split_list]) == len(self), f"Unconsistent length of LogSets."
        return split_list

    def split_by_stderr(self):
        """
        Split self into list of LogSet()s. Each of the generated LogSet()s will have
        LogBlock()s with the same unique combination of STDERR messages. 
        """
        split_dict = {}
        for log in self:
            is_added = False
            stderr_data = log.parse_stderr()
            messages = []
            error_types = []
            for entry in stderr_data:
                try:
                    messages.append(entry['message'])
                    error_types.append(entry['error_type'])
                except KeyError:
                    messages.append("Uncaught exception")
                    error_types.append('Uncaught exception')
            hash_ = str(sorted(zip(messages, error_types))) #that is not a hash, but used like one
            for key, set_ in split_dict.items():
                if hash_ == key:
                    split_dict[key] += log
                    is_added = True
                    break
            if not is_added:
                split_dict[hash_] = LogSet(logs = [log])
        assert sum([len(list_) for list_ in split_dict.values()]) == len(self), f"Unconsistent length of LogSets."
        return list(split_dict.values())

    def split_by_status(self):
        """
        Split self by LogBlock()s that log _successful_, _failed_, or _crashed_ runs.
        """
        intermediate_runs = LogSet(logs = [log for log in self if not log.successful and not log.crashed])
        return [self.successful_runs, intermediate_runs, self.crashed_runs]

    def serialize(self) -> List[dict]:
        """
        Return list of LogBlocks() represented as `dict`s.
        """
        return [log.to_dict() for log in self.logs]

    def find_unknown_errors(self, error_descriptions: Iterable):
        """
        Given an iterable, parse the STDERR of all logs in `self` and compare if they 
        are contained in the iterable. The comparison uses the function `dicts_match`
        defined above, which consideres that the candidates in `self` can have more 
        information than what is given in the iterable.
        """
        unknown_errors = {}
        for log in self:
            stderr_ = log.parse_stderr()
            for description in stderr_:
                if any([dicts_match(description, ref) for ref in error_descriptions]):
                    continue
                if not log.unique_id in unknown_errors.keys():
                    unknown_errors[log.unique_id] = []
                unknown_errors[log.unique_id].append(description)
        return unknown_errors

    def get_logs_by_error(self, error: dict) -> object:
        """
        Get all LogBlocks that contain a specific error, i.e. all logs that match all
        keys and values defined in `error`.
        """
        logs_with_error = LogSet()
        for log in self:
            if any([dicts_match(description, error) for description in log.parse_stderr()]):
                logs_with_error += log
        return logs_with_error

    def get_log_by_id(self, id_):
        """
        Get a log with a specific log id.
        """
        return [log for log in self if log.unique_id == id_][0]

    @staticmethod
    def from_serialized_list(list_: List[dict]) -> object:
        logs = [LogBlock.from_dict(dict_) for dict_ in list_]
        self = LogSet(logs = logs)
        return self 
    
    # arithmetic function
    
    def __add__(self, other):
        if isinstance(other, LogSet):
            return LogSet(logs = np.append(self.logs, other.logs))
        elif isinstance(other, LogBlock):
            return LogSet(logs = np.append(self.logs, [other]))
        else:
            raise TypeError('Addition is not defined for other instances than LogBlock() or LogSet()')
            
    # iterator functions
    def __iter__(self):
        self._iter_index = 0
        return self

    def __next__(self):
        if self._iter_index + 1 > len(self):
            self._iter_index = 0
            raise StopIteration
        else:
            self._iter_index += 1
            return self._logs[self._iter_index-1]

    def __getitem__(self, key):
        if isinstance(key, int):
            return self._logs[key]
        elif isinstance(key, str):
            matches = [log for log in self.logs if log.unique_id == key]
            if len(matches) == 1:
                return matches[0]  
            else:
                raise KeyError('Unable to process: Too many matches for key.')
        else:
            raise KeyError(f'Unable to interpret as index: {key} of type {type(key)}.')
    
    def __len__(self):
        return len(self._logs)
    
    # misc properties
    def __repr__(self):
        return f"LogSet() for codes {self._codes} with {len(self)} entries"

class ErrorCollection:
    """
    Collection of errors (described by dicts), (manually added) comments and 
    classifiers.
    """

    def __init__(self):
        self._errors = []
        self._comments = []
        self._iter_index = []
        self._classifiers = []
    
    # functions
    
    def add(self, error : dict, comment = "", classifier = "") -> None:
        self._errors.append(error)
        self._comments.append(comment)
        self._classifiers.append(classifier)
    
    def get_all(self):
        return [{"error" : error, "comment" : comment, "classifier" : classifier} for error, comment, classifier in zip(self.errors, self.comments, self.classifiers)]
    
    def save(self, filename: str, filepath: str):
        with open(os.path.join(filepath, filename), "w") as f:
            json.dump(self.get_all(), f, indent=4)
    
    @staticmethod
    def load(filename: str, filepath: str):
        self = ErrorCollection()
        with open(os.path.join(filepath, filename), "r") as f:
            data = json.load(f)
        for item in data:
            classifier = ""
            if "classifier" in item.keys():
                classifier = item["classifier"]
            self.add(item["error"], item["comment"], classifier)
        return self

    def set_classifier(self, error_index: int, classifier: str) -> None:
        self._classifiers[error_index] = classifier

    def set_comment(self, error_index: int, comment: str) -> None:
        self._comments[error_index] = comment

    # properties
    
    @property
    def errors(self):
        return self._errors
    
    @property
    def comments(self):
        return self._comments

    @property
    def classifiers(self):
        return self._classifiers
        
    # iterator functions
    def __iter__(self):
        self._iter_index = 0
        return self

    def __next__(self):
        if self._iter_index + 1 > len(self):
            self._iter_index = 0
            raise StopIteration
        else:
            self._iter_index += 1
            return self._errors[self._iter_index-1]

    def __getitem__(self, key):
        if isinstance(key, int):
            return self._errors[key]
        else:
            raise KeyError(f'Unable to interpret as index: {key} of type {type(key)}.')
    
    def __len__(self):
        return len(self._errors)