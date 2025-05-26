import os
import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Путь для файла в директорию скрипта
download_dir = os.path.abspath(os.path.dirname(__file__))

# Задаем настройки для скачивания
options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}
options.add_experimental_option("prefs", prefs)

browser = webdriver.Chrome(options=options)
browser.maximize_window()

try:
    # 1. Перейти на https://sbis.ru/
    browser.get("https://sbis.ru/")
    wait = WebDriverWait(browser, 10)

    # 2. В Footer найти "Скачать СБИС"
    footer = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[href="/download"]')))

    # 3. Перейти по ней
    footer.click()
    sleep(2)

    # 4. На странице выбрать и скачать плагин для вашей ОС
    assert browser.current_url == 'https://saby.ru/download?tab=plugin&innerTab=default'
    plugin_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[href="https://update.saby.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe"]')))
    plugin_link.click()

    # 5. Убедиться, что файл скачался
    filename = None
    timeout = 30
    start_time = time.time()

    while time.time() - start_time < timeout:
        files = os.listdir(download_dir)
        for f in files:
            if f.startswith('sbisplugin-setup-web'):
                filename = f
                break
        if filename:
            break
        time.sleep(1)

    if not filename:
        raise Exception("Файл не был скачан за отведенное время.")

    # 6. Вывести размер файла в мегабайтах
    file_path = os.path.join(download_dir, filename)
    size_bytes = os.path.getsize(file_path)
    size_mb = size_bytes / (1024 * 1024)
    print(f"Размер скачанного файла: {size_mb:.2f} МБ")

finally:
    browser.quit()