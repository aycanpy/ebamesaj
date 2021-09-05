import pyautogui
import os
import time

tckimlik = "BURAYATCGELECEK"
sifre = "BURAYASİFREGELECEK"
mesaj = "BURAYAMESAJGELECEK"

os.system("start https://giris.eba.gov.tr/EBA_GIRIS/student.jsp")
time.sleep(5)
pyautogui.typewrite(tckimlik)
pyautogui.press("tab")
pyautogui.typewrite(sifre)
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(5)
pyautogui.press("tab")
pyautogui.typewrite(mesaj)
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.press("down")
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.press("enter")
