#!/usr/bin/env python3
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, project_root)

from lib.bool_functions import return_true

def test_return_true():
    '''in bool_functions, function "return_true" returns True.'''
    assert return_true() == True
