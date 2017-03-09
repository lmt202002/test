#coding=utf8
import time
import unittest

from selenium import webdriver


class testCase(unittest.TestCase):
    def setUp(self):
        self.s='abc'

    def testtaobao(self):
        u'''淘宝查看订单测试'''
        self.browser=webdriver.Firefox()
        self.browser.get('https://login.taobao.com/member/login.jhtml')
        self.browser.maximize_window()
        self.browser.find_element_by_id('su').click()
    def testbaidu(self):
        u'''百度搜索测试'''
        self.browser=webdriver.Firefox()
        self.browser.get('http://www.baidu.com/')
        time.sleep(2)
        self.browser.find_element_by_id('dd').click()
    def tearDown(self):
        self.browser.quit()