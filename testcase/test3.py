#coding=utf8
import time
import unittest

from selenium import webdriver


class testCase(unittest.TestCase):
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