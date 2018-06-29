#! /usr/bin/env python3

import sys, os
sys.path.append(os.getcwd())

import re, time
import lib.basic_python3

def test_strftime():
    time_string = '2016-01-10T13:30:33'
    time_tuple = time.strptime(time_string, '%Y-%m-%dT%H:%M:%S')
    assert lib.basic_python3.strftime(time_tuple) == time_string

def test_strftime_now():
    time_string = lib.basic_python3.strftime_now()
    assert re.match("\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}", time_string)
