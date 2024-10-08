from cases.kdrive import kdrive
from cases.cowork import cowork
from cases.mail import mail
from cases.approve import approve
from cases.etc import etc
from cases.report import report
import win32api
import win32con
import yaml

print('start')

with open('./config.yml','r',encoding='UTF8') as f:
    config = yaml.full_load(f)

flag = True
if config != 'report': 
    flag = False

result = {}

result['문서중앙화'] = kdrive.test()
if config == 'checkup' or config == 'report':
    result['협업'] = cowork.test()
    result['메일'] = mail.test() 
    result['전자결재'] = approve.test()
result.update(etc.test())

for key,val in result.items() :
    if val == False:
        print(f"{key} 오류 발생!")
        flag = False

win32api.MessageBox(0,str(result),"점검결과",win32con.MB_OK)

print(result)

if flag:
    win32api.MessageBox(0,"자동보고를 시작합니다","점검결과",win32con.MB_OK)
    report.page()
    report.message()

print('finish')


