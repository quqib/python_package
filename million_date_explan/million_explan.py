# 计算 spark dask ray
# 存储 hdfs s3 分布式数据库
# 调度 airflow prefect 管理数据pipline
import time

import requests

mainUrl = 'https://zfcg.jxf.gov.cn/gpcms/rest/web/v2/info/selectInfoForIndex?'

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 UOS Community', 'sign': 'f39468525cdc4ac1d9c4666b96a56fed', 'time': '1767685494521', 'url': '/gpcms/rest/web/v2/index/getDeploymentSiteId'}

params = {'_t': 1767685494519, 'agency': '', 'channel': 'c5bff13f-21ca-4dac-b158-cb40accd3035', 'cityOrArea': '', 'currPage': 1, 'noticeType': '59', 'openTenderCode': '', 'operationEndTime': '2026-01-06 23:59:59', 'operationStartTime': '2026-01-04 00:00:00', 'pageSize': 10, 'purchaseManner': '', 'purchaseNature': '', 'purchaser': '', 'region': '', 'regionCode': '', 'siteId': '93BB7F0CFA5A6362B1100531C50AE36B', 'title': '', 'verifyCode': '3117'}

resTotal = requests.get(mainUrl, data=params, headers=headers)

print(resTotal.text)


