from splinter import Browser
import threading

executable_path = {'executable_path': r'C:\Users\Johnny\Desktop\chromedriver_win32\chromedriver'}
USERNAME = 'chick_poacher_1000';
PASSWORD = 'johnny4388228'

# create a new instance of the chrome browser
browser = Browser('chrome', **executable_path, headless = False)

def login():
    url = 'https://www.neopets.com/login/'
    browser.visit(url)
    username = browser.find_by_id('loginUsername')

    username.fill(USERNAME)
    password = browser.find_by_id('loginPassword')

    password.fill(PASSWORD)
    logIn = browser.find_by_id('loginButton')
    logIn.click()
def startDice():
    url = 'https://www.neopets.com/games/dicearoo.phtml'
    browser.visit(url)
    diceARoo()
def diceARoo():
    submit = browser.find_by_css('[value="Lets Play! (Costs 5 NP)"]')
    if submit:
        submit.click()
    else:
        url = 'https://www.neopets.com/games/dicearoo.phtml'
        browser.visit(url)
    play = browser.find_by_css('[value="Play Dice-A-Roo"]')
    if play:
        play.click()
    rollDice()
    restart()
    diceARoo()
def rollDice():
    roll = browser.find_by_css('[value="Roll Again"]')
    if roll:
        roll.click()
        rollDice()
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
    waitForLogin(startDice)

start()
