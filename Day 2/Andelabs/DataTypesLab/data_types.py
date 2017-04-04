#!/usr/bin/env python
# encoding: utf-8

"""
TODO:
string returns length of string
None returns 'no value'
Booleans return the boolean itself
integers return a string of how it compares to 100
lists return the third item or None if it doesnt exist

"""

def data_type(data):
    if isinstance(data, str):
        return len(data)
    elif data is None:
        return 'no value'
    elif isinstance(data, bool):
        return data
    elif isinstance(data, int):
        if data < 100:
            return 'less than 100'
        if data == 100:
            return 'equal to 100'
        if data > 100:
            return 'more than 100'
    elif isinstance(data, list):
    	if len(data) < 3:
    		return None
    	else:
        	return data[2]
    else:
        return None
