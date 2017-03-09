#coding=utf8
import os,sys,unittest
from mylibs.ecm import ECMlibs
#设置用例目录
testcasedir=os.getcwd()+'\\testcase'
#设置测试用例目录，测试test开头用例
testcaselist=unittest.defaultTestLoader.discover(testcasedir,pattern='test*.py',top_level_dir=None)
#创建测试套件
testunit=unittest.TestSuite()
#循环读取用例目录中的用例
for testcase1 in testcaselist:
    testunit.addTest(unittest.makeSuite(testcase1))
rununit=ECMlibs(object)
rununit.SaveResult(testcasedir,testunit)