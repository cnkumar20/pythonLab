#!/usr/bin/python

import sys
import requests

#print 'Number of arguments:', len(sys.argv), 'arguments.'
#$print 'Argument List:', str(sys.argv)
#args = sys.argv
create_data_type = ""

curl -H "Content-Type: application/json" -X POST \
-d '{"id":"qa.analysis_data_complete_Conversion","label":"qa.analysis_data_complete_Conversion","locator":"/heds/hive/land_logs.db","description":"qa.analysis_data_complete_Conversion","trim": 720}' http://datamanager.sj2.hadoop.vccorp.vclk.net:9080/rest/datatype


curl -H "Content-Type: application/json" -X POST \
-d '{"id":"qa.redacted_conversion", "owner":"DPL","email":"CNVR_DATATEAM@conversantmedia.com", "setting":"30","filter":"LastWholeHours","ackTrim":1440,"dataTypeSet":["qa.analysis_data_complete_Conversion","qa.orc_data_complete_Conversion"]} ' \
http://datamanager.sj2.hadoop.vccorp.vclk.net:9080/rest/job

1636344000000_1636347600000


payload = {"id":"qa.analysis_data_complete_Conversion_1636344000000_1636347600000", "starttime": 1636344000000, "endtime": 1636347600000, "datatype": "qa.analysis_data_complete_Conversion"}
a = requests.post('http://datamanager.sj2.hadoop.vccorp.vclk.net:9080/rest/data', data=payload)
a.status_code
