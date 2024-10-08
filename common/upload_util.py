import win32gui
import win32con
import time

def find_dialog(hwnd,dialog_handle):
    class_name = win32gui.GetClassName(hwnd)
    window_text = win32gui.GetWindowText(hwnd)
    parent = win32gui.GetParent(hwnd)
    if (
        class_name == '#32770' and window_text == '열기' and parent != 0 
    ):
        dialog_handle.append(hwnd)

def choice_handle(dialog_handle,parent):
    if len(dialog_handle)> 1 :
        for handle in dialog_handle :
            if parent in win32gui.GetWindowText(win32gui.GetParent(handle)) :
                return handle

    elif len(dialog_handle) == 1 :
        return dialog_handle[0]

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

def popupControl(file_path,parent=""):
    dialog_handle=[]
    win32gui.EnumWindows(find_dialog,dialog_handle)
    handle = choice_handle(dialog_handle,parent)
    
    combo_box_ex32 = win32gui.FindWindowEx(handle,0,"ComboBoxEx32",None)
    combo_box = win32gui.FindWindowEx(combo_box_ex32,0,"ComboBox",None)
    edit_handle = win32gui.FindWindowEx(combo_box,0,"Edit",None)

    win32gui.SendMessage(edit_handle,win32con.WM_SETTEXT,None,file_path)

    open_button = win32gui.FindWindowEx(handle,0,"Button","열기(&O)")

    win32gui.SendMessage(handle, win32con.WM_COMMAND, 1, open_button)
    
    time.sleep(2)

    close_error_popup(handle)