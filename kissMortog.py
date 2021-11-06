from splinter import Browser
import threading
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
'''chrome_options.add_argument('--headless')'''
chrome_options.add_argument('--log-level=3')
executable_path = {'executable_path': r'C:\Users\Johnny\Desktop\chromedriver_win32\chromedriver'}
USERNAME = 'chick_poacher_1000';
PASSWORD = 'johnny4388228'

# create a new instance of the chrome browser
browser = Browser('chrome', **executable_path, headless=False, options=chrome_options)

def login():
    url = 'https://www.neopets.com/login/'
    browser.visit(url)
    username = browser.find_by_id('loginUsername')

    username.fill(USERNAME)
    password = browser.find_by_id('loginPassword')

    password.fill(PASSWORD)
    logIn = browser.find_by_id('loginButton')
    logIn.click()
def startMortog():
    url = 'https://www.neopets.com/medieval/kissthemortog.phtml'
    browser.visit(url)
    while True:

        kissMortog()
        resolveMortog()

def kissMortog():
    mortogs = browser.find_by_css('[src="//images.neopets.com/items/pet_mortog.gif"]')
    mortogs[0].click()
def resolveMortog():
    tryAgain = browser.find_by_css('[value="Try again..."]')
    if tryAgain:
        tryAgain.click()
    else:
        winnings = browser.find_by_css('[type="submit"]')[2].value
        winnings = winnings.split(' - ');
        np = winnings[1].split(' ')[0]
        np = ''.join(np.split(','))
        np = int(np)
        print('np', np)
        if np >= 5900:
            browser.find_by_css('[type="submit"]')[2].click()
        else:
            browser.find_by_css('[value="Continue"]').click()
def restart():
    restart = browser.find_by_css('[value="Press Me"]')
    if restart:
        restart.click()
def waitForLogin(callback):
    bell = browser.find_by_css('[class="nav-bell-icon__2020"]')
    if bell:
        callback()
    else:
        timer = threading.Timer(1.0, waitForLogin(callback))
        timer.start()


def start():
    login()
    waitForLogin(startMortog)

start()
