from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

try:
    # 1 Переход на сайт
    browser.maximize_window()
    browser.get("https://saby.ru/")
    sleep(2)

    # 2. Переход в раздел "Контакты"
    contacts = browser.find_element(By.CSS_SELECTOR, '[href="/contacts"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);",contacts)
    sleep(1)
    contacts.click()
    sleep(2)
    browser.find_element(By.CSS_SELECTOR, '[class="sbisru-Contacts__logo-tensor mb-12"]').click()
    sleep(2)

    # 2. Переход на "https://tensor.ru/"
    handles = browser.window_handles
    browser.switch_to.window(handles[1])

    # 3. Проверка, что есть блок новости "Сила в людях"
    news = browser.find_element(By.XPATH, '//p[text()="Сила в людях"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);",news)
    sleep(2)
    assert browser.find_element(By.XPATH, '//p[text()="Сила в людях"]')

    #4. Переход в "Подробнее" и проверка, что открывается https://tensor.ru/about
    browser.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content [href="/about"]').click()
    sleep(2)
    assert browser.current_url == "https://tensor.ru/about", "Открыт не https://tensor.ru/about"

finally:
    browser.quit()