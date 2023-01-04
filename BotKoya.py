from selenium import webdriver #DRIVER
from selenium.webdriver.common.keys import Keys #KEY : ENTER
import time #WAIT

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  #ATTENTE EXPLICITE
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver import ActionChains #MOUSE OVER
#VARIABLES TPS

tpsFish = 0
tpsDaily = 0
tpsBoat = 0
tpsDdm = 0

def Lancement():

    driver = webdriver.Chrome("chromedriver.exe")

    driver.get("https://discord.com/login")

    driver.find_element_by_name("email").send_keys("email")
    driver.find_element_by_name("password").send_keys("password")
    time.sleep(1)
    driver.find_element_by_name("password").send_keys(Keys.RETURN)

    try:
        element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, "private-channels-1"))
        )
    finally:
        driver.find_element_by_class_name('searchBarComponent-32dTOx').click()
        time.sleep(0.2)
        driver.find_element_by_class_name("input-2VB9rf").send_keys("Koya#1050")
        driver.find_element_by_class_name("input-2VB9rf").send_keys(Keys.RETURN)


    time.sleep(1)
    textBox = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/form/div/div/div/div[3]/div[2]')
    return textBox,driver


def Fish(tb):
    global tpsFish
    tb.send_keys("^^fish")
    time.sleep(1)
    tb.send_keys(Keys.RETURN)
    tpsFish = int(time.time())

def Daily(tb):
    global tpsDaily
    tb.send_keys("^^daily")
    time.sleep(1)
    tb.send_keys(Keys.RETURN)
    tpsDaily = int(time.time())

def Boat(tb,driver):
    global tpsBoat
    tb.send_keys("^^boat a")
    tb.send_keys(Keys.RETURN)
    time.sleep(6)
    tb.send_keys("^^boat exp 2")
    tb.send_keys(Keys.RETURN)
    time.sleep(1)


    #AJOUT REACTION

    message = driver.find_elements_by_class_name('contents-2mQqc9')
    message=message[-1] #dernier message du chat
    time.sleep(1)

    actions = ActionChains(driver)
    actions.move_to_element(message).perform()#.move_to_element(react).click().perform()
    reaction=driver.find_elements_by_class_name("button-1ZiXG9")
    reaction = reaction[-3] #bouton emote
    reaction.click()
    emote=driver.find_element_by_xpath('.//*[@id="emoji-picker-tab-panel"]/div[1]/div[1]/div[1]/div/input')
    emote.send_keys("white_check_mark")
    time.sleep(1)
    emote.send_keys(Keys.RETURN)


    tpsBoat = int(time.time())

def Ddm(tb):
    global tpsDdm
    tb.send_keys("^^ddm")
    time.sleep(1)
    tb.send_keys(Keys.RETURN)
    tpsDdm = int(time.time())

def Boucle():

    tpsActuel = int(time.time())

    if tpsActuel >= (tpsFish+3600):
        x = Lancement()
        tb = x[0]
        driv= x[1]
        time.sleep(2)
        Fish(tb)
        time.sleep(2)
        driv.quit()


    if tpsActuel >= (tpsDaily+86400):
        x = Lancement()
        tb = x[0]
        driv= x[1]
        time.sleep(2)
        Daily(tb)
        time.sleep(2)
        driv.quit()


    if tpsActuel >= (tpsBoat+3600):
        x = Lancement()
        tb = x[0]
        driv= x[1]
        time.sleep(2)
        Boat(tb,driv)
        time.sleep(2)
        driv.quit()

    """
    if tpsActuel >= (tpsDdm+900):
        x = Lancement()
        tb = x[0]
        driv= x[1]
        time.sleep(2)
        Ddm(tb)
        time.sleep(2)
        driv.quit()
    """
    time.sleep(30)
    Boucle()

Boucle()

