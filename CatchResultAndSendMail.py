#-*-coding=utf-8 -*-
from mylibs.ecm import ECMlibs
import os
def SendResult():
    currentdir=os.getcwd()
    # print(currentdir)
    resultdir=currentdir+'\\testresult'
    newfile=ECMlibs(object)
    filesource=newfile.CatchNewFile(resultdir)
    newfile.SentMail(filesource)
