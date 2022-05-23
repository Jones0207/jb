import requests, calendar
import json, random, datetime, time
#time.sleep(random.randint(0,30))#随机延迟5分钟内

ts = calendar.timegm(time.gmtime())

#必填，不知道g_tk_openkey哪里来的，抓包的时候某一个url上会有g_tk_openkey，复制过来就好了

corp_id = 'wwad849d24b9ae762e'
corp_secret = 'N_86pzzeYqUJSjtcZvlWL9A3i9O1NxgogGwviEIVoDg'
agent_id = '1000003'

AgentId = '1000003'
corpid = 'wwad849d24b9ae762e'
Secret = 'N_86pzzeYqUJSjtcZvlWL9A3i9O1NxgogGwviEIVoDg'
media_id='2-BNDSx4dv7-R82aqy_2jsT7N6s1T2Apd2Uo_7bKSKb5iCIruhUB6tkkV8_4istn3'

key = 'SCU98442T64d7b6ca5b64ef207ea65289bd0c5e895ec3d8c1254d9'  # server酱key，不填不通知

jsdkey = '59bb3e34d287476ca85749b1e953149f'#即时达推送KEY,不填不通知
header = {'Host': 'router-app-api.jdcloud.com',
'User-Agent': '%E4%BA%AC%E4%B8%9C%E4%BA%91%E6%97%A0%E7%BA%BF%E5%AE%9D/1005 CFNetwork/1240.0.4 Darwin/20.6.0',
'wskey': 'AAJiVP3_AEAq-LOkozRunC-19kWBLSdW3YrHFB1F69sSmxQisa6egh5doMoIGnhmOPFVgTSOSjhRb1oiojy7ce3P2a_IOAhj'}

headers = {
'Host': 'router-app-api.jdcloud.com',
'User-Agent': '%E4%BA%AC%E4%B8%9C%E4%BA%91%E6%97%A0%E7%BA%BF%E5%AE%9D/1005 CFNetwork/1240.0.4 Darwin/20.6.0',
'X-MLAAS-AT': 'wl=0',
'jdmt-rx-appKey': 'fe2c20725c261e49a80d707a6ab299e1',
'jdmt-rx-sign': '4e0422ad2b405dcee23a55fca8fc58c1',
'jdmt-rx-time': 'ts',
'wskey': 'AAJiVP3_AEAq-LOkozRunC-19kWBLSdW3YrHFB1F69sSmxQisa6egh5doMoIGnhmOPFVgTSOSjhRb1oiojy7ce3P2a_IOAhj'
}




def _sign_in_():
    url = 'https://router-app-api.jdcloud.com/v1/regions/cn-north-1/todayPointIncome?'

    urlz = 'https://router-app-api.jdcloud.com/v1/regions/cn-north-1/pinTotalAvailPoint'
    msg = '';
    mss = '';
    try:
        resp = requests.get(url=url, headers=headers)
        respzjf = requests.get(url=urlz, headers=header)
        
        re = json.loads(resp.text)
        dz = json.loads(resp.text)['result']
        print(dz)
        zjf = json.loads(respzjf.text)['result']
        print(zjf)
        if re['code'] == 200:
            msg = '今日总收入：'+str(dz['todayTotalPoint'])+'积分'+"<br/>"+'可兑换总积分：'+str(zjf['totalAvailPoint'])+'积分'
            
        else:
            msg = result['error_msg']



    except Exception:
        msg = 'cookie失效'
    return msg

#def send_message(content):
   #content = requests.get('https://sc.ftqq.com/' + key + '.send?text=京东云无线宝&desp=' + content).text

def push(title, content):
    if 'Token' in globals() and Token:
        try:
            pp=requests.post('http://www.pushplus.plus/send', json={"token": Token, "title": title,"content": content,"template": "html"},headers={'Content-Type': 'application/json'})
            if pp.json()['code'] == 200:print('pushplus已推送')
            else:exit()
        except:print('pushplus推送失败')
    if 'media_id' in globals() and media_id:
        response = requests.post('https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + corpid + '&corpsecret=' + Secret).json()['access_token'], json={'touser': '@all', 'msgtype': 'mpnews','agentid': AgentId, 'mpnews': {'articles': [{'thumb_media_id': media_id, 'title': title, 'content': content,'author': '初音ミク', 'content_source_url': 'http://syyt.syycgo.cn/?merchant_id=2&up_id=60274'}]},"enable_duplicate_check": 1,"duplicate_check_interval": 1800}).json()['errmsg']
        if response == 'ok':print('企业微信推送成功')
        else:print('企业微信推送失败')

def main_handler(event, context):
    msg = _sign_in_()
    print('msg: ', msg)
    push('京东无线宝'+msg, msg)
    #if len(key) > 0:
       #wechat_push_text(msg)
       #send_message(msg)
       #send(msg)

