# -*- coding: utf-8 -*-
'''
Created on 2018年4月23日

@author: Simba
'''


import data.data_config as DATA
import http_requests.http_requests as HTTP_REQUEST
import exception.myException as MYEXCEPTION
import logging


# 增加
def addRepo():
    # 添加比对库
    resObject = HTTP_REQUEST.post_request(DATA.ADD_REPO_URL, DATA.ADD_REPO_SOURCE)
    if resObject[1] == 201:
        print "Add repo successfully."
        print resObject[0]
        return resObject
        
        
# 删除
def delRepoById(repoId):
    url = "http://%s:%s/api/repositories/%s" % (DATA.DEEPCLOUD_IP, DATA.DEEPCLOUD_PORT, repoId)
    resDelRepoByIdObject = HTTP_REQUEST.del_request(url)
    if resDelRepoByIdObject[1] == 200:
        logging.info("repo %s has been deleted." % repoId)
        return resDelRepoByIdObject
    else:
        print resDelRepoByIdObject[1]
        raise MYEXCEPTION.MyException("Delete repo by repoID error.")

# 查询
def queryRepoById(repoId):
    url = DATA.QUERY_REPO_BY_ID_URL.replace("repo _id_str", repoId)
    resObject = HTTP_REQUEST.get_request(url)
    if resObject[1] == 200:
        print resObject[0]
        return resObject


# 查询比对库列表
def getRepoList():
    url = DATA.GET_REPO_LIST_URL
    resObject = HTTP_REQUEST.get_request(url)
    if resObject[1] == 200:
        print resObject[0]["list"]
        return resObject

        
    