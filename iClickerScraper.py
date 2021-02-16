from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from random import randint, randrange
import time

def scrape(email, password, scrolls):

    options = Options()
    #options.headless = True # Comment out for development
    options.add_argument("--disable-gpu")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-notifications")
    options.page_load_strategy = 'eager'
    driver = webdriver.Chrome(options=options)

    time.sleep(3)
    site = "https://www.facebook.com"
    driver.get(site)
    time.sleep(3) # Let site load

    print("Login procedure.")
    driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="pass"]').send_keys(password)
    time.sleep(1)
    driver.find_element_by_name('login').click()
    time.sleep(10)
    # By this point, you should be logged in. Otherwise, there was an issue with the website or your credentials.

    # Go into Free & For Sale Facebook group and View Posts
    driver.get("https://www.facebook.com/groups/687364258007925/search?q=iclicker&filters=eyJmaWx0ZXJfYnNnX3NlYXJjaF9sYXlvdXQ6MCI6IntcIm5hbWVcIjpcImZpbHRlcl9ic2dfc2VhcmNoX2xpc3RfbGF5b3V0XCIsXCJhcmdzXCI6XCJcIn0ifQ%3D%3D")
    time.sleep(randint(5, 7))

    for i in range(scrolls):
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(randint(5, 7))
        except:
            time.sleep(randint(5, 7))
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    page_source = driver.execute_script("return document.body.innerHTML")


    file = open("source_data.txt", "a+", encoding="utf-8")
    file.write(page_source)
    file.close()

    driver.close()

# email = input("Email: ")
# password = input("Password: ")
# scrolls = int(input("Scrolls: "))
# # I think scrolling 20 times is more than sufficient.
#
# iClickerScraper.scrape(email, password, scrolls)