from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)

try:
    # 1 Авторизация
    browser.maximize_window()
    browser.get("https://fix-online.sbis.ru/")
    sleep(2)
    user_login, user_password = 'sil84', 'P@ssw0rd'
    login_input = browser.find_element(By.CSS_SELECTOR, '.controls-InputBase__field [type="text"]')
    login_input.send_keys(user_login, Keys.ENTER)
    assert login_input.get_attribute('value') == user_login
    sleep(1)
    password = browser.find_element(By.CSS_SELECTOR, '[type="password"]')
    password.send_keys(user_password, Keys.ENTER)
    sleep(5)
    #wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-name="contacts"]')))

    # 2. Переход в реестр "Контакты"
    browser.find_element(By.CSS_SELECTOR, '[data-name="contacts"]').click()
    sleep(1)
    browser.find_element(By.CSS_SELECTOR, '[data-qa="Контакты"]').click()
    sleep(2)
    #wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-name="sabyPage-addButton"]')))

    # 3. Отправка сообщения себе
    message_text = 'Текст сообщения'
    recipient = 'Кочетов'
    browser.find_element(By.CSS_SELECTOR, '[data-name="sabyPage-addButton"]').click()
    sleep(2)
    browser.find_element(By.CSS_SELECTOR, '.addressee-selector-popup__browser-search [type="text"]').send_keys(recipient, Keys.ENTER)
    sleep(2)
    browser.find_element(By.CSS_SELECTOR, '.addressee-selector-popup__view-item-wrapper [title="Кочетов"]').click()
    sleep(2)
    browser.find_element(By.CSS_SELECTOR, '.textEditor_slate_Field').send_keys(message_text)
    sleep(2)
    browser.find_element(By.CSS_SELECTOR, '[title="Отправить"]').click()
    sleep(2)

    # 4. Проверка, что сообщение появилось в реестре
    assert browser.find_elements(By.CSS_SELECTOR, f'[title={recipient}]'), "Элемент не найден"

    # 5. Удаление сообщения
    news_item = browser.find_element(By.CSS_SELECTOR,'.controls-ListView__itemContent')
    action = ActionChains(browser)
    action.move_to_element(news_item).perform()
    sleep(2)
    browser.find_element(By.CSS_SELECTOR, '.controls-itemActionsV').click()
    browser.find_element(By.CSS_SELECTOR, '[title="Перенести в удаленные"]').click()
    sleep(2)

    # 6. Проверка, что сообщение удалено
    element = browser.find_elements(By.CSS_SELECTOR, f'[title={recipient}]')
    assert len(element) == 0, "Сообщение не удалено"

finally:
    browser.quit()