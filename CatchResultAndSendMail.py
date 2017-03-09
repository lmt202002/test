#-*-coding=utf-8 -*-
from mylibs.ecm import ECMlibs

resultdir='E:\\test\\testresult'
newfile=ECMlibs(object)
filesource=newfile.CatchNewFile(resultdir)
newfile.SentMail(filesource)

