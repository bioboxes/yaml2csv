import os, re, os.path, shutil
from behave import *

def get_stream(context, stream):
    assert stream in ['stderr', 'stdout'], "Unknown output stream {}".format(stream)
    return getattr(context.output, stream)

def get_env_path(context, file_):
    return os.path.join(context.env.cwd, file_)

def assert_not_empty(obj):
    assert len(obj) > 0

def assert_file_exists(file_):
    assert os.path.isfile(file_), "The file \"{}\" does not exist.".format(file_)

def assert_file_not_empty(file_):
    with open(file_, 'r') as f:
        assert_not_empty(f.read().strip())

@given(u'I create the directory "{directory}"')
def step_impl(context, directory):
    os.makedirs(get_env_path(context, directory))

@given(u'I create the file "{file_}" with the contents')
def step_impl(context, file_):
    with open(get_env_path(context, file_), 'w') as f:
        f.write(context.text)

@when(u'I run the command')
def step_impl(context):
    context.output = context.env.run(
            "bash -c '{}'".format(os.path.expandvars(context.text)),
            expect_error  = True,
            expect_stderr = True)

@then(u'the {stream} should be empty')
def step_impl(context, stream):
    output = get_stream(context, stream)
    assert output == "",\
        "The {} should be empty but contains:\n\n{}".format(stream, output)

@then(u'the exit code should be {code}')
def step_impl(context, code):
    returned = context.output.returncode
    assert returned == int(code),\
        "Process should return exit code {} but was {}".format(code, returned)


@then(u'the file "{}" should exist')
def step_impl(context, file_):
    assert_file_exists(get_env_path(context, file_))

@then(u'the file "{file_}" should contain')
def step_impl(context, file_):
        path = get_env_path(context, file_)
        with open(path, 'r') as f:
            expected = context.text
            result = f.read()
            assert expected == result, "Error file contents do not match '{}' != '{}'".format(expected, result)

@then(u'the file "{}" should not be empty')
def step_impl(context, file_):
    assert_file_not_empty(get_env_path(context, file_))

@then(u'the following files should exist and not be empty')
def step_impl(context):
    for row in context.table.rows:
        file_ = get_env_path(context, row['file'])
        assert_file_exists(file_)
        assert_file_not_empty(file_)


@then(u'the {stream} should contain')
def step_impl(context, stream):
    output = get_stream(context, stream)
    assert context.text in output

@then(u'the {stream} should equal')
def step_impl(context, stream):
    output = get_stream(context, stream)
    assert context.text == output

@then(u'excluding warnings the {stream} should equal')
def step_impl(context, stream):
    output = get_stream(context, stream)
    assert context.text == remove_warnings(output)

@then(u'the {stream} should match /{regexp}/')
def step_impl(context, stream, regexp):
    output = get_stream(context, stream)
    assert re.match(regexp, output) != None,\
        "Regular expression {} not found in:\n'{}'".format(regexp, output)

@then(u'the directory "{}" should not exist')
def step_impl(context, dir_):
    assert not os.path.isdir(dir_),\
        "The directory \"{}\" should not exist.".format(dir_)