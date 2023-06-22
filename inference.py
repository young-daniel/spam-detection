from preprocessing import clean_message
import pickle

with open('pipeline.pickle', 'rb') as f:
    pipeline = pickle.load(f)
output_map = {0:'ham', 1:'spam'}

import argparse

parser = argparse.ArgumentParser(
    description="CLI for spam detection",
)

parser.add_argument("--file", "-f", required=True, help="File containing messages to process, one message per line")
parser.add_argument("--output", "-o", default=None, help="File to store inferences, otherwise prints to stdout")

args = parser.parse_args()

with open(args.file, 'r') as f:
    lines = f.readlines()
lines = [clean_message(line.strip()) for line in lines]
results = pipeline.predict(lines)
results = [output_map[result] for result in results]

if args.output:
    with open(args.output, 'w') as f:
        for result in results:
            f.write(result + '\n')
else:
    for result in results:
        print(result)

