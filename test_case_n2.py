from selenium import webdriver
browser = webdriver.Chrome()

browser.get('https://www.amazon.com/')
searchbox = browser.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
searchbox.send_keys('iphone 12')

searchbutton = browser.find_element_by_xpath('//*[@id="nav-search-submit-button"]')
searchbutton.click()

browser.quit()