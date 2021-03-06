#coding=utf-8
import codecs
import csv
import datetime
import HTMLTestRunner
import os
import smtplib
import time
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from mylibs import location
from PIL import ImageGrab


class ECMlibs(object):
    def __init__(self, BsObject):
        self.BsObject = BsObject
        self.me=location
#截图并按用例函数名和时间命名
    def Screenshot(self,testname=''):
        self.BsObject.get_screenshot_as_file(os.getcwd()+'\\screenshot\\'+testname+ time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())+'.jpg')
#发邮件
    def SentMail(self,file_new):
    #发信邮箱
        mail_from='bruceloo@aliyun.com'
        #收信邮箱
        mail_to='bruceloo@aliyun.com;bruceloo@aliyun.com;'
        #定义正文
        f = open(file_new, 'rb')
        mail_body = f.read()
        f.close()
        msg=MIMEText(mail_body,_subtype='html',_charset='utf-8')
        #定义标题
        msg['from']=mail_from
        msg['to']=mail_to
        msg['Subject']=u"云智测试报告"
        #定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
        msg['date']=time.strftime('%a, %d %b %Y %H:%M:%S %z')
        smtp=smtplib.SMTP()
        #连接 SMTP 服务器，此处用的126的 SMTP 服务器
        smtp.connect('smtp.aliyun.com')
        #用户名密码
        smtp.login('bruceloo@aliyun.com','lmtlsl73')
        smtp.sendmail(mail_from,mail_to,msg.as_string())
        smtp.quit()
        print u'邮件发送成功!'
#打印报告
    def SaveResult(self,resultdir,testunit):
        now=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
        self.filename=resultdir+'\\'+now+'result.html'
        fp=file(self.filename,'wb')
        runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'云智测试报告',description=u'用例执行情况：')
        runner.run(testunit)
#获取目录下最新的文件
    def CatchNewFile(self,result_dir):
        self.result_dir = result_dir
        self.lists=os.listdir(self.result_dir)
        self.lists.sort(key=lambda fn: os.path.getmtime(self.result_dir+"\\"+fn) if not
        os.path.isdir(self.result_dir+"\\"+fn) else 0)
        print (u'最新的文件为： '+self.lists[-1])
        self.file = os.path.join(self.result_dir,self.lists[-1])
        print self.file
        return self.file
#登录手机端
    def LoginM(self,domain,usrname,usrpwd):
        try:
            self.BsObject.get("http://"+domain+"/m/login?weixinAutoLogin=false")
            self.me.findId(self.BsObject,"J_LoginUser").send_keys(str(usrname))
            self.me.findId(self.BsObject,"J_LoginPsw").send_keys(str(usrpwd))
            self.me.findId(self.BsObject,"J_LoginBtn").click()
            #raise
        except:
            im = ImageGrab.grab()
            im.save('d:\\Login.jpg','jpeg')
            print u"登录出错，已截图到'd:\Login.jpg'"
# 登录PC端
    def LoginP(self,domain,usrname,usrpwd):
        try:
            self.BsObject.get("http://"+domain+"/login.html?successUrl=%2F")
            self.me.findName(self.BsObject,"j_username").send_keys(str(usrname))
            self.me.findName(self.BsObject,"j_password").send_keys(str(usrpwd))
            self.me.findId(self.BsObject,"loginBtn").click()
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
