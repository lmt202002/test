#-*-coding=utf-8 -*-
import unittest,time
from selenium import webdriver
from mylibs.ecm import ECMlibs
import HTMLTestRunner
class test2(unittest.TestCase):
    def setUp(self):
        self.s='abc'

    def test2(self):
        self.browser=webdriver.Firefox()
        self.browser.get('https://login.taobao.com/member/login.jhtml')
        self.browser.maximize_window()
        # self.browser.find_element_by_id('su').click()
    def test3(self):
        self.browser=webdriver.Firefox()
        self.browser.get('http://www.baidu.com/')
        time.sleep(2)
        self.browser.find_element_by_id('dd').click()
    def tearDown(self):
        self.browser.quit()
        # os.system('E:\\test\\%s 1>>log.txt 2>&1'%self.test3())
# if __name__ =="__main__":
# unittest.main()
# now=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
resultdir='E:\\test'
testunit=unittest.TestSuite()
testunit.addTest(test2('test2'))
testunit.addTest(test2('test3'))
# filename='E:\\test\\'+now+'result.html'
# fp=file(filename,'wb')
# runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'XXX测试报告',description=u'用例执行情况：')
# # runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'云智测试报告',description=u'用例执行情况：')
aa=ECMlibs(object)
aa.PrintResult(resultdir,testunit)


