#!/usr/bin/python
# -*- coding: utf8
import requests
import json
import os

zdUrl = 'http://api.turinglabs.net/api/v1/jd/bean/create/'
ncUrl = 'http://api.turinglabs.net/api/v1/jd/farm/create/'
mcUrl = 'http://api.turinglabs.net/api/v1/jd/pet/create/'
ddurl = "http://api.turinglabs.net/api/v1/jd/ddfactory/create/"
jxurl = "http://api.turinglabs.net/api/v1/jd/jxfactory/create/"
jdzzurl = "https://code.chiang.fun/api/v1/jd/jdzz/create/"

token1 = os.environ['PLUS_KEY']
token2 = os.environ['PLUS_KEY2']
tokens = [token1, token2, token1]

Defalt_ncShareCode = ['f362373e1dee41e0857a6cb4834af992',
                      '18a804a19d58474e98d5a5490e8f91a3',
                      'b261337d06e74b1098f616141a0547dd']
Defalt_mcShareCode = ['MTAxODc2NTEzNTAwMDAwMDAyMDE5MzUzNQ==',
                      'MTEzMzI0OTE0NTAwMDAwMDA0MTc4OTM3OQ==',
                      'MTE1NDUwMTI0MDAwMDAwMDQyNTAwMTA5']
Defalt_zdShareCode = ['mlrdw3aw26j3xfouimthxb26gr53v4mg7y4seji',
                      'iq4paoebhftxidofiue6rcrqbxvakewvs3qidqi',
                      'sbtpzthpn5duja6ati5zl4psmorhk3o73cuza5y']
Defalt_ddShareCode = ['P04z54XCjVWnYaS5m9cZ2Wq2C5Mw1YsO47pBdM',
                      'P04z54XCjVWnYaS5nJcdiixtC8o6eKmuBkMtQ',
                      'P04z54XCjVWnYaS5nJccwqkqAE914H_MlaA']
Defalt_jxShareCode = ['rg5PyZyZiAvO9g7SHMJphQ==',
                      'SDXbeYAJc51IGPh1AwkP8A==',
                      'T7AgoLvxsm5bJX_1zJXoWQ==']

Defalt_jdzzShareCode = ['S5KkcRUwcp1KBKEunl6ZbIA']

def AddhelpCode(Url, Defalt_ShareCode):
    for i, code in enumerate(Defalt_ShareCode):
        try:
            AddcodeRes = hongliyu(Url + code + '/')
            print(AddcodeRes)

            if AddcodeRes['code'] == 200:
                notify(tokens[i], "互助码添加成功✅", "互助码:" + code + "添加成功✅")
            elif AddcodeRes['code'] == 400:
                notify(tokens[i], "互助码已存在", "互助码:" + code + "已存在")
            else:
                notify(tokens[i], "互助码添加异常", "互助码:" + code + "添加异常")
        except Exception as e:
            pass


def hongliyu(url):
    try:
        return json.loads(requests.get(url).text)
    except Exception as e:
        print('''初始化函数:''', str(e))


def notify(token, title, content):
    try:
        print(content)
        #title = '京东互助上车执行情况'
        url = 'https://sc.ftqq.com/' + token + '.send?text=' + title + '&desp=' + content
        requests.get(url)
    except Exception as e:
        print('''发送通知:''', str(e))


AddhelpCode(mcUrl, Defalt_mcShareCode)
AddhelpCode(ncUrl, Defalt_ncShareCode)
AddhelpCode(zdUrl, Defalt_zdShareCode)
AddhelpCode(ddurl, Defalt_ddShareCode)
AddhelpCode(jxurl, Defalt_jxShareCode)
AddhelpCode(jdzzurl, Defalt_jdzzShareCode)
