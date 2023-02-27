# Analysis of NOMAD parser execution traces

This file describes how the analysis of the results of grammer-based fuzzing on the NOMAD parsers is performed.

## Usage

1. Generate Jupyter notebooks for manual classification
The command
```bash
python gen_analysis_notebook.py <code> <notebook filename> <data filename>
```
will generate a notebook with specified name for the given parser and store the data required for the analysis in a data file.

2. Execute notebooks 
Open the notebooks and stepwise execute the cells. In the first code cells of the notebooks, a `ErrorCollection()` is initialized. In the later parts of the notebook, the found errors are displayed, sorted by success (*successful*, *failed*, or *crashed*), and consequently by the unique combinations of NOMAD *error hashes*, and data written to *STDERR*.

3. Classify errors
For each set of errors, find unclassified errors by executing the cells including `find_unknown_errors(error_collection)`. This will output the logs of NOMADs own error handling system as well as any uncaught exceptions. This data can be used to analyze the cause of the error. Add the error to the `error_collection` using the available data, e.g.:
```python
error_collection.add({
    'message' : 'parsing failed',
    'error_type' : 'ERROR',
    'nomad.cli.parser' : 'parsers/<parser_name>'}, 
    comment = "Error that is triggered by [...]", 
    classifier = "Critical")
```

4. Generate report
To generate the report, save the `error_collection`s in each notebook for code `<code>` as `final_<code>_error_collection_classified.json`. Run the report generator using:
```bash
python gen_report_markdown.py
```