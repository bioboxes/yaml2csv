"""\
yaml2csv - convert YAML/JSON inputs to comma separated key value pairs.

Usage:
    yaml2csv [options] --input=<in_yaml> --output=<out_csv>

Options:
    --input=<in_yaml>       Source YAML/JSON file
    --output=<out_csv>      Destination file for CSV output
    --downcase              Convert all uppercase keys to lowercase
"""

import csv
import ruamel.yaml as yaml

from docopt           import docopt
from yaml2csv.version import __version__


# http://codereview.stackexchange.com/a/21035/129868
def flatten_dict(data):
    def items():
        for key, value in data.items():
            if isinstance(value, dict):
                for subkey, subvalue in flatten_dict(value).items():
                    yield key + "." + subkey, subvalue
            else:
                yield key, value

    return dict(items())


def format(data, opts):
    if ('--downcase' in opts) and opts['--downcase']:
        data = map(lambda x: (x[0].lower(), x[1]), data)
    return list(data)


def convert(data, opts):
    return format(list(flatten_dict(data).items()), opts)


def parse_args(args):
    return docopt(__doc__, args, True, version = __version__)


def run(args):
    opts = parse_args(args)
    with open(opts['--input'], 'r') as in_file:
        with open(opts['--output'], 'w') as out_file:
            in_data = yaml.load(in_file.read())
            out_data = csv.writer(out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in convert(in_data, opts):
                out_data.writerow(row)
