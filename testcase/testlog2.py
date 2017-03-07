#-*-coding=utf-8 -*-
import unittest,time
from selenium import webdriver
import HTMLTestRunner
# class test2(unittest.TestCase):
#     def setUp(self):
#         self.s='abc'
#
#     def test2(self):
#         self.browser=webdriver.Firefox()
#         self.browser.get('http://www.baidu.com/')
#         time.sleep(2)
#         self.browser.find_element_by_id('su').click()
#     def test3(self):
#         self.browser=webdriver.Firefox()
#         self.browser.get('http://www.baidu.com/')
#         time.sleep(2)
#         self.browser.find_element_by_id('dd').click()
#     def tearDown(self):
#         self.browser.quit()
#         # os.system('E:\\test\\%s 1>>log.txt 2>&1'%self.test3())
# if __name__ =="__main__":
# # unittest.main()
#     testunit=unittest.TestSuite()
#     testunit.addTest(test2('test2'))
#     testunit.addTest(test2('test3'))
#     filename='E:\\test\\result.html'
#     fp=file(filename,'wb')
#     runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'云智测试报告',description=u'用例执行情况：')
#     runner.run(testunit)


class TestClass():
 arr1 = 2
 arr2 = 2

 def setUp(self):
     self.arr1 = 3
     self.arr2 = 3
     print "MyTestClass setup"

 def tearDown(self):
     print "MyTestClass teardown"

 def Testfunc1(self):
     assert self.arr1 == self.arr2

 def Testfunc2(self):
     assert self.arr1 == 3
