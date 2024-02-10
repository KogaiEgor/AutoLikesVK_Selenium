import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os


def main():
    load_dotenv()
    driver = webdriver.Chrome()
    driver.get("https://vk.com/")
    try:
        authorize(driver)
        like_posts(driver, os.getenv('community'))
        time.sleep(3)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

def authorize(driver):
    wait = WebDriverWait(driver, 10)

    remember_me_check_box = driver.find_element(By.CLASS_NAME, "VkIdCheckbox__name")
    remember_me_check_box.click()

    number_field = driver.find_element(By.CLASS_NAME, "VkIdForm__input")
    number_field.send_keys(os.getenv("number"))
    number_field.send_keys(Keys.ENTER)

    password_field = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
    password_field.clear()
    password_field.send_keys(os.getenv("password"))
    password_field.send_keys(Keys.ENTER)
    time.sleep(2)

def like_posts(driver, url):
    driver.get(url)
    time.sleep(2)
    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    posts = driver.find_elements(By.XPATH, '//div[contains(@class, "_post post page_block all post--withPostBottomAction  post--with-likes deep_active Post--redesign")]')
    posts = posts + driver.find_elements(By.XPATH, '//div[contains(@class, "_post post page_block all own post--withPostBottomAction  post_with_ads_button post--with-likes deep_active Post--redesign")]')
    for post in posts:
        try:
            like = post.find_element(By.XPATH, './/span[contains(@class, "_like_button_icon")]')
            driver.execute_script("arguments[0].click();", like)
            time.sleep(1)
        except Exception as ex:
            print(ex)


if __name__ == '__main__':
    main()







# driver = webdriver.Chrome()
# driver.get("https://vk.com/")
#
# try:
#     remember_me_check_box = driver.find_element(By.CLASS_NAME, "VkIdCheckbox__name")
#     remember_me_check_box.click()
#     time.sleep(1)
#
#     number_field = driver.find_element(By.CLASS_NAME, "VkIdForm__input")
#     number_field.send_keys("996702180201")
#     number_field.send_keys(Keys.ENTER)
#     time.sleep(1)
#
#     password_field = driver.find_element(By.NAME, "password")
#     password_field.clear()
#     password_field.send_keys("doev357")
#     password_field.send_keys(Keys.ENTER)
#     time.sleep(2)
#     # messenger_button = driver.find_element(By.PARTIAL_LINK_TEXT, "Мессенджер")
#     # messenger_button.click()
#     #
#     # dialog = driver.find_element(By.PARTIAL_LINK_TEXT, "Артем Артемов")
#     # dialog.click()
#
#     # group_button = driver.find_element(By.PARTIAL_LINK_TEXT, "Сообщества")
#     # group_button.click()
#     # driver.implicitly_wait(2)
#
#     driver.get("https://vk.com/club224628037")
#
#     # voenmem = driver.find_element(By.PARTIAL_LINK_TEXT, "Test")
#     # voenmem.click()
#     # enter_button = driver.find_element(By.CLASS_NAME, "FlatButton__in")
#     # enter_button.click()
#     time.sleep(3)
# except Exception as ex:
#     print(ex)
# finally:
#     driver.close()
#     driver.quit()
