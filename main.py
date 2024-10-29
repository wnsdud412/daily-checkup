from cases.config import config
from cases.kdrive import kdrive
from cases.cowork import cowork
from cases.mail import mail
from cases.approve import approve
from cases.etc import etc
from cases.report import report
import win32api
import win32con
import pyautogui
import yaml
import time
import sys

print('start')

if config.test() == False :
    sys.exit()

with open('./config.yml','r',encoding='UTF8') as f:
    config = yaml.full_load(f)

flag = True
if config['status'] != 'report': 
    flag = False

result = {}

result['문서중앙화'] = kdrive.test()
if config['status'] == 'checkup' or config['status'] == 'report':
    result['협업'] = cowork.test()
    result['메일'] = mail.test() 
    result['전자결재'] = approve.test()

result.update(etc.test())

for key,val in result.items() :
    if val == False:
        print(f"{key} 오류 발생!")
        flag = False

pyautogui.alert(str(result),title="점검결과")

print(result)

if flag and win32api.MessageBox(0,"자동보고를 원하시면 확인을 눌러주세요","자동보고",1) == 1: 
    report.page()
    report.message()

print('finish')


