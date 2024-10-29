from .. import *

def test():
    if os.path.isfile("./config.yml") == False :
        print("설정파일이 없습니다.")
        pyautogui.alert("설정파일이 없습니다.\n점검를 종료합니다.",title="설정파일 오류")
        return False

    with open('./config.yml','r',encoding='UTF8') as f:
        config = yaml.full_load(f)

    config_list=['status','user','checker','pm']

    for key in config_list :
        if key not in config :
            print("설정값("+key+")가 설정파일에 없습니다.")
            pyautogui.alert("설정값("+key+")가 설정파일에 없습니다.\n테스트를 종료합니다.",title="설정파일 오류")
            return False

    if config['status'] != 'report': 
        return True

    report_config_list=['coworker','reporter']

    for key in report_config_list :
        if key not in config :
            print("설정값("+key+")가 설정파일에 없습니다.")
            pyautogui.alert("설정값("+key+")가 설정파일에 없습니다.\n테스트를 종료합니다.",title="설정파일 오류")