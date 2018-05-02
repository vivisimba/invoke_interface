# -*- coding: utf-8 -*-
'''
Created on 2018年4月23日

@author: Simba
'''


import data.data_config as DATA
import http_requests.http_requests as HTTP_REQUEST
import exception.myException as MYEXCEPTION


# 添加布控rule
def addRule(source):
    url = DATA.ADD_RULE_URL
    resObject = HTTP_REQUEST.post_request(url, source)
    print resObject
    if resObject[1] == 201:
        return resObject
    else:
        raise MYEXCEPTION.MyException("add rule error.")


# del rule by ID
def delRuleById(ruleId):
    url = "http://%s:%s/api/monitors/%s" % (DATA.DEEPCLOUD_IP, DATA.DEEPCLOUD_PORT, ruleId)
    resDelRuleByIdObject = HTTP_REQUEST.del_request(url)
    if resDelRuleByIdObject[1] != 200: # 此处按照文档描述，应该是204
        raise MYEXCEPTION.MyException("Del rule by id error. errorCode: %s, errorMessage: %s" % (resDelRuleByIdObject[0], resDelRuleByIdObject[1]))
    else:
        return resDelRuleByIdObject
    
    
    
    
    