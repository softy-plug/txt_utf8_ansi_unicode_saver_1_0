import os

# Установка необходимых библиотек
os.system("pip install pyautogui")
os.system("pip install keyboard")

input("Для запуска программы нажмите Enter")

import subprocess
import time
import pyautogui
import keyboard

# Получаем текущую директорию
current_folder = os.getcwd()

# Проходим по всем файлам в текущей директории
for filename in os.listdir(current_folder):
    if filename.endswith('.txt'):
        file_path = os.path.join(current_folder, filename)
        
        # Открываем файл в Блокноте
        subprocess.Popen(['notepad.exe', file_path])
        time.sleep(3)  # Ждем, пока Блокнот откроется

        # Сохраняем файл с кодировкой ANSI
        keyboard.press_and_release('ctrl+shift+s') # Выбираем "Сохранить как"
#        pyautogui.hotkey('ctrl', 'shift', 's')  # Выбираем "Сохранить как"
        time.sleep(3)  # Ждем, пока откроется диалог
        pyautogui.press('tab', presses=3)  # Переходим к полю кодировки
        pyautogui.press('down')  # Открываем список кодировок
        pyautogui.press('up', presses=3)  # Выбираем ANSI (может потребоваться несколько нажатий)
        pyautogui.press('enter')  # Подтверждаем выбор кодировки
        time.sleep(3)  # Ждем, пока диалог обновится
        pyautogui.press('tab')  # Переходим к полю сохранения файла
        pyautogui.press('enter')  # Открываем меню сохранения файла
        pyautogui.press('left')  # Заменяем файл
        pyautogui.press('enter')  # Сохраняем файл
        pyautogui.press('enter')  # Подтверждаем сохранение файла

        # Закрываем Блокнот
        keyboard.press_and_release('alt+f4') # Закрываем Блокнот
#        pyautogui.hotkey('alt', 'f4')
        time.sleep(2)  # Ждем, чтобы Блокнот закрылся

print("Все файлы .txt сохранены с кодировкой ANSI.")

# Закрыть браузер
input("Нажмите Enter для закрытия окна")

# softy_plug