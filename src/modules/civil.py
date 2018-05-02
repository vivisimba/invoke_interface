# -*- coding: utf-8 -*-
'''
Created on 2018年4月23日

@author: Simba
'''


import data.data_config as DATA
import http_requests.http_requests as HTTP_REQUEST
import exception.myException as MYEXCEPTION


# del civil by repoid and civilID
def delCivilByRepoIDAndCivilID(repoID, civilID):
    url = "http://%s:%s/api/repositories/%s/entities/%s" % (DATA.DEEPCLOUD_IP, DATA.DEEPCLOUD_PORT, repoID, civilID)
    resDelCivilByRepoIDAndCivilIDObject = HTTP_REQUEST.del_request(url)
    if resDelCivilByRepoIDAndCivilIDObject[1] == 200:
        return resDelCivilByRepoIDAndCivilIDObject
    else:
        raise MYEXCEPTION.MyException("Delete civil by repoID and civilID error.")


# query civil by repoid
def queryCivilByRepoID(repoID):
    url = "http://%s:%s/api/repositories/%s/entities" % (DATA.DEEPCLOUD_IP, DATA.DEEPCLOUD_PORT, repoID)
    resQueryCivilByRepoIDObject = HTTP_REQUEST.get_request(url)
    if resQueryCivilByRepoIDObject[1] == 200:
        return resQueryCivilByRepoIDObject
    else:
        raise MYEXCEPTION.MyException("Query civil by repoID error.")
