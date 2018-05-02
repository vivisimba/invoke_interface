# -*- coding: utf-8 -*-
'''
Created on 2018年4月23日

@author: Simba
'''


import data.data_config as DATA
import http_requests.http_requests as HTTP_REQUEST


# 查询设备列表
def getSensorList():
    url = DATA.GET_SENSOR_LIST_URL
    resObject = HTTP_REQUEST.get_request(url)
    if resObject[1] == 200:
        # print resObject[0]["list"]
        return resObject