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

    # Firefox (автоматический профиль)
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


if __name__ == "__main__":
    user_profile = os.environ['USERPROFILE']

    clear_recycle()
    clear_temp()
    clear_Temp(user_profile)
    clear_updates()
    clear_prefetch()
    clear_browser(user_profile)
    clear_mStore(user_profile)
