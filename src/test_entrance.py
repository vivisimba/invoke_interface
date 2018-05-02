# -*- coding: utf-8 -*-
'''
Created on 2018年4月23日

@author: Simba
'''


import logService.logService as logService
import modules.repo as REPO
import logging
import modules.sensor as SENSOR
import modules.rule as RULE
import json
import modules.civil as CIVIL




def run():
    # 添加比对库
#     repoObject = REPO.addRepo()
#     logging.info("new repo id is :" + repoObject[0]["id"])

    # RULE
    
    ruleSource = { 
        "repositories": [
            {
                "id":"22e1bed6-ee8f-4a68-8c5c-5d07a19293b6",
                "threshold": 0.6
                }
            ],
        "source_id": "",
        "times": {
            "is_persistent": True
            }
        }
    
    # 比对库ID
    repoId = "7afeb686-aab9-4da0-b3e4-26c8960febbd"
    
    # 获得所有设备ID列表
    sensorIdList = []
    sensorList = SENSOR.getSensorList()[0]["list"]
    for i in sensorList:
        sensorIdList.append(i["id"])
        
    # 循环为所有设备添加布控 RULE
    for j in sensorIdList:
        rightSource = ruleSource
        rightSource["source_id"] = j
        resAddRuleObject = RULE.addRule(rightSource)
        
        
    


# 删除指定repo中的所有civil
def delAllCivilInRepo(repoID):
    # 查询，获得指定repo中的所有civil
    resQueryCivilByRepoIdObject = CIVIL.queryCivilByRepoID(repoID)
    print resQueryCivilByRepoIdObject
    print resQueryCivilByRepoIdObject[0]["count"]
    print len(resQueryCivilByRepoIdObject[0]["list"])
    civilIdList = []

    for i in resQueryCivilByRepoIdObject[0]["list"]:
        civilIdList.append(i["id"])
    
    for j in civilIdList:
        resDelCivilByRepoIdAndCivilIdObject = CIVIL.delCivilByRepoIDAndCivilID(repoID, j)
        logging.info("Civil %s has been deleted" % j)

        
    
    
    





if __name__ == '__main__':
    logService.initLogging()
    '''
    :param 脚本本身
    '''
    run()
    #REPO.delRepoById("dfbdd1e2-4e45-4bdf-86bd-a7a07c6bd034")
#     RULE.delRuleById("1559031680")

     
    logService.destoryLogging()