import os.path
import os, time
import stat
import shutil

def clear_dir(path):
    
    now = time.time()
    for i in os.listdir():
        if i != "desktop.ini":
            full_path = os.path.join(path, i)
            try:
                if now - os.path.getctime(full_path) > 600:
                    os.chmod(full_path, stat.S_IWRITE)
                    os.remove(full_path)
                    print(f"Удалён: {full_path}")
            except Exception as e:
                print(f"Ошибка при удалении {full_path}: {e}")
                
    for i in os.listdir():
        if i != "desktop.ini":
            full_path = os.path.join(path, i)
            try:
                if now - os.path.getctime(full_path) > 600:
                    os.chmod(full_path, stat.S_IWRITE)
                    shutil.rmtree(full_path)
                    print(f"Удалён: {full_path}")
            except Exception as e:
                print(f"Ошибка при удалении {full_path}: {e}")

def clear_recycle():
    recycle_path = r"C:\$Recycle.Bin\S-1-5-21-3980900106-2805927168-1824951230-1001"
    os.chdir(recycle_path)
    clear_dir(recycle_path)

def clear_temp():
    temp_path = r"C:\Windows\Temp"
    os.chdir(temp_path)
    clear_dir(temp_path)

def clear_Temp(user):
    Temp_path =  os.path.join(user, r"AppData\Local\Temp")
    os.chdir(Temp_path)
    clear_dir(Temp_path)

def clear_updates():
    updates_pats = r"C:\Windows\SoftwareDistribution\Download"
    os.chdir(updates_pats)
    clear_dir(updates_pats)

def clear_prefetch():
    prefetch_path = r"C:\Windows\Prefetch"
    os.chdir(prefetch_path)
    clear_dir(prefetch_path)
    
def clear_browser(user):
    chrome_path = os.path.join(user, r"AppData\Local\Google\Chrome\User Data\Default\Cache")
    os.chdir(chrome_path)
    clear_dir(chrome_path)
    
    firefox_path = os.path.join(user, r"AppData\Local\Mozilla\Firefox\Profiles\<профиль>\cache2")
    os.chdir(firefox_path)
    clear_dir(firefox_path)

def clear_mStore(user):
    print(user)
    mStore_path = os.path.join(user, r"AppData\Local\Packages")
    os.chdir(mStore_path)
    clear_dir(mStore_path)


user_profile = os.environ['USERPROFILE']

clear_recycle()
clear_temp()
clear_Temp(user_profile)
clear_updates()
clear_prefetch()
clear_browser(user_profile)
clear_mStore(user_profile)