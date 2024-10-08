from .. import *

def find_dialog(hwnd,dialog_handle):
    class_name = win32gui.GetClassName(hwnd)
    window_text = win32gui.GetWindowText(hwnd)
    parent = win32gui.GetParent(hwnd)
    if (
        class_name == '#32770' and window_text == '열기' and parent != 0 
        and win32gui.GetClassName(parent) == 'Chrome_WidgetWin_1'
        and win32gui.GetWindowText(parent) == '기안 - 프로필 1 - Microsoft​ Edge'
    ):
        dialog_handle.append(hwnd)
    
def close_error_popup(dialog_handle):
    def find_popup(hwnd,popup_handle):
        class_name = win32gui.GetClassName(hwnd)
        window_text = win32gui.GetWindowText(hwnd)
        parent = win32gui.GetParent(hwnd)
        if (
            "열기" in window_text and class_name == '#32770' and parent == dialog_handle
        ):
            popup_handle.append(hwnd)
    err_handle = []
    win32gui.EnumWindows(find_popup,err_handle)
    if len(err_handle)>0:
        win32gui.PostMessage(err_handle[0],win32con.WM_CLOSE,0,0)
        win32gui.PostMessage(dialog_handle,win32con.WM_CLOSE,0,0)


def step(driver,wait) :
    selenium_util.click(driver,By.ID,'btnFileAttach')
    selenium_util.change_frame(driver,By.ID,'iFrameLayer')
    selenium_util.click(driver,By.ID,'btn_AttachAdd')
        
    wait.until(
        EC.presence_of_element_located(
            (By.ID,'file1')
        )
    )

    time.sleep(1)

    dialog_handle=[]
    win32gui.EnumWindows(find_dialog,dialog_handle)

    combo_box_ex32 = win32gui.FindWindowEx(dialog_handle[0],0,"ComboBoxEx32",None)
    combo_box = win32gui.FindWindowEx(combo_box_ex32,0,"ComboBox",None)
    edit_handle = win32gui.FindWindowEx(combo_box,0,"Edit",None)

    win32gui.SendMessage(
        edit_handle,win32con.WM_SETTEXT,None,
        'K:\\공유받은 폴더\\외주인력폴더\\일일점검\\\일일점검_'+datetime.today().strftime("%Y%m%d"+'.docx')
    )

    open_button = win32gui.FindWindowEx(dialog_handle[0],0,"Button","열기(&O)")

    win32gui.SendMessage(dialog_handle[0], win32con.WM_COMMAND, 1, open_button)
    
    time.sleep(2)

    close_error_popup(dialog_handle[0])

    selenium_util.click(driver,By.ID,'btn_AttachSaveSure')

    driver.switch_to.default_content()