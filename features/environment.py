import os.path
from scripttest import TestFileEnvironment

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def before_scenario(context, _):
    context.env = TestFileEnvironment(base_path = os.path.join(root_dir, 'tmp/features'))
