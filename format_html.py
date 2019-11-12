from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time, pyperclip

formatter = webdriver.Chrome()
formatter.maximize_window()
formatter.get('https://htmlformatter.com/')
time.sleep(2)

def format_content(html_content, formatter):
    text_area = formatter.find_element_by_xpath('//*[@id="text-field"]/div[1]/div[1]')
    ActionChains(formatter).move_to_element(text_area).click(text_area).perform()
    pyperclip.copy(html_content)
    ActionChains(formatter).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    # text_area.send_keys(Keys.CONTROL, 'v')
    format_button = formatter.find_element_by_xpath('//*[@id="start-button"]/div[1]')
    format_button.click()
    time.sleep(3)
    text_area = formatter.find_element_by_xpath('//*[@id="text-field"]/div[1]/div[6]/div[1]')
    text_area.click()
    ActionChains(formatter).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
    ActionChains(formatter).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
    formatter.find_element_by_xpath('//*[@id="clear-button"]/div').click()
    return pyperclip.paste()
