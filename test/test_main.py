import yaml2csv.main as y2c

def test_parse_args():
    assert y2c.parse_args(['--input', '1', '--output', '2']) ==\
            {'--input' : '1',
             '--output' : '2',
             '--downcase' : False,
             '--strict-keys' : False,
             '--convert-bools' : False}

def assert_converted(input_, expected):
    assert y2c.convert(input_, {}) == expected


def test_convert_single_key_value_pair():
    args = {"key" : "value"}
    expected = [("key", "value")]
    assert_converted(args, expected)

def test_convert_multiple_key_value_pair():
    args = {"key_1" : "value_1", "key_2" : "value_2"}
    expected = [("key_1", "value_1"), ("key_2", "value_2")]
    assert_converted(args, expected)

def test_convert_single_nested_key_value_pair():
    args = {"key_1" : { "key_2" : "val"}}
    expected = [("key_1.key_2", "val")]
    assert_converted(args, expected)


def test_convert_multiple_nested_key_value_pair():
    args = {"key_1" : { "key_2" : "val_1"}, "key_3" : { "key_4" : "val_2"}}
    expected = [("key_1.key_2", "val_1"), ("key_3.key_4", "val_2")]
    assert_converted(args, expected)


def test_convert_multiple_nested_key_value_pair():
    args = {"key_1" : { "key_2" : "val_1"}, "key_3" : { "key_4" : "val_2"}}
    expected = [("key_1.key_2", "val_1"), ("key_3.key_4", "val_2")]
    assert_converted(args, expected)


def test_format_uppercase_key():
    data = [("KEY", "value")]
    expected = [("key", "value")]
    assert y2c.format(data, {'--downcase' : True}) == expected


def test_format_strict_keys():
    data = [("has  |space", "value")]
    expected = [("has_space", "value")]
    assert y2c.format(data, {'--strict-keys' : True}) == expected

def test_format_booleans():
    data = [("key_1", True), ("key_2", False)]
    expected = [("key_1", 1), ("key_2", 0)]
    result = y2c.format(data, {'--convert-bools' : True})
    assert result == expected
    assert type(result[0][1]) == int
    assert type(result[1][1]) == int
