# windows_cleaner
Небольшая утилита для очистки системы

# 🧹 Windows Cleaner Script (Python)

Этот скрипт предназначен для быстрой очистки временных и кэшированных данных в Windows 10/11 с использованием Python.

## 🚀 Что делает скрипт

Удаляет:

- 🗑️ Файлы из корзины (`$Recycle.Bin`)
- 🧊 Файлы из системной папки Temp (`C:\Windows\Temp`)
- 🧊 Файлы из пользовательской папки Temp (`%USERPROFILE%\AppData\Local\Temp`)
- 📦 Кэш Центра обновлений Windows (`SoftwareDistribution\Download`)
- ⚡ Файлы предзагрузки (`C:\Windows\Prefetch`)
- 🌐 Кэш браузеров: Google Chrome и Mozilla Firefox
- 🏪 Кэш Microsoft Store (`AppData\Local\Packages`)

⚠️ Удаляются файлы и папки, **старше 10 минут**, кроме `desktop.ini`.

---

## 📦 Требования

- Python 3.6+
- Запуск **от имени администратора** (иначе часть директорий будет недоступна)

---
