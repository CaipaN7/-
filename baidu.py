import requests, js2py, json

content = js2py.EvalJs()

with open('sing.js', 'r', encoding='utf-8') as f:
    content.execute(f.read())

url = 'https://fanyi.baidu.com/v2transapi'
query = input('请输入待查询字符：')
sign = content.e(query)

data = {
    'from': 'en',
    'to': 'zh',
    'query': query,
    'simple_means_flag': '3',
    'sign': sign,
    'token': 'f9588cc5d9e36acf34058543eb278ac2'
}

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
    'referer': 'https://fanyi.baidu.com/?aldtype=16047',
    'cookie': 'BAIDUID=4CE621B4E3428D45096B717FC6ADA993:FG=1; BIDUPSID=4CE621B4E3428D45096B717FC6ADA993; PSTM=1541988307; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; locale=zh; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1561044155,1561044204,1561044375,1561044738; BDRCVFR[mkUqnUt8juD]=mk3SLVN4HKm; delPer=0; H_PS_PSSID=1460_21086_29135_29238_29099_29369_28835_29221; PSINO=1; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; yjs_js_security_passport=8de6720ba5daf9234eccb96e9a3c0eddf677110a_1561089960_js; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1561089869,1561089898,1561089956,1561090914; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1561090914'
}

res = requests.post(url=url, data=data, headers=headers)
print(json.loads(res.text)['trans_result']['data'][0]['dst'])

