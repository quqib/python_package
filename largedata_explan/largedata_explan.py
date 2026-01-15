import requests

cookies = {
    'regionCode': '360001',
    'regionFullName': '%E6%B1%9F%E8%A5%BF%E7%9C%81%E6%9C%AC%E7%BA%A7',
    'regionRemark': '1',
    'TS0113089b': '011e290be00e5f91339e33a99f9021db5ceb2c0951fc235af4b7bfe572cc9b9b628ec0aa448d008e5b77adfbb2d7ce04b71bf11285',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://zfcg.jxf.gov.cn/maincms-web/massageListPageJx',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
    'nsssjss': 'YfMLhmyFm0h04We40AclUGQB5INQvqV6wEEA5+4QRCKo185OEWn4VqKEzmlD+P1dDkcfez61IkVkHYltO6bbwAzS4E2uA81rDkOkpptK27cou2y9hFbrAqVnPgdKtC+fTQktuQirN6jfyyGrraLNNXk+Y5d+VFTVzHw/8DJBl5M=',
    'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sign': '89c86f34132bf0e8a1f2e9c1f7b2628d',
    'time': '1767685970181',
    'url': '/gpcms/rest/web/v2/info/selectInfoForIndex',
    # 'Cookie': 'regionCode=360001; regionFullName=%E6%B1%9F%E8%A5%BF%E7%9C%81%E6%9C%AC%E7%BA%A7; regionRemark=1; TS0113089b=011e290be00e5f91339e33a99f9021db5ceb2c0951fc235af4b7bfe572cc9b9b628ec0aa448d008e5b77adfbb2d7ce04b71bf11285',
}

queryDictYX = {
    'currPage': 1,
    'pageSize': 40,
    'siteId': '93BB7F0CFA5A6362B1100531C50AE36B',
    'channel': '6d48e0f7-8dff-412f-9f89-83f01a2d296f',
    'noticeType': 59,
    'title': '',
    'purchaser': '',
    'purchaseNature': '',
    'operationStartTime': '2026-01-04 00:00:00',
    'operationEndTime': '2026-01-06 00:00:00',
    'cityOrArea': '',
    'verifyCode': '3117',
    '_t': '1767680856182'
}


{'_t': 1767686343612, 'agency': '', 'channel': 'c5bff13f-21ca-4dac-b158-cb40accd3035', 'cityOrArea': '',
 'currPage': 1, 'noticeType': '59',
 'openTenderCode': '',
 'operationEndTime': '2026-01-06 23:59:59',
 'operationStartTime': '2026-01-04 00:00:00',
 'pageSize': 10,
 'purchaseManner': '',
 'purchaseNature': '',
 'purchaser': '',
 'region': '',
 'regionCode': '', 'siteId': '93BB7F0CFA5A6362B1100531C50AE36B', 'title': '', 'verifyCode': '4076'}

response = requests.get(
    'https://zfcg.jxf.gov.cn/gpcms/rest/web/v2/info/selectInfoForIndex?',
    # cookies=cookies,
    params=queryDictYX,
    # headers=headers,
)

print(response.status_code)
print(response.text)