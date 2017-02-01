import yaml2csv.main as y2c

def test_parse_args():
    assert y2c.parse_args(['--input', '1', '--output', '2']) ==\
            {'--input' : '1', '--output' : '2'}

def assert_converted(input_, expected):
    assert y2c.convert(input_) == expected


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
