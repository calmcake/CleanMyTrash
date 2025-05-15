import tkinter as tk
from tkinter import scrolledtext
import os
import time
import stat
import shutil

def clear_dir(path):
    now = time.time()

    for i in os.listdir(path):
        if i != "desktop.ini":
            full_path = os.path.join(path, i)
            try:
                if os.path.isfile(full_path) and now - os.path.getctime(full_path) > 600:
                    os.chmod(full_path, stat.S_IWRITE)
                    os.remove(full_path)
                    print(f"🗑️ Удалён файл: {full_path}")
            except Exception as e:
                print(f"❌ Ошибка при удалении файла {full_path}: {e}")

    for i in os.listdir(path):
        if i != "desktop.ini":
            full_path = os.path.join(path, i)
            try:
                if os.path.isdir(full_path) and now - os.path.getctime(full_path) > 600:
                    os.chmod(full_path, stat.S_IWRITE)
                    shutil.rmtree(full_path)
                    print(f"🧹 Удалена папка: {full_path}")
            except Exception as e:
                print(f"❌ Ошибка при удалении папки {full_path}: {e}")

def safe_clear(path):
    if os.path.exists(path):
        try:
            os.chdir(path)
            clear_dir(path)
        except Exception as e:
            print(f"❌ Не удалось очистить {path}: {e}")
    else:
        print(f"⚠️ Путь не найден: {path}")

def clear_recycle():
    recycle_path = r"C:\$Recycle.Bin"
    for sid in os.listdir(recycle_path):
        full_path = os.path.join(recycle_path, sid)
        safe_clear(full_path)

def clear_temp():
    safe_clear(r"C:\Windows\Temp")

def clear_Temp(user):
    Temp_path = os.path.join(user, "AppData", "Local", "Temp")
    safe_clear(Temp_path)

def clear_updates():
    updates_path = r"C:\Windows\SoftwareDistribution\Download"
    safe_clear(updates_path)

def clear_prefetch():
    prefetch_path = r"C:\Windows\Prefetch"
    safe_clear(prefetch_path)

def clear_browser(user):
    # Chrome
    chrome_path = os.path.join(user, "AppData", "Local", "Google", "Chrome", "User Data", "Default", "Cache")
    safe_clear(chrome_path)

    # Firefox
    profiles_root = os.path.join(user, "AppData", "Local", "Mozilla", "Firefox", "Profiles")
    if os.path.exists(profiles_root):
        for profile in os.listdir(profiles_root):
            cache_path = os.path.join(profiles_root, profile, "cache2")
            if os.path.exists(cache_path):
                safe_clear(cache_path)
                break

def clear_mStore(user):
    mstore_path = os.path.join(user, "AppData", "Local", "Packages")
    safe_clear(mstore_path)

def clear_all():
    clear_recycle()
    clear_temp()
    clear_Temp(user_profile)
    clear_updates()
    clear_prefetch()
    clear_browser(user_profile)
    clear_mStore(user_profile)

user_profile = os.environ['USERPROFILE']

def run_cleaning(func, name):
    output_text.insert(tk.END, f"\n▶ Выполняется: {name}...\n")
    output_text.see(tk.END)
    try:
        func()
        output_text.insert(tk.END, f"✅ Завершено: {name}\n")
    except Exception as e:
        output_text.insert(tk.END, f"❌ Ошибка при выполнении {name}: {e}\n")
    output_text.see(tk.END)

root = tk.Tk()
root.title("🧹 Чистильщик системы Windows")
root.geometry("600x600")
root.resizable(False, False)

title = tk.Label(root, text="🧼 Чистка системы", font=("Segoe UI", 18))
title.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

buttons = [
    ("🗑️ Очистить корзину", lambda: run_cleaning(clear_recycle, "Очистка корзины")),
    ("🧊 Очистить Windows\\Temp", lambda: run_cleaning(clear_temp, "Очистка Windows\\Temp")),
    ("🔥 Очистить User Temp", lambda: run_cleaning(lambda: clear_Temp(user_profile), "Очистка User Temp")),
    ("⬇️ Очистить обновления", lambda: run_cleaning(clear_updates, "Очистка обновлений")),
    ("📁 Очистить Prefetch", lambda: run_cleaning(clear_prefetch, "Очистка Prefetch")),
    ("🌐 Очистить кэш браузеров", lambda: run_cleaning(lambda: clear_browser(user_profile), "Очистка браузеров")),
    ("🏪 Очистить Microsoft Store", lambda: run_cleaning(lambda: clear_mStore(user_profile), "Очистка Microsoft Store")),
    ("🚀 Очистить всё", lambda: run_cleaning(clear_all, "Полная очистка")),
]

for text, command in buttons:
    b = tk.Button(button_frame, text=text, foreground = "#ffffff", background = "#0078d4", font=("Segoe UI", 10), width=40, command=command)
    b.pack(pady=5)

output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=15, font=("Consolas", 10))
output_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
output_text.insert(tk.END, "⏳ Ожидание действий...\n")

root.mainloop()
