import requests
import json, random, datetime, time
#time.sleep(random.randint(0,30))#随机延迟5分钟内


#必填，不知道g_tk_openkey哪里来的，抓包的时候某一个url上会有g_tk_openkey，复制过来就好了
cookie = 'smzdm_id=9385699623; device_id=30859538521619139627690812297f5daf32506db612e512d13b553253; sess=NDYyZmF8MTYyNDMyMzYyN3w5Mzg1Njk5NjIzfDMzNDkzMjlmOTEyNDhhZmZkNGVkNjRlNDU5NGM0ZTZifDMwODU5NTM4NTIxNjE5MTM5NjI3NjkwODEyMjk3ZjVkYWYzMjUwNmRiNjEyZTUxMmQxM2I1NTMyNTN8d2Vi; user=user%3A9385699623%7C9385699623; FROM_BD=1; sajssdk_2015_cross_new_user=1; __jsluid_s=5a587b6669ab51dd4b315dcb2f4b8f8e; __ckguid=9Wl4se7YlN6Nw9uycQnknI3'  # Cookie
key = 'SCU98442T64d7b6ca5b64ef207ea65289bd0c5e895ec3d8c1254d9'  # server酱key，不填不通知
jsdkey = '59bb3e34d287476ca85749b1e953149f'#即时达推送KEY,不填不通知

headers = {'Cookie': cookie,'Referer': 'https://www.smzdm.com/?utm_source=baidu&utm_medium=cpc&utm_campaign=002','User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36',
}




def _sign_in_():
    url = 'https://zhiyou.smzdm.com/user/checkin/jsonp_checkin'
    msg = '';
    try:
        resp = requests.get(url=url, headers=headers)
        print(resp.text)
        result = json.loads(resp.text)
       
        if result['error_code'] == 0:
        
            msg = '签到成功' + '\n\n' + '累计：' + str(result['data']['checkin_num']) + '天,' + '    '+'经验：' + str(result['data']['exp'])+ '  ' + '金币：' + str(result['data']['gold'])+ '   ' + '积分：' + str(result['data']['point'])
        else:
            msg = result['error_msg']
    except Exception:
        msg = 'cookie失效'
    return msg


def send_message(content):
   content = requests.get('https://sc.ftqq.com/' + key + '.send?text=什么值得买2号&desp=' + content).text
#def send(JSD):
    #JSD = requests.get('http://push.ijingniu.cn/send?key=' + jsdkey + '&head=什么值得买&body=' + JSD).text

def main_handler(event, context):
    msg = _sign_in_()
    print('msg: ', msg)
    if len(key) > 0:
       send_message(msg)
       #send(msg)
