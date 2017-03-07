#coding=utf-8
from PIL import ImageGrab
import csv,codecs
class ECMlibs(object):
    def __init__(self, BsObject):
        self.BsObject = BsObject
#登录手机端
    def LoginM(self,domain,usrname,usrpwd):
        try:
            self.BsObject.get("http://"+domain+"/m/login?weixinAutoLogin=false")
            self.BsObject.find_element_by_id("J_LoginUser").send_keys(str(usrname))
            self.BsObject.find_element_by_id("J_LoginPsw").send_keys(str(usrpwd))
            self.BsObject.find_element_by_id("J_LoginBtn").click()
            #raise
        except:
            im = ImageGrab.grab()
            im.save('d:\\Login.jpg','jpeg')
            print u"登录出错，已截图到'd:\Login.jpg'"
# 登录PC端
    def LoginP(self,domain,usrname,usrpwd):
        try:
            self.BsObject.get("http://"+domain+"/login.html?successUrl=%2F")
            self.BsObject.find_element_by_name("j_username").send_keys(str(usrname))
            self.BsObject.find_element_by_name("j_password").send_keys(str(usrpwd))
            self.BsObject.find_element_by_id("loginBtn").click()
        except:
            im = ImageGrab.grab()
            im.save('d:\\Login.jpg','jpeg')
            print u"登录出错，已截图到'd:\Login.jpg'"
# 退出登录（链接带虚拟组织ID）
    def Logout(self,tid):
        try:
            self.BsObject.execute_script('javascript:doLogout('+str(tid)+');')
        except:
            im = ImageGrab.grab()
            im.save('d:\\Logout.jpg','jpeg')
            print u"退出出错，已截图到'd:\Logout.jpg'"
#读文件所有数据，并按行显示
    def ReadFile(self,filename):
        try:
            with open(filename,'r') as f:
                     for line in f.readlines():
                         print(line.strip())
                         time.sleep(1)
        except:
            print "文件读取错误！！"
#写List数据到CSV文件，追加方式一行行写入

    def SaveListAsCsv(self,filename,list):
        try:
            with open(filename,'a') as f:
                f.write("组织ID,用户名,密码\n".decode('utf-8').encode('gb2312'))
            contain=""
            for values in list:
                contain=contain+str(values)+","
            contain=contain+'\n'
            with open(filename,'a') as f:
                f.write(contain)
        except:
            print "文件写入错误！！"
#写List内包含多组的数据到CSV文件，覆盖方式写入list所有数据，一个组一行
    def SaveMutiListAsCsv(self,filename,list):
        try:
            csvfile = file(filename, 'wb')
            csvfile.write(codecs.BOM_UTF8) #防乱码
            writer = csv.writer(csvfile)
            writer.writerow(['id', 'url', 'keywords'])
            writer.writerows(list)
            csvfile.close()
        except:
                print "文件写入错误！！"
#读取CSV文件中的字段做参数
    def ReadCsvAsParameters(self,filename):
        try:
            for line in open(filename):
                tid,username,userpwd = line.split(",")
                tid = tid.strip(' \t\r\n')
                username = username.strip(' \t\r\n')
                userpwd = userpwd.strip(' \t\r\n')
                print (tid + '\t' + username + '\t' + userpwd)
            return tid,username,userpwd
        except:
            print "文件读取错误！！"
