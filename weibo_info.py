#
# weibo_info.py
#
# RobotFlying 2013-08-01
#

#! /usr/bin/python3
# -*- encoding:utf-8 -*-

from weibo_entry import WeiboEntry
from log import log

class WeiboInfo:
    """
    WeiboInfo is a data struct to store data cralwed from webpages
    """

    def __init__(self,weibo_entry):
        self.__mid = weibo_entry.get_mid()
        self.__url,self.__user_id = weibo_entry.get_url()
        self.__time = weibo_entry.get_create_time()
        self.__text = weibo_entry.get_text()
        self.__forward_num = weibo_entry.get_forward_num()
        self.__reply_num = weibo_entry.get_reply_num()

    def print(self):
        log("mid",self.__mid)
        log("url",self.__url)
        log("user_id",self.__user_id)
        log("time",self.__time)
        log("forward_num",self.__forward_num)
        log("reply_num",self.__reply_num)
        log("text",self.__text)
