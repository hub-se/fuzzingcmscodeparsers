This repository contains the files to reproduce the results of our paper "Grammar-based Fuzzing of Data Integration Parsers in Computational Materials Science" (DOI: http://doi.org/10.1002/spe.3266).

Before running the experiments, download the required libraries (as mentioned in the paper, Tribble is already included in the repository).

To reproduce the experiments:

    git clone https://github.com/hub-se/fuzzingcmscodeparsers.git  
    cd ./fuzzingcmscodeparsers/Data/scripts      
    python3 experiments.py  

For further information use `python3 experiments.py -h`. 

The data which was used for the evaluation as presented in the paper is available [here](https://zenodo.org/records/10159310)

For the analysis of the results, refer to: [Readme for the analysis pipeline](https://github.com/hub-se/fuzzingcmscodeparsers/blob/main/Notebooks/README.md)
