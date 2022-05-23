'''
cron: 0 09,14 * * *
new Env('值得买');
'''
import requests
import json, random, datetime, time
#time.sleep(random.randint(0,30))#随机延迟5分钟内


#必填，不知道g_tk_openkey哪里来的，抓包的时候某一个url上会有g_tk_openkey，复制过来就好了
cookie = 'font_size=normal;session_id=C8qDd9W%2BDlkxaF%2BquJUZKhwSt8ieAt9QRdOnb9OSZh3kWBHOnJhzfQ%3D%3D.1587452720;partner_name=AppStore;device_s=C8qDd9WDlkxaFquJUZKhwSt8ieAt9QRdOnb9OSZh0sZw8ScyTu0EtBIlaCqaaTbE5IPtiFgiw%3D;partner_id=0;phone_sort=6p;device_id=C8qDd9W%2BDlkxaF%2BquJUZKhwSt8ieAt9QRdOnb9OSZh3kWBHOnJhzfQ%3D%3D;f=iphone;device_name=iPhone%207%20Plus;latitude=003c735e9281346cb6181011ca444ab6321fe8d5b7b8bf7d;is_new_user=0;v=9.7.0;device_smzdm_version_code=80;device_smzdm_version=9.7.0;longitude=7e97547ebadc28c456a4330af9157cf5b8e91d850004d615;device_system_version=13.4.1;login=1;client_id=C8qDd9W%2BDlkxaF%2BquJUZKhwSt8ieAt9QRdOnb9OSZh3kWBHOnJhzfQ%3D%3D.1586561895744;osversion=17E262;device_idfa=BKPqRF1XYSCICz9Fb2MU%2FVmeEVVwXmzTqux%2B%2FtSbZUTV7g%2FRCK1aMg%3D%3D;network=1;smzdm_id=7919517668;sess=YThhNjN8MTU5MDQ0OTk3NXw3OTE5NTE3NjY4fDg4Njc5NjAyMmJjM2RiOGM3ODg5OGM4NTk4NzE3NDI5;device_push=notifications_are_disabled;device_type=iPhone9%2C2;ab_test=c;coupon_h5=a;device_smzdm=iphone;'  # Cookie
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
   content = requests.get('https://sc.ftqq.com/' + key + '.send?text=什么值得买签到结果&desp=' + content).text
#def send(JSD):
    #JSD = requests.get('http://push.ijingniu.cn/send?key=' + jsdkey + '&head=什么值得买&body=' + JSD).text

def main_handler(event, context):
    msg = _sign_in_()
    print('msg: ', msg)
    if len(key) > 0:
       send_message(msg)
       #send(msg)
