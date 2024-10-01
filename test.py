from selenium import webdriver
import geckodriver_autoinstaller


geckodriver_autoinstaller.install()  # Check if the current version of geckodriver exists
                                     # and if it doesn't exist, download it automatically,
                                     # then add geckodriver to path

driver = webdriver.Firefox()
driver.get("http://www.gutenberg.org")
books = driver.find_elements("tag name","p")
for i in range(0,len(books)):
    print(books[i].text)