"""\
yaml2csv - convert YAML/JSON inputs to comma separated key value pairs.

Usage:
    yaml2csv --input=<in_yaml> --output=<out_csv>

Options:
    --input=<in_yaml>     Source YAML/JSON file
    --output=<out_csv>    Destination file for CSV output
"""

import csv
import ruamel.yaml as yaml

from docopt           import docopt
from yaml2csv.version import __version__


def convert(data):
    return list(data.items())

def parse_args(args):
    return docopt(__doc__, args, True, version = __version__)

def run(args):
    opts = parse_args(args)
    with open(opts['--input'], 'r') as in_file:
        with open(opts['--output'], 'w') as out_file:
            in_data = yaml.load(in_file.read())
            out_data = csv.writer(out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in convert(in_data):
                out_data.writerow(row)
