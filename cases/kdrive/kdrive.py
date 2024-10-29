from .. import *
            
def test():
    try:
        pwd=system_util.resource_path()

        moniters = win32api.EnumDisplayMonitors()
        originPoint = [0,0]
        for monitor in moniters:
            rect = monitor[2]
            for i in [0,1] :
                if rect[i] < originPoint[i] :
                    originPoint[i] = rect[i]

        path = r"K:\공유받은 폴더\외주인력폴더\일일점검"
        item = f"일일점검_{datetime.today().strftime('%Y%m%d')}.docx"
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

        urlCopyPoint = pyautogui.center(pyautogui.locateOnScreen(pwd+'/cases/kdrive/내부URL복사.png'))
        pyautogui.moveTo(urlCopyPoint.x+originPoint[0],urlCopyPoint.y+originPoint[1],0.3)

        time.sleep(0.5)
        
        pyautogui.click()
        
        time.sleep(1)

        clickPoint = pyautogui.center(pyautogui.locateOnScreen(pwd+'/cases/kdrive/복사url확인.PNG'))
        pyautogui.moveTo(clickPoint.x+originPoint[0],clickPoint.y+originPoint[1],0.3)

        time.sleep(0.5)

        pyautogui.click()
        pyautogui.hotkey('ctrl','w')

        return f"일일점검_{datetime.today().strftime('%Y%m%d')}" in pyperclip.paste()
    except Exception as ex:
        print("@@@@@@@@@@@문서중앙화 실패@@@@@@@@@@@")
        print(ex)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        return False

