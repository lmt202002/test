#coding=utf8
import os,sys,unittest,CatchResultAndSendMail
from mylibs.ecm import ECMlibs
#设置测试用例目录，测试test开头用例
testcaselist=unittest.defaultTestLoader.discover(os.getcwd()+'\\testcase',pattern='test*.py',top_level_dir=None)
#创建测试套件
testunit=unittest.TestSuite()
#循环读取用例目录中的用例
for testcase1 in testcaselist:
    testunit.addTest(testcase1)
rununit=ECMlibs(object)
#执行用例并保存报告
rununit.SaveResult(os.getcwd()+'\\testresult',testunit)
#获取报告目录最新报告并发邮件
CatchResultAndSendMail.SendResult()
