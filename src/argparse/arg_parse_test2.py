import argparse

parser = argparse.ArgumentParser()
parser.add_argument("echo", help="echo the string you use here")
# parse_args() method actually returns some data from the options specified, in this case, echo
args = parser.parse_args()
print(args.echo)
