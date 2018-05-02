# -*- coding: utf-8 -*-
'''
Created on 2018年4月23日

@author: Simba
'''

# IP PORT
DEEPCLOUD_IP = "123.206.1.151"
DEEPCLOUD_PORT = "8082"


# REPO
# ADD
ADD_REPO_SOURCE = {"mode":"white_list","name":"Simba_test","type":"person","capacity":10000}
ADD_REPO_URL = "http://%s:%s/api/repositories" % (DEEPCLOUD_IP, DEEPCLOUD_PORT)

# QUERY REPO BY ID
REPO_ID = "repo _id_str"
QUERY_REPO_BY_ID_URL = "http://%s:%s/api/repositories/%s" % (DEEPCLOUD_IP, DEEPCLOUD_PORT, REPO_ID)

# GET REPO LIST
GET_REPO_LIST_OFFSET = ""
GET_REPO_LIST_LIMIT = "*"
GET_REPO_LIST_URL = "http://%s:%s/api/repositories?offset=%s&limit=%s" % (DEEPCLOUD_IP, DEEPCLOUD_PORT, GET_REPO_LIST_OFFSET, GET_REPO_LIST_LIMIT)


# SENSOR
# get sensor list
GET_SENSOR_LIST_OFFSET = ""
GET_SENSOR_LIST_LIMIT = "*"
GET_SENSOR_LIST_URL = "http://%s:%s/api/sources?offset=%s&limit=%s" % (DEEPCLOUD_IP, DEEPCLOUD_PORT, GET_SENSOR_LIST_OFFSET, GET_SENSOR_LIST_LIMIT)


# RULE
# add rule
ADD_RULE_URL = "http://%s:%s/api/monitors" % (DEEPCLOUD_IP, DEEPCLOUD_PORT)
