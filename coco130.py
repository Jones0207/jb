'''
cron: 0 05 10 * * *
new Env('COCO130');
'''
import requests
import json, random, datetime, time
#time.sleep(random.randint(0,30))#随机延迟5分钟内

key = 'SCU98442T64d7b6ca5b64ef207ea65289bd0c5e895ec3d8c1254d9'  # server酱key，不填不通知

jsdkey = '59bb3e34d287476ca85749b1e953149f'#即时达推送KEY,不填不通知

headers = {'Content-Type': 'application/json;charset=utf-8','Cookie': 'UM_distinctid=17f6ca5031258c-08f938a5d86696-61276d23-100200-17f6ca503137c8; CNZZDATA1280296261=1417342069-1646792990-%7C1646792990;',
'Host': 'pncct.coco.360neighbour.com',
'Origin': 'https://pncct.coco.360neighbour.com',
'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.1 Mobile/15E148 Safari/604.1',
'X-Requested-With': 'XMLHttpRequest',
'token': '31767f5590abad8ae03753df7a6a92fc'
}

params = '{"token":"31767f5590abad8ae03753df7a6a92fc"}'#打卡提交数据


def _sign_in_():
    url = 'https://pncct.coco.360neighbour.com/user/member/sign'
    msg = '';
    try:
        resp = requests.post(url=url, data=params, headers=headers)
        print(resp.text)
        result = json.loads(resp.text)
       
        if result['error_code'] == 0:
            msg = '签到成功'
        else:
            msg = result['error_msg']
    except Exception:
        msg = 'cookie失效'
    return msg


#def send_message(content):
    #content = requests.get('https://sc.ftqq.com/' + key + '.send?text=什么值得买签到结果&desp=' + content).text
def send(content):
    content = requests.get('http://push.ijingniu.cn/send?key=' + jsdkey + '&head=COCO签到&body=' + content).text

def main_handler(event, context):
    msg = _sign_in_()
    print('msg: ', msg)
    if len(key) > 0:
        #send_message(msg)
        send(msg)
