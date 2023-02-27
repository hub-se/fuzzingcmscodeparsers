#The experiments, run without arguments to reproduce the original experiments
import os
import sys
import shutil
from multiprocessing.pool import Pool
import subprocess
from datetime import datetime, timedelta
import time
import random
from struct import pack, unpack
import argparse
import ast
from multiprocessing.pool import Pool
from datetime import datetime, timedelta
from struct import pack, unpack

from floatifier import floatify

#The Seed for the feasability runs
SEED = 42
#The concrete program call for the nomad-lab environment
NOMAD = "nomad"

#Dictionary for the targeted nomad parsers; the key is any name (unique), the value is a list containing tuples containing:
#1st the path to the grammar
#2nd the location for the generated files
#3rd the file extension for the files
#4th if it exists the name which the file has to have to be parsable by nomad
#Each tuple defines its own output so that nomad parsers with several distinct output formats can be tested
TARGETS = {
           "exciting" : [(os.path.join("..", "exciting", "infoout.grammar"), "output", "txt", "INFO.OUT")],
           "aims" : [(os.path.join("..", "aims", "out.grammar"), "output", "txt", "")],
           "espresso" : [(os.path.join("..", "espresso", "out.grammar"), "output", "txt", "")],
           "vasp" : [(os.path.join("..", "vasp", "out.grammar"), "output", "xml", "")]
           }


def generate_suite(path_to_grammar, out_directory,
                   file_extension, seed, files=100,
                   derivation_limits=(150, 250)):
    """The test suite generator, employs tribble to generate a
    default 100 files (files parameter) with derivations between 150 and 250 (derivation_limits parameter).
    A result can only be reproduced if and only if generation and reproduction use the same files and derivation_limits values"""

    subprocess.call(["java", "-Xss1g", "-Xms256m", "-Xmx4g", "-jar",
                     "./inputGenerator/tribble.jar", "generate",
                     "--suffix=." + file_extension,
                     "--mode=" + str(derivation_limits[0]) + "-"
                     + str(derivation_limits[1]) + "-probabilistic-" + str(files),
                     "--out-dir=" + out_directory,
                     "--random-seed=" + str(seed),
                     "--grammar-file=" + path_to_grammar])


def sanitise_names(in_folder):
    """Removes UUIDs from tribble-generated files"""

    for file_ in sorted(os.listdir(in_folder)):
        print("Renaming " + os.path.join(in_folder, file_) + " to "
              + os.path.join(in_folder, file_.split('_')[0] + os.path.splitext(file_)[1]))
        shutil.move(os.path.join(in_folder, file_),
                    os.path.join(in_folder, file_.split('_')[0] + os.path.splitext(file_)[1]))


def floatify_suite(in_folder, out_folder, random_number_generator):
    """Inserts concrete floats into the generated samples"""

    file_seeds = dict()
    for file_ in sorted(os.listdir(in_folder)):
        print("Inserting floats for " + os.path.join(in_folder, file_)
              + " and saving to " + os.path.join(out_folder, file_))
        seed = random_number_generator.getrandbits(64)
        file_seeds[os.path.join(out_folder, file_)] = seed
        floatify(os.path.join(in_folder, file_), os.path.join(out_folder, file_), seed)
    return file_seeds


def run_suite(loc, in_folder, out_folder, log_basename, name, reproduce_this):
    """Evaluates samples on nomad parse in parallel"""

    with Pool(30) as pool, \
         open(os.path.join(out_folder, log_basename + "_full"), 'w') as full:
        [pool.apply_async(create_temp_and_parse, (loc, os.path.join(in_folder, file_), index, name, reproduce_this, ))
                   for index, file_ in enumerate(sorted(os.listdir(in_folder)))]
        pool.close()
        pool.join()
        results = [os.path.join(loc, "tmp", file_) for file_ in sorted(os.listdir(os.path.join(loc, "tmp")), key=lambda x: x.split("-")[1])]
        for result in results:
            with open(result, "r") as res:
                full.write(res.read())
            os.remove(result)


def nomad_parse(file_):
    """Parse a file using nomad parse, returns the subprocess that parses the file."""

    print("Parsing " + file_)
    return subprocess.run([NOMAD, "parse", "--show-archive", file_], encoding="utf-8", stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def create_temp_and_parse(loc, file_, index, name, reproduce_this):
    """Creates a temporary folder for the file to be parsed and renames it according to the naming
    scheme, then calls nomad_parse and generates the log file for it."""

    path = os.path.splitext(os.path.join(loc, "tmp", os.path.basename(file_)))[0]
    os.makedirs(path)
    filename = os.path.basename(file_)
    if name != "":
        filename = name
    shutil.copy(file_, os.path.join(path, filename))
    start_time = time.monotonic()
    current = nomad_parse(os.path.join(path, filename))
    time_expired = timedelta(seconds=time.monotonic() - start_time)
    shutil.rmtree(path)
    with open(os.path.join(loc, "tmp", "tmp-{}".format(index)), 'w') as full:
        full.write("Write Command\n")
        full.write(" ".join(current.args) + "\n")
        full.write("Write stderr\n")
        full.write(current.stderr)
        full.write("Write stdout\n")
        full.write(current.stdout + "\n")
        full.write("Write timestamp\n")
        full.write(str(time_expired) + "\n")
        full.write("Reproduce this\n")
        full.write(str([reproduce_this[0], reproduce_this[1], file_, reproduce_this[2][file_]]) 
                   + "\n----------------------------------------------------\n\n")


def single_run(loc, seed, files=100):
    """A single run, both size and base seed are confiugurable."""

    sample_dir = os.path.join(loc, "samples")
    os.makedirs(sample_dir)
    floatified_dir = os.path.join(loc, "floatified")
    os.makedirs(floatified_dir)
    res_dir = os.path.join(loc, "res")
    os.mkdir(res_dir)
    times = dict()
    gen = random.Random()
    gen.seed(seed, version=2)
    for target in TARGETS:
        for entry in TARGETS[target]:
            reproduce_this = []
            reproduce_this.append(entry)
            start_time = time.monotonic()
            shutil.rmtree("automata", ignore_errors=True)
            seed = unpack("=l", pack("=L", gen.getrandbits(32)))[0]
            reproduce_this.append(seed)
            generate_suite(entry[0], os.path.join(sample_dir, target, entry[1]), entry[2], seed, files=files)
            sanitise_names(os.path.join(sample_dir, target, entry[1]))
            current_target = os.path.join(floatified_dir, target, entry[1])
            os.makedirs(current_target)
            file_seeds = floatify_suite(os.path.join(sample_dir, target, entry[1]), current_target, gen)
            reproduce_this.append(file_seeds)
            run_suite(loc, current_target, res_dir, target, entry[3], reproduce_this)
            time_expired = timedelta(seconds=time.monotonic() - start_time)
            times[target] = time_expired
    with open(os.path.join(loc, "metadata"), 'w') as f:
        f.write(str(times) + "\n")
        f.write("Seed: " + str(seed) + "\n")


def run_experiments(loc="run", skip_feasible=False, base_seed=-1, runs=30):
    """Runs the experimental setup, first the feasible run and then the random runs.
    Configurable to skip the feasibility run, set the amount of runs, the folder as well as the seed."""
    
    if os.path.exists(loc):
        shutil.make_archive('Backup-'
                            + str(datetime.now()).replace(":", "-").replace(" ", "-"), 'zip', loc)
        shutil.rmtree(loc)
    os.mkdir(loc)
    if not skip_feasible:
        feas_dir = os.path.join(loc, "feasible")
        os.mkdir(feas_dir)
        single_run(feas_dir, SEED)
    gen = random.Random()
    if base_seed == -1:
        base_seed = int(time.time())
    gen.seed(base_seed, version=2)
    for run in range(runs):
        current_dir = os.path.join(loc, "run-" + str(run))
        os.mkdir(current_dir)
        seed = unpack("=l", pack("=L", gen.getrandbits(32)))[0]
        single_run(current_dir, seed)
    shutil.make_archive('Backup-'
                        + str(datetime.now()).replace(":", "-").replace(" ", "-"), 'zip', loc)
    shutil.rmtree(loc)


def reproduce_floatify_suite(in_folder, out_folder, file_to_reproduce, file_seed):
    """Reproduces a single file, by inserting the same floats that were originally used."""

    file_seeds = dict()
    for file_ in sorted(os.listdir(in_folder)):
        if file_ == os.path.basename(file_to_reproduce):
            print("Inserting floats for " + os.path.join(in_folder, file_)
                  + " and saving to " + os.path.join(out_folder, file_))
            seed = file_seed
            file_seeds[os.path.join(out_folder, file_)] = seed
            floatify(os.path.join(in_folder, file_), os.path.join(out_folder, file_), seed)
    return file_seeds


def reproduce_file(reproduction_string, loc="reproduce"):
    """Uses the provided reproduction String to reproduce the corresponding file. the loc parameter describes the location where it is reproduced.
    If the folder exists it prompts to delete it and if the prompt is denied, it aborts."""

    reproduction_data = ast.literal_eval(reproduction_string)
    if os.path.exists(loc):
        userinput = input("Folder " + loc + " already exists, do you want to delete it? [Yn]")
        if userinput in ["", "y", "Y"]:
            shutil.rmtree(loc)
        else:
            print("Aborting")
            sys.exit()
    entry = reproduction_data[0]
    seed = reproduction_data[1]
    sample_dir = os.path.join(loc, "samples")
    os.makedirs(sample_dir)
    floatified_dir = os.path.join(loc, "floatified")
    os.makedirs(floatified_dir)
    res_dir = os.path.join(loc, "res")
    os.mkdir(res_dir)
    reproduce_this = []
    reproduce_this.append(entry)
    shutil.rmtree("automata", ignore_errors=True)
    reproduce_this.append(seed)
    generate_suite(entry[0], os.path.join(sample_dir, entry[1]), entry[2], seed, size=100)
    sanitise_names(os.path.join(sample_dir, entry[1]))
    current_target = os.path.join(floatified_dir, entry[1])
    os.makedirs(current_target)
    file_seeds = reproduce_floatify_suite(os.path.join(sample_dir, entry[1]), current_target, reproduction_data[2], reproduction_data[3])
    reproduce_this.append(file_seeds)
    run_suite(loc, current_target, res_dir, "reproduce", entry[3], reproduce_this)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='The experimental pipeline for fuzzing computational material science codes.')
    parser.add_argument('--seed','-s', default=-1, type=int, help="The base seed for all random runs.")
    parser.add_argument('--runs','-r', default=30, type=int, help="The amount of random runs.")
    parser.add_argument('--skip-feasible', default=False, action='store_true', help="Sets if the feasability run should be skipped.")
    parser.add_argument('--location', '-l', default="run", help="The generation location for reproduction and fuzzing.")
    parser.add_argument('--reproduce', default=False, help="Sets the tool into reproduction mode and takes the reproduction string (don't forget the \").")
    args = parser.parse_args()

    if args.reproduce == False:
        run_experiments(loc=args.location, skip_feasible=args.skip_feasible, base_seed=args.seed, runs=args.runs)
    else:
        reproduce_file(args.reproduce, loc=args.location)
