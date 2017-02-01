import yaml2csv.main as y2c

def test_parse_args():
    assert y2c.parse_args(['--input', '1', '--output', '2']) ==\
            {'--input' : '1', '--output' : '2'}


def test_convert_single_key_value_pair():
    args = {"key" : "value"}
    expected = [("key", "value")]
    assert y2c.convert(args) == expected

def test_convert_multiple_key_value_pair():
    args = {"key_1" : "value_1", "key_2" : "value_2"}
    expected = [("key_1", "value_1"), ("key_2", "value_2")]
    assert y2c.convert(args) == expected
