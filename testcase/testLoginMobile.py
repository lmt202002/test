#coding=utf-8
from selenium import webdriver
from mylibs.ecm import ECMlibs
import unittest
import time,os,HTMLTestRunner
#确定测试的服务器域名
class testlist(unittest.TestCase):
#初始化
    def setUp(self):
        self.URL="o2oonline64.ecmaster.cn"
        #确定虚拟组织
        self.tid=1150
        #确定用户名密码
        self.username=13211110001
        self.userpwd=1
        self.browser=webdriver.Firefox()
        # time.sleep(2)
#用例列表
    def test64(self):
        LoginM1=ECMlibs(self.browser)
        LoginM1.LoginM(self.URL,self.username,self.userpwd)
        time.sleep(5)
        LoginM1.Logout(self.tid)
        time.sleep(2)
#结束处理
    def tearDown(self):
        self.browser.quit()
#执行
if __name__ =="__main__":
    unittest.main()