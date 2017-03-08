#-*-coding=utf-8 -*-
import unittest,time
from selenium import webdriver
from mylibs.ecm import ECMlibs
from testcase import test3
resultdir='E:\\test'
testunit=unittest.TestSuite()
testunit.addTest(unittest.makeSuite(test3.testCase))
aa=ECMlibs(object)
aa.PrintResult(resultdir,testunit)


