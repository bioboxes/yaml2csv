"""\
yaml2csv - convert YAML/JSON inputs to comma separated key value pairs.

Usage:
    yaml2csv [options] --input=<in_yaml> --output=<out_csv>

Options:
    --input=<in_yaml>     Source YAML/JSON file.
    --output=<out_csv>    Destination file for CSV output.
    --downcase            Convert all uppercase keys to lowercase.
    --strict-keys         Converts all non [A-Za-z0-9_.] characters into a single underscore.
    --convert-bools       Converts True/False booleans to 1/0 integers.
"""

import csv, re
import ruamel.yaml as yaml

from docopt           import docopt
from yaml2csv.version import __version__


def has_arg(key, args):
    return (key in args) and args[key]


def parse_args(args):
    return docopt(__doc__, args, True, version = __version__)


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


def possibly_convert_bool(i):
    if type(i) == bool:
        return int(i)
    else:
        return i


def format(data, opts):
    if has_arg('--strict-keys', opts):
        data = map(lambda x: (re.sub(r'[^A-Za-z0-9._]+', '_', x[0]), x[1]), data)
    if has_arg('--downcase', opts):
        data = map(lambda x: (x[0].lower(), x[1]), data)
    if has_arg('--convert-bools', opts):
        data = map(lambda x: (x[0], possibly_convert_bool(x[1])), data)
    return list(data)


def convert(data, opts):
    return format(list(flatten_dict(data).items()), opts)



def run(args):
    opts = parse_args(args)
    with open(opts['--input'], 'r') as in_file:
        with open(opts['--output'], 'w') as out_file:
            in_data = yaml.load(in_file.read())
            out_data = csv.writer(out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in convert(in_data, opts):
                out_data.writerow(row)
