import ctypes
import pyautogui
import psutil

def set_foreground_window(title):
    """Focus on the window with the specified title"""
    # Load the user32.dll system library
    user32 = ctypes.WinDLL('user32')

    # Find the window with the specified title
    hwnd = user32.FindWindowW(None, title)

    # Set the focus to the found window
    user32.SetForegroundWindow(hwnd)

def detectForgroundWindows():
    #Stolen from https://sjohannes.wordpress.com/2012/03/23/win32-python-getting-all-window-titles/
    EnumWindows = ctypes.windll.user32.EnumWindows
    EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
    GetWindowText = ctypes.windll.user32.GetWindowTextW
    GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
    IsWindowVisible = ctypes.windll.user32.IsWindowVisible
    titles = []
    def foreach_window(hwnd, lParam):
        if IsWindowVisible(hwnd):
            length = GetWindowTextLength(hwnd)
            buff = ctypes.create_unicode_buffer(length + 1)
            GetWindowText(hwnd, buff, length + 1)
            titles.append(buff.value)
        return True

    EnumWindows(EnumWindowsProc(foreach_window), 0)
     
    return titles

titles = detectForgroundWindows()

# Set focus to window
for title in titles:
    """Change the value based on the start of the window name of interest"""
    if title.startswith("888008900"):
        set_foreground_window(title)

        # Send the key combination "Alt + C" to the selected window program
        pyautogui.hotkey('alt','c')
