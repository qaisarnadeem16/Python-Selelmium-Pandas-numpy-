import utils.net
import utils.clients
import utils.http_session
import utils.transport
import utils.session
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("https://www.google.com")

browser.quit()
