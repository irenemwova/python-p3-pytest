#!/usr/bin/env python3
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, project_root)

from lib.not_none_functions import return_not_none

# def test_return_not_none():
#     '''in not_none_functions, function "return_not_none" returns a value that is not None.'''
#     assert False
