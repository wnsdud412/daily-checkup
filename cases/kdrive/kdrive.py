from .. import *

def resource_path():
    try:
        base_path=sys._MEIPASS
    except Exception:
        base_path=os.path.abspath(".")
    return base_path
            
def test():
    pwd=resource_path()
    try:
        path = r"K:\공유받은 폴더\외주인력폴더\일일점검"
        item = f"일일점검_{datetime.today().strftime('%Y%m%d')}.docx"
        print(path+"\\"+item)
        word = win32client.gencache.EnsureDispatch("Word.application")
        word.Visible = True
        doc = word.Documents.Add()
        word.Selection.InsertBefore('일일점검_'+datetime.today().strftime("%Y%m%d")) 
        doc.SaveAs(fr"K:\공유받은 폴더\외주인력폴더\일일점검\일일점검_{datetime.today().strftime('%Y%m%d')}.docx")
        doc.Close()
        word.Quit()

        time.sleep(1)

        subprocess.Popen('explorer /select,"'+path+"\\"+item+'"')
        time.sleep(5)

        pyautogui.hotkey('shift','f10')

        time.sleep(3)

        rightClickThirdPoint = pyautogui.center(pyautogui.locateOnScreen(pwd+'/cases/kdrive/내부URL복사.png'))
        pyautogui.moveTo(rightClickThirdPoint.x,rightClickThirdPoint.y,0.3)

        time.sleep(0.5)
        
        pyautogui.click()
        
        time.sleep(1)

        clickPoint = pyautogui.center(pyautogui.locateOnScreen(pwd+'/cases/kdrive/복사url확인.PNG'))
        pyautogui.moveTo(clickPoint.x,clickPoint.y,0.3)

        time.sleep(0.5)

        pyautogui.click()
        pyautogui.hotkey('ctrl','w')

        return f"일일점검_{datetime.today().strftime('%Y%m%d')}" in pyperclip.paste()
    except Exception as ex:
        print("@@@@@@@@@@@문서중앙화 실패@@@@@@@@@@@")
        print(ex)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        return False

