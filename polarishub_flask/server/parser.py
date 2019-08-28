import argparse
import logging

parser = argparse.ArgumentParser()
parser.add_argument("--verbose", help = "Show all the logs in terminal.", action = "store_true")

args = parser.parse_args()
verbose = args.verbose
if verbose:
    print("Running on verbose version.")
else:
    print("Running on quiet version.")
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)

print("To open PolarisHub: http://localhost:5000/")

def printv(*args):
    if verbose:
        print(*args)