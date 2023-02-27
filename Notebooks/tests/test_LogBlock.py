import pytest
import sys

sys.path.append("..")

from data_model import LogBlock, dicts_match

@pytest.fixture()
def mock_textblock():
    text = """Write Command
TestCommand
Write stderr
TestSTDERR
Write stdout
TestSTDOUT
Write timestamp
01:01:01
Reproduce this
TestRandomSeeds
-------------------------------------""".split("\n")
    return text

@pytest.fixture()
def mock_parser_stderr():
    stderr = """
ERROR    nomad.cli            YYYY-MM-DDThh:mm:ss Error description 1
  - example: key1
  - example2: key2 and something: else
ERROR    nomad.cli            YYYY-MM-DDThh:mm:ss Error description 2
  - exception: Traceback (most recent call last):
      File "some/path/some/file.py", line 68, in some_function
        object.function(arg1, arg2, kwarg=kwarg)
    TypeError: Wrong
  - example: key1
  - example2: key2 and something: else
Traceback (most recent call last):
  File "some/path/in/nomad", line 7, in <module>
    some_problem0(cause0)
  File "some/path/in/nomad", line 8, in <module>
    some_problem(cause)
module.CustomError: Uncaught error in the code"""
    return stderr.split("\n")

def test_dicts_match():
    reference = {"A" : "a", "B":["b","bb"]}
    candidate_matches_0 = {"A" : "a", "B":["b", "bb"], "C": "c"}
    candidate_matches_1 = {"A" : "a", "B":["b", "bb", "bbb"], "C": "c"}
    candidate_matches_not_0 = {"A":"a", "C":"c"}
    candidate_matches_not_1 = {"A":"a", "B":"b"}
    candidate_matches_not_2 = {"A":"a", "B":["b"]}

    assert dicts_match(candidate_matches_0, reference), "Does not match correct dictionaries"
    assert dicts_match(candidate_matches_1, reference), "Does not match dictionaries with additional list items"
    assert not dicts_match(candidate_matches_not_0, reference), "Matches dicts with differing keys"
    with pytest.raises(TypeError):
        dicts_match(candidate_matches_not_1, reference)
    assert not dicts_match(candidate_matches_not_2, reference), "Matches dict with missing entries"

def test_LogBlock_init(mock_textblock):

    def mock_run_path_generator(_, suffix):
        return suffix

    log = LogBlock(mock_textblock, run_id=1, code="TEST", run_path_generator=mock_run_path_generator, suffix = ".testSuffix")

    assert log.prog_call == "TestCommand", "Wrong command read from text block"
    assert log.stderr == ["TestSTDERR"], "Wrong STDERR from text block"
    assert log.stdout == ["TestSTDOUT"], "Wrong STDOUT from text block"
    assert log.timestamp == "01:01:01", "Wrong timestamp from text block"
    assert log.rndnrs == "TestRandomSeeds", "Wrong random seed from text block"
    assert log.floatified_input_path == ".testSuffix", "Wrong parser input data path"

def test_LogBlock_parse_stderr(mock_parser_stderr):
    
    log = LogBlock(None)

    log.stderr = mock_parser_stderr

    result = log.parse_stderr()

    expected = [
        {'message': 'Error description 1', 
        'error_type': 'ERROR', 'traceback': '', 
        'example': 'key1', 
        'example2': 'key2 and something: else'}, 
        {'message': 'Error description 2', 
        'error_type': 'ERROR', 
        'traceback': '  - exception: Traceback (most recent call last):      File "some/path/some/file.py", line 68, in some_function        object.function(arg1, arg2, kwarg=kwarg)    TypeError: Wrong', 'example': 'key1', 'example2': 'key2 and something: else'}, {'additional_exceptions': 
            ['Traceback (most recent call last):', '  File "some/path/in/nomad", line 7, in <module>', '    some_problem0(cause0)', '  File "some/path/in/nomad", line 8, in <module>', '    some_problem(cause)', 'module.CustomError: Uncaught error in the code']}]

    assert result == expected, "Parsing STDERR failed"

