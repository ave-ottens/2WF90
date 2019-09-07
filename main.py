import argparse
import sys
from Context import *

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help='name of input file')
parser.add_argument('output', help='name of output file')

args = parser.parse_args()

input  = open(args.input, 'r') if args.input else sys.stdin
output = open(args.output, 'w', encoding='utf-8')

context = Context()

if not args.input:
    print('Interactive mode. Ctrl-Z plus Return to exit.')

for line in input:
    out = context.read_line(line)
    output.write(out)

    if not args.input:
        print(f'OUT: {repr(out)}')
