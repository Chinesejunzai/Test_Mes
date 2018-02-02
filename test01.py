#!/usr/bin/env python
# encoding=utf-8

'''
@author: houxiaojun
@license: (C) Copyright 2017
@contact: Chinesejunzai@163.com
@software: garner
@file: test01.py
@time: 2018/1/25 14:36
@desc:
'''
import pytest
class Test_ST:

    def setup(self):
        print(">>>setup")
    def teardown(self):
        assert False
        print(">>>teardown")
    def test_001(self):
        assert True
    def test_002(self):


