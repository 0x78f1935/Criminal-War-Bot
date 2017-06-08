from __future__ import print_function
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException  
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from PIL import Image
from PIL import ImageGrab
import time
import re
import getpass
from threading import Thread
import os
import sys

from desktopmagic.screengrab_win32 import (
getDisplayRects, saveScreenToBmp, saveRectToBmp, getScreenAsImage,
getRectAsImage, getDisplaysAsImages)

global website
website = 'http://www.criminalwar.nl/'

def inloggen():

    username = input("Username: ")
    wachtwoord = getpass.getpass()

    global browser
    browser = webdriver.Firefox(executable_path=r'Geckodriver\geckodriver.exe')

    browser.get(website)

    browser.find_element_by_xpath('//*[@id=\"formLogin\"]/span[1]/input').send_keys(username)
    browser.find_element_by_xpath('//*[@id=\"formLogin\"]/span[2]/input').send_keys(wachtwoord)
    browser.find_element_by_xpath('//*[@id=\"formLogin\"]/input').click()

    try:
        daily_login_reward = browser.find_element_by_css_selector('.qtip-button')
        print("*** You have a daily reward! ***")
        daily_login_reward.click()
    except NoSuchElementException:
        pass

def check_exists_by_xpath(xpath):
    try:
        browser.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def check_exists_by_css_selector(css):
    try:
        browser.find_element_by_css_selector(css)
    except NoSuchElementException:
        return False
    return True

def get_numbers(string):
    #strips numbers down
    global numbers
    numbers = re.compile('\d+(?:\.\d+)?')
    string = numbers.findall(string)
    return string

def get_captcha_v1():
    print("--- Looking for Captcha ---")

    try:
        print("--- Looking for popups... ---")

        browser.find_element_by_css_selector('.qtip-button').click() or browser.find_element_by_css_selector('.submitBig').click()
        print("!!! Pop up detected !!!")
        pass
    except NoSuchElementException:
        print("+++ No popup detected +++")

        pass

    captcha_xpath_code_text = check_exists_by_xpath('//*[@id=\"page\"]/form/table/tbody/tr[7]/td[2]/table/tbody/tr/td[1]/a')
    captcha_xpath_image = check_exists_by_xpath('//*[@id=\"page\"]/form/table/tbody/tr[7]/td[2]/table/tbody/tr/td[2]/img')
    captcha_empty_space = check_exists_by_xpath('//*[@id=\"page\"]/form/table/tbody/tr[7]/td[2]/table/tbody/tr/td[3]')
    captcha_xpath_input_box = check_exists_by_xpath('//*[@id=\"page\"]/form/table/tbody/tr[7]/td[2]/table/tbody/tr/td[3]/input')
    captcha_xpath_image_questionmark = check_exists_by_xpath('//*[@id=\"page\"]/form/table/tbody/tr[7]/td[2]/table/tbody/tr/td[3]/strong/a')
    captcha_css_selector_code_text = check_exists_by_css_selector('#page > form:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > a:nth-child(1)')
    captcha_css_selector_image = check_exists_by_css_selector('#page > form:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > img:nth-child(1)')
    captcha_css_selector_input = check_exists_by_css_selector('.input2')
    captcha_css_selector = check_exists_by_css_selector('#page > form:nth-child(2) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(7) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > a:nth-child(1)')

    #print("\n \n !!!!!!DEBUG!!!!!! \n \n  Code text : %s \n xpath image : %s \n  xpath_empty_space : %s \n xpath input box: %s \n xpath ? : %s \n css code text : %s \n css image : %s \n css input : %s \n captcha css selector : %s \n \n" %(captcha_xpath_code_text, captcha_xpath_image, captcha_empty_space, captcha_xpath_input_box, captcha_xpath_image_questionmark, captcha_css_selector_code_text, captcha_css_selector_image, captcha_css_selector_input, captcha_css_selector))

    if captcha_xpath_code_text or captcha_xpath_image or captcha_empty_space or captcha_xpath_input_box or captcha_xpath_image_questionmark or captcha_css_selector_code_text or captcha_css_selector_image or captcha_css_selector_input == True:
        
        print("!!! Captcha found !!!")
        box = 2065, 315, 2179, 358

        full_screen_capture = getScreenAsImage()
        #Screen_capture = getRectAsImage((box))
        full_screen_capture.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +'.png', format='png')

        time_need_to_stay_idle = 300
        print("!!! The bot will restart after %s seconds !!!" % (time_need_to_stay_idle))
        time.sleep(time_need_to_stay_idle)
        restart()
        
    else:
        print("+++ Captcha not found +++")
        return

def get_captcha_v1_shooting_range():
    print("--- Looking for Captcha ---")

    try:
        print("--- Looking for popups... ---")

        browser.find_element_by_css_selector('.qtip-button').click() or browser.find_element_by_css_selector('.submitBig').click()
        print("!!! Pop up detected !!!")
        pass
    except NoSuchElementException:
        print("+++ No popup detected +++")

        pass

    captcha_xpath_code_text = check_exists_by_xpath('//*[@id=\"page\"]/form/table/tbody/tr[7]/td[2]/table/tbody/tr/td[1]/a')
    captcha_xpath_image = check_exists_by_xpath('//*[@id=\"page\"]/form/table/tbody/tr[7]/td[2]/table/tbody/tr/td[2]/img')
    captcha_empty_space = check_exists_by_xpath('//*[@id=\"page\"]/form/table/tbody/tr[7]/td[2]/table/tbody/tr/td[3]')
    captcha_xpath_input_box = check_exists_by_xpath('//*[@id=\"page\"]/form/table/tbody/tr[7]/td[2]/table/tbody/tr/td[3]/input')
    captcha_xpath_image_questionmark = check_exists_by_xpath('//*[@id=\"page\"]/form/table/tbody/tr[7]/td[2]/table/tbody/tr/td[3]/strong/a')
    captcha_css_selector_code_text = check_exists_by_css_selector('#page > form:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > a:nth-child(1)')
    captcha_css_selector_image = check_exists_by_css_selector('#page > form:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > img:nth-child(1)')
    #captcha_css_selector_input = check_exists_by_css_selector('.input2')
    captcha_css_selector = check_exists_by_css_selector('#page > form:nth-child(2) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(7) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > a:nth-child(1)')

    print("\n \n !!!!!!DEBUG!!!!!! \n \n  Code text : %s \n xpath image : %s \n  xpath_empty_space : %s \n xpath input box: %s \n xpath ? : %s \n css code text : %s \n css image : %s \n css input : %s \n captcha css selector : %s \n \n" %(captcha_xpath_code_text, captcha_xpath_image, captcha_empty_space, captcha_xpath_input_box, captcha_xpath_image_questionmark, captcha_css_selector_code_text, captcha_css_selector_image, captcha_css_selector_input, captcha_css_selector))

    if captcha_xpath_code_text or captcha_xpath_image or captcha_empty_space or captcha_xpath_input_box or captcha_xpath_image_questionmark or captcha_css_selector_code_text or captcha_css_selector_image or captcha_css_selector_input == True:
        
        print("!!! Captcha found !!!")
        box = 2065, 315, 2179, 358

        full_screen_capture = getScreenAsImage()
        #Screen_capture = getRectAsImage((box))
        full_screen_capture.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +'.png', format='png')

        time_need_to_stay_idle = 300
        print("!!! The bot will restart after %s seconds !!!" % (time_need_to_stay_idle))
        time.sleep(time_need_to_stay_idle)
        restart()
        
    else:
        print("+++ Captcha not found +++")
        return


def get_captcha_v1_hostage():
    print("--- Looking for Captcha ---")

    try:
        print("--- Looking for popups... ---")

        browser.find_element_by_css_selector('.qtip-button').click() or browser.find_element_by_css_selector('.submitBig').click()
        print("!!! Pop up detected !!!")
        pass
    except NoSuchElementException:
        print("+++ No popup detected +++")

        pass

    captcha_xpath_code_text = check_exists_by_xpath('//*[@id=\"page\"]/form/table/tbody/tr[7]/td[2]/table/tbody/tr/td[1]/a')
    captcha_xpath_image = check_exists_by_xpath('//*[@id=\"page\"]/form/table/tbody/tr[7]/td[2]/table/tbody/tr/td[2]/img')
    captcha_empty_space = check_exists_by_xpath('//*[@id=\"page\"]/form/table/tbody/tr[7]/td[2]/table/tbody/tr/td[3]')
    captcha_xpath_input_box = check_exists_by_xpath('//*[@id=\"page\"]/form/table/tbody/tr[7]/td[2]/table/tbody/tr/td[3]/input')
    captcha_xpath_image_questionmark = check_exists_by_xpath('//*[@id=\"page\"]/form/table/tbody/tr[7]/td[2]/table/tbody/tr/td[3]/strong/a')
    captcha_css_selector_code_text = check_exists_by_css_selector('#page > form:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > a:nth-child(1)')
    captcha_css_selector_image = check_exists_by_css_selector('#page > form:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > img:nth-child(1)')
    #captcha_css_selector_input = check_exists_by_css_selector('.input2')
    captcha_css_selector = check_exists_by_css_selector('#page > form:nth-child(2) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(7) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > a:nth-child(1)')

    if captcha_xpath_code_text or captcha_css_selector or captcha_xpath_image or captcha_empty_space or captcha_xpath_input_box or captcha_xpath_image_questionmark or captcha_css_selector_code_text or captcha_css_selector_image == True:
        
        print("!!! Captcha found !!!")
        box = 2062, 390, 2167, 436

        #full_screen_capture = getScreenAsImage()
        Screen_capture = getRectAsImage((box))
        Screen_capture.save(os.getcwd() + '\\full_snap__' + 'hostage.png', format='png')

        time_need_to_stay_idle = 300
        print("!!! The bot will restart after %s seconds !!!" % (time_need_to_stay_idle))
        time.sleep(time_need_to_stay_idle)
        restart()
        
    else:
        print("+++ Captcha not found +++")

        return

def get_captcha_v1_crime():
    print("--- Looking for Captcha ---")

    try:
        print("--- Looking for popups... ---")

        browser.find_element_by_css_selector('.qtip-button').click() or browser.find_element_by_css_selector('.submitBig').click()
        print("!!! Pop up detected !!!")
        pass
    except NoSuchElementException:
        print("+++ No popup detected +++")

        pass

    captcha_xpath_code_text = check_exists_by_xpath('//*[@id=\"page\"]/form/table/tbody/tr[7]/td[2]/table/tbody/tr/td[1]/a')
    captcha_xpath_image = check_exists_by_xpath('//*[@id=\"page\"]/form/table/tbody/tr[7]/td[2]/table/tbody/tr/td[2]/img')
    captcha_empty_space = check_exists_by_xpath('//*[@id=\"page\"]/form/table/tbody/tr[7]/td[2]/table/tbody/tr/td[3]')
    captcha_xpath_input_box = check_exists_by_xpath('//*[@id=\"page\"]/form/table/tbody/tr[7]/td[2]/table/tbody/tr/td[3]/input')
    captcha_xpath_image_questionmark = check_exists_by_xpath('//*[@id=\"page\"]/form/table/tbody/tr[7]/td[2]/table/tbody/tr/td[3]/strong/a')
    captcha_css_selector_code_text = check_exists_by_css_selector('#page > form:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > a:nth-child(1)')
    captcha_css_selector_image = check_exists_by_css_selector('#page > form:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > img:nth-child(1)')
    captcha_css_selector_input = check_exists_by_css_selector('.input2')
    captcha_css_selector = check_exists_by_css_selector('#page > form:nth-child(2) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(7) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > a:nth-child(1)')

    if captcha_xpath_code_text or captcha_css_selector or captcha_xpath_image or captcha_empty_space or captcha_xpath_input_box or captcha_xpath_image_questionmark or captcha_css_selector_code_text or captcha_css_selector_image or captcha_css_selector_input == True:
        
        print("!!! Captcha found !!!")
        box = 2062, 389, 2164, 427

        #full_screen_capture = getScreenAsImage()
        Screen_capture = getRectAsImage((box))
        Screen_capture.save(os.getcwd() + '\\full_snap__' + 'crime.png', format='png')

        time_need_to_stay_idle = 300
        print("!!! The bot will restart after %s seconds !!!" % (time_need_to_stay_idle))
        time.sleep(time_need_to_stay_idle)
        restart()
        
    else:
        print("+++ Captcha not found +++")
        return

def get_captcha_v1_training():
    print("--- Looking for Captcha ---")

    try:
        print("--- Looking for popups... ---")

        browser.find_element_by_css_selector('.qtip-button').click() or browser.find_element_by_css_selector('.submitBig').click()
        print("!!! Pop up detected !!!")
        pass
    except NoSuchElementException:
        print("+++ No popup detected +++")

        pass

    captcha_xpath_code_text = check_exists_by_xpath('//*[@id=\"page\"]/form/table/tbody/tr[7]/td[2]/table/tbody/tr/td[1]/a')
    captcha_xpath_image = check_exists_by_xpath('//*[@id=\"page\"]/form/table/tbody/tr[7]/td[2]/table/tbody/tr/td[2]/img')
    captcha_empty_space = check_exists_by_xpath('//*[@id=\"page\"]/form/table/tbody/tr[7]/td[2]/table/tbody/tr/td[3]')
    captcha_xpath_input_box = check_exists_by_xpath('//*[@id=\"page\"]/form/table/tbody/tr[7]/td[2]/table/tbody/tr/td[3]/input')
    captcha_xpath_image_questionmark = check_exists_by_xpath('//*[@id=\"page\"]/form/table/tbody/tr[7]/td[2]/table/tbody/tr/td[3]/strong/a')
    captcha_css_selector_code_text = check_exists_by_css_selector('#page > form:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > a:nth-child(1)')
    captcha_css_selector_image = check_exists_by_css_selector('#page > form:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > img:nth-child(1)')
    captcha_css_selector_input = check_exists_by_css_selector('.input2')
    captcha_css_selector = check_exists_by_css_selector('#page > form:nth-child(2) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(7) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > a:nth-child(1)')

    if captcha_xpath_code_text or captcha_css_selector or captcha_xpath_image or captcha_empty_space or captcha_xpath_input_box or captcha_xpath_image_questionmark or captcha_css_selector_code_text or captcha_css_selector_image or captcha_css_selector_input == True:
        
        print("!!! Captcha found !!!")
        box = 2064, 309, 2175, 355

        #full_screen_capture = getScreenAsImage()
        Screen_capture = getRectAsImage((box))
        Screen_capture.save(os.getcwd() + 'training.png', format='png')

        time_need_to_stay_idle = 300
        print("!!! The bot will restart after %s seconds !!!" % (time_need_to_stay_idle))
        time.sleep(time_need_to_stay_idle)
        restart()
        
    else:
        print("+++ Captcha not found +++")
        return

def get_captcha_v1_carjack():
    print("--- Looking for Captcha ---")

    try:
        print("--- Looking for popups... ---")

        browser.find_element_by_css_selector('.qtip-button').click() or browser.find_element_by_css_selector('.submitBig').click()
        print("!!! Pop up detected !!!")
        pass
    except NoSuchElementException:
        print("+++ No popup detected +++")

        pass

    captcha_xpath_code_text = check_exists_by_xpath('//*[@id=\"page\"]/form/table/tbody/tr[7]/td[2]/table/tbody/tr/td[1]/a')
    captcha_xpath_image = check_exists_by_xpath('//*[@id=\"page\"]/form/table/tbody/tr[7]/td[2]/table/tbody/tr/td[2]/img')
    captcha_empty_space = check_exists_by_xpath('//*[@id=\"page\"]/form/table/tbody/tr[7]/td[2]/table/tbody/tr/td[3]')
    captcha_xpath_input_box = check_exists_by_xpath('//*[@id=\"page\"]/form/table/tbody/tr[7]/td[2]/table/tbody/tr/td[3]/input')
    captcha_xpath_image_questionmark = check_exists_by_xpath('//*[@id=\"page\"]/form/table/tbody/tr[7]/td[2]/table/tbody/tr/td[3]/strong/a')
    captcha_css_selector_code_text = check_exists_by_css_selector('#page > form:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > a:nth-child(1)')
    captcha_css_selector_image = check_exists_by_css_selector('#page > form:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > img:nth-child(1)')
    captcha_css_selector_input = check_exists_by_css_selector('.input2')
    #captcha_css_selector = check_exists_by_css_selector('#page > form:nth-child(2) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(7) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > a:nth-child(1)')

    if captcha_xpath_code_text or captcha_xpath_image or captcha_empty_space or captcha_xpath_input_box or captcha_xpath_image_questionmark or captcha_css_selector_code_text or captcha_css_selector_image or captcha_css_selector_input == True:
        
        print("!!! Captcha found !!!")
        box = 2062, 348, 2165, 389

        Screen_capture = getRectAsImage((box))
        Screen_capture.save(os.getcwd() + 'carjack.png', format='png')

        time_need_to_stay_idle = 300
        print("!!! The bot will restart after %s seconds !!!" % (time_need_to_stay_idle))
        time.sleep(time_need_to_stay_idle)
        restart()
        
    else:
        print("+++ Captcha not found +++")
        return



def get_captcha_v1_hooker():
    print("--- Looking for Captcha ---")
    
    try:
        print("--- Looking for popups... ---")

        browser.find_element_by_css_selector('.qtip-button').click() or browser.find_element_by_css_selector('.submitBig').click()
        print("!!! Pop up detected !!!")
        pass
    except NoSuchElementException:
        print("+++ No popup detected +++")

        pass

    captcha_xpath_code_text = check_exists_by_xpath('//*[@id=\"page\"]/form/table/tbody/tr[7]/td[2]/table/tbody/tr/td[1]/a')
    captcha_xpath_image = check_exists_by_xpath('//*[@id=\"page\"]/form/table/tbody/tr[7]/td[2]/table/tbody/tr/td[2]/img')
    captcha_empty_space = check_exists_by_xpath('//*[@id=\"page\"]/form/table/tbody/tr[7]/td[2]/table/tbody/tr/td[3]')
    captcha_xpath_input_box = check_exists_by_xpath('//*[@id=\"page\"]/form/table/tbody/tr[7]/td[2]/table/tbody/tr/td[3]/input')
    captcha_xpath_image_questionmark = check_exists_by_xpath('//*[@id=\"page\"]/form/table/tbody/tr[7]/td[2]/table/tbody/tr/td[3]/strong/a')
    captcha_css_selector_code_text = check_exists_by_css_selector('#page > form:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > a:nth-child(1)')
    captcha_css_selector_image = check_exists_by_css_selector('#page > form:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > img:nth-child(1)')
    captcha_css_selector_input = check_exists_by_css_selector('.input2')
    #captcha_css_selector_questionmark = captcha_css_selector('#page > form:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(3) > strong:nth-child(2) > a:nth-child(1)')
    captcha_css_selector = check_exists_by_css_selector('#page > form:nth-child(2) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(7) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > a:nth-child(1)')

    if captcha_css_selector_input or captcha_xpath_code_text or captcha_css_selector or captcha_xpath_image or captcha_empty_space or captcha_xpath_input_box or captcha_xpath_image_questionmark or captcha_css_selector_code_text or captcha_css_selector_image == True:

        print("!!! Captcha found !!!")
        box = 2065, 315, 2179, 358

        Screen_capture = getRectAsImage((box))
        Screen_capture.save(os.getcwd() + 'hooker.png', format='png')

        time_need_to_stay_idle = 300
        print("!!! The bot will restart after %s seconds !!!" % (time_need_to_stay_idle))
        time.sleep(time_need_to_stay_idle)
        restart()
        
    else:
        print("+++ Captcha not found +++")
        return


        

def get_captcha(browser, element, path):

    #(2063, 391, 2166, 423)
    # now that we have the preliminary stuff out of the way time to get that image :D
    location = element.location
    size = element.size
    # saves screenshot of entire page
    browser.save_screenshot(path)

    # uses PIL library to open image in memory
    image = Image.open(path)

    left = location['x']
    top = location['y'] + 140
    right = location['x'] + size['width']
    bottom = location['y'] + size['height'] + 140

    image = image.crop((left, top, right, bottom))  # defines crop points
    image.save(path, 'jpeg')  # saves new cropped image

def homepage():
    browser.get(website)
    time.sleep(2)

def timer(x):
    return_tijd = ' '.join(map(str, x))
    return return_tijd

def checksum():
    print("Checksum wordt gestart..")
    time.sleep(5)


##############################################################################################################################################################################################################



def get_crime():
    global misdaad_timer_check
    misdaad_timer_check = str(misdaad_timer.text)
    if misdaad_timer_check == 'Nu':
        print("+++ Crime available +++")
        misdaad_timer.click()
        time.sleep(2)
        misdaad_timerr = browser.find_element_by_xpath('//*[@id=\"page\"]/form/table/tbody/tr[1]/td[4]/small').text
        misdaad_timerr = get_numbers(misdaad_timerr)
        misdaad_timerr = ' '.join(map(str, misdaad_timerr))
        #misdaad_timerr = float(int(misdaad_timerr))
        get_captcha_v1_crime()
        #checkbox_crime = browser.find_element_by_xpath('//*[@id=\"page\"]/form/table/tbody/tr[6]/td[1]/input')
        #checkbox_crime.click()
        try:
            misdaad_uitvoeren = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".submitBig")))
            browser.find_element_by_css_selector('.submitBig').click()
        finally:
            print("*** Crime will be done in %s seconds ***" % (misdaad_timerr))
            get_profile()
            
    else:
        print("--- Crime Unavailable for %s seconds ---" % (misdaad_timer_check))
        return

def carjack():
    global car_timer
    car_timer_check = str(car_timer.text)

    if car_timer_check == 'Nu':
        print("+++ Carjack Available +++")
        car_timer.click()
        time.sleep(1)
        car_timer = browser.find_element_by_xpath('//*[@id=\"page\"]/form/table/tbody/tr[1]/td[4]/small').text
        car_timer = get_numbers(car_timer)
        car_timer = ' '.join(map(str,car_timer))
        #car_timer = float(int(car_timer))

        try:
            carjack_uitvoeren = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".submitBig")))
            get_captcha_v1_carjack()
            #checkbox_carjack = browser.find_element_by_xpath('//*[@id=\"page\"]/form/table/tbody/tr[4]/td[1]/input')
            #checkbox_carjack.click()
            carjack_uitvoeren.click()
            print("*** Carjack will be done in %s minutes ***" %(car_timer))
            get_profile()

        except NoSuchElementException:
            print("--- Carjack run button not found ---")
            get_profile()

    else:
        print("--- Carjack Unavailable for %s seconds ---" %(car_timer_check))
        return

def submit_button(available, unavailable):
        try:
            get_some = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".submitBig")))
            get_captcha_v1()
            get_some.click()
            print(available)
            get_profile()

        except NoSuchElementException:
            print(unavailable)
            return
    

def get_hookers():
    global hooker_timer_string
    hooker_timer_string = str(hooker_timer.text)
    if hooker_timer_string == 'Nu':
        print("+++ Hookers Available +++")
        hooker_timer.click()
        time.sleep(1)
        checkbox_hooker = browser.find_element_by_xpath('//*[@id=\"page\"]/form/table/tbody/tr[1]/td[1]/input')
        checkbox_hooker.click()

        try:
            get_some_hookers = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".submitBig")))
            get_captcha_v1_hooker()
            get_some_hookers.click()
            print("*** New hookers are requested ***")
            get_profile()

        except NoSuchElementException:
            print("--- Hookers not found on the streets ---")
            get_profile()
            
    else:
        print("--- There are no hookers on the streets for %s seconds ---" % (hooker_timer_string))
        return

    #als in hookers in de tag tbody gevangenis voorkomt go back to homepage
#tbody
#Je zit in de gevangenis 

def wheel_of_fortune():
    global rad_of_fortune_timer_string
    rad_of_fortune_timer_string = str(rad_of_fortune_timer.text)
    if rad_of_fortune_timer_string == 'Nu':
        print("+++ Wheel of furtune is available +++")
        rad_of_fortune_timer.click()
        time.sleep(1)
        try:
            spin = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id=\"btn_spin\"]')))
            get_captcha_v1()
            spin.click()
            print("*** Finished wheel of fortune ***")
            time.sleep(2)
            get_profile()

        except NoSuchElementException:
            print("--- Can't find rad of furtune to spin ---")
            get_profile()
    else:
        print("--- Wheel of furtune is unavailable for %s seconds ---" % (rad_of_fortune_timer_string))
        return

def get_hostage():
    global gijzel_timer_string
    gijzel_timer_string = str(gijzel_timer.text)
    if gijzel_timer_string == 'Nu':
        print("+++ Hostage Available +++")
        gijzel_timer.click()
        time.sleep(1)
        try:
            #checkbox_hostage = browser.find_element_by_xpath('//*[@id=\"page\"]/form/table/tbody/tr[4]/td[1]/input')
            #checkbox_hostage.click()
            #get_hostage_in_jail = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".submitBig")))
            get_hostage_in_jail = browser.find_element_by_css_selector('.submitBig')
            get_captcha_v1_hostage()
            get_hostage_in_jail.click()
            print("*** Hostage taken ***")
            get_profile()

        except NoSuchElementException:
            print("--- Can't find any hostages ---")
            get_profile()

    else:
        print("--- Hostage available in %s seconde ---" %(gijzel_timer_string))
        return

def get_training():
    global train_timer_string
    train_timer_string = str(train_timer.text)
    if train_timer_string == 'Nu':
        print("+++ Training Available +++")
        train_timer.click()
        time.sleep(1)
        try:
            submit_training = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".submit")))
            get_captcha_v1_training()
            submit_training.click()
            print("*** You are a lot stronger now ***")
            get_profile()

        except NoSuchElementException:
            print("--- Can't train right now ---")
            get_profile()

    else:
        print("--- Training available in %s seconde ---" %(train_timer_string))
        return


def get_shooting():
    global shoot_timer_string
    shoot_timer_string = str(shoot_timer.text)
    if shoot_timer_string == 'Nu':
        print("+++ Shooting range available +++")
        shoot_timer.click()
        time.sleep(1)
        try:
            submit_shooting = browser.find_element_by_name('schieten')
            get_captcha_v1_shooting_range()
            submit_shooting.click()
            print("*** Shooting skills increased ***")
            get_profile()

        except:
            print("--- Shooting range is unavailable ---")
            get_profile()

    else:
        print("--- Training available in %s seconds ---" %(shoot_timer_string))
        return


def loop():
    print("\n Inizialize...")

    if jail_timer.text == 'Vrij' and travel_timer.text == 'Nu':
        
        global bot_ronde
        global total_rounds
        bot_ronde += 1
        print("*** %s / 100 Rounds before restart, Total rounds finished : %s ***" % (bot_ronde, total_rounds))
        if bot_ronde == 100:
            restart()
        else:
            time.sleep(.1)
            wheel_of_fortune()
            time.sleep(.1)
            carjack()
            time.sleep(.1)
            get_training()
            time.sleep(.1)
            #get_shooting()
            #time.sleep(.1)
            get_hostage()
            time.sleep(.1)
            get_hookers()
            time.sleep(.1)
            get_crime()
            print("+++ DONE +++")
            time.sleep(.1)
            get_profile()



    else:
        print("--- You are; or in prison for %s seconds.., or you are not able to walk ---" %(jail_timer.text))
        time.sleep(30)
        get_profile()

def get_profile():
    #Homepage Timers
    homepage()

    try:
        print("--- Looking for popups... ---")
        browser.find_element_by_css_selector('.qtip-button').click()
        print("!!! Pop up detected !!!")
        pass
    except NoSuchElementException:
        print("+++ No popup detected +++")
        pass

    #Wachttijden

    global misdaad_timer, gijzel_timer, car_timer, overval_timer, georganiseerd_timer, hooker_timer, rad_of_fortune_timer, jail_timer, train_timer, travel_timer, shoot_timer
    global murder_timer, bescherming_timer, familie_misdaad, familie_org_misdaad, hoger_lager_timer, uitbreek_timer

    try:

        misdaad_timer = browser.find_element_by_xpath('//*[@id=\"page\"]/table[1]/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[1]/td[3]/a')
        #print(misdaad_timer.text)

        gijzel_timer = browser.find_element_by_xpath('//*[@id=\"page\"]/table[1]/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td[3]/a')
        #print(gijzel_timer.text)

        car_timer = browser.find_element_by_xpath('//*[@id=\"page\"]/table[1]/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[3]/td[3]/a')
        #print(car_timer.text)

        overval_timer = browser.find_element_by_xpath('//*[@id=\"page\"]/table[1]/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[4]/td[3]/a')
        #print(overval_timer.text)

        georganiseerd_timer = browser.find_element_by_xpath('//*[@id=\"page\"]/table[1]/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[5]/td[3]/a')
        #print(georganiseerd_timer.text)

        hooker_timer = browser.find_element_by_xpath('//*[@id=\"page\"]/table[1]/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[6]/td[3]/a')
        #print(hooker_timer.text)

        rad_of_fortune_timer = browser.find_element_by_xpath('//*[@id=\"page\"]/table[1]/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td[3]/a')
        #print(rad_of_fortune_timer.text)

        jail_timer = browser.find_element_by_xpath('//*[@id=\"page\"]/table[1]/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[9]/td[3]/a')
        #print(jail_timer.text)

        train_timer = browser.find_element_by_xpath('//*[@id=\"page\"]/table[1]/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[1]/td[6]/a')
        #print(train_timer.text)

        travel_timer = browser.find_element_by_xpath('//*[@id=\"page\"]/table[1]/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td[6]/a')
        #print(travel_timer.text)

        shoot_timer = browser.find_element_by_xpath('//*[@id=\"page\"]/table[1]/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[3]/td[6]/a')
        #print(shoot_timer.text)

        murder_timer = browser.find_element_by_xpath('//*[@id=\"page\"]/table[1]/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[4]/td[6]/a')
        #print(murder_timer.text)

        bescherming_timer = browser.find_element_by_xpath('//*[@id=\"page\"]/table[1]/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[5]/td[6]/a')
        #print(bescherming_timer.text)

        familie_misdaad = browser.find_element_by_xpath('//*[@id=\"page\"]/table[1]/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[6]/td[6]/a')
        #print(familie_misdaad.text)

        familie_org_misdaad = browser.find_element_by_xpath('//*[@id=\"page\"]/table[1]/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[7]/td[6]/a')
        #print(familie_org_misdaad.text)

        hoger_lager_timer = browser.find_element_by_xpath('//*[@id=\"page\"]/table[1]/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td[6]/a')
        #print(hoger_lager_timer.text)

        uitbreek_timer = browser.find_element_by_xpath('//*[@id=\"page\"]/table[1]/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[9]/td[6]/a')
        #print(uitbreek_timer.text)

        # Goederen

        global credits, zakjes_drugs, flessen_drank, energie, kogels, cannabis

        credits = browser.find_element_by_xpath('//*[@id=\"page\"]/table[2]/tbody/tr/td[1]/table/tbody/tr[2]/td[3]/a')
        #print(credits.text)

        zakjes_drugs = browser.find_element_by_xpath('//*[@id=\"page\"]/table[2]/tbody/tr/td[1]/table/tbody/tr[3]/td[3]/a')
        #print(zakjes_drugs.text)

        flessen_drank = browser.find_element_by_xpath('//*[@id=\"page\"]/table[2]/tbody/tr/td[1]/table/tbody/tr[4]/td[3]/a')
        #print(flessen_drank.text)

        energie = browser.find_element_by_xpath('//*[@id=\"page\"]/table[2]/tbody/tr/td[1]/table/tbody/tr[5]/td[3]/a')
        #print(energie.text)

        kogels = browser.find_element_by_xpath('//*[@id=\"page\"]/table[2]/tbody/tr/td[1]/table/tbody/tr[6]/td[3]/a')
        #print(kogels.text)

        cannabis = browser.find_element_by_xpath('//*[@id=\"page\"]/table[2]/tbody/tr/td[1]/table/tbody/tr[7]/td[3]/a')
        #print(cannabis.text)

        # Macht

        global positie, power, rang, gangsters, hitmen, hookers

        positie = browser.find_element_by_xpath('//*[@id=\"page\"]/table[2]/tbody/tr/td[2]/table/tbody/tr[2]/td[3]/a')
        #print(positie.text)

        power = browser.find_element_by_xpath('//*[@id=\"page\"]/table[2]/tbody/tr/td[2]/table/tbody/tr[3]/td[3]/a')
        #print(power.text)

        rang = browser.find_element_by_xpath('//*[@id=\"page\"]/table[2]/tbody/tr/td[2]/table/tbody/tr[4]/td[3]/a')
        #print(rang.text)

        gangsters = browser.find_element_by_xpath('//*[@id=\"page\"]/table[2]/tbody/tr/td[2]/table/tbody/tr[5]/td[3]/a')
        #print(gangsters.text)

        hitmen = browser.find_element_by_xpath('//*[@id=\"page\"]/table[2]/tbody/tr/td[2]/table/tbody/tr[6]/td[3]/a')
        #print(hitmen.text)

        hookers = browser.find_element_by_xpath('//*[@id=\"page\"]/table[2]/tbody/tr/td[2]/table/tbody/tr[7]/td[3]/a')
        #print(hookers.text)

        # level statestieken

        global level, xp

        level = browser.find_element_by_xpath('//*[@id=\"rankBox\"]/span/a')
        #print(level.text)

        xp = browser.find_element_by_xpath('//*[@id=\"rankBox\"]/a')
        #print(xp.text)

        #premium = browser.find_element_by_xpath('//*[@id=\"page\"]/h1/span[2]/a')
        #print(premium.text)

        print("\n Console : \n+++++++ \n \n Statics: \n*** \n Level : %s \n Experience : %s \n Membership : Not Valid Input \n \n Protection : %s \n Rank Position : %s \n Nickname : %s \n Power : %s \n Gangsters : %s \n Hitmen : %s \n Hookers : %s \n Jail time : %s \n Jailbreak : %s \n \nGoods : \n*** \n Credits :  %s \n Drugbags :  %s \n Alcohol :  %s \n Energy :  %s \n Bullets :  %s \n Cannabis :  %s \n \nTimers: \n*** \n Actions \n --- \n \n Crime : %s \n Kidnap : %s \n Carjack :  %s \n Robbery : %s \n Organized Crime : %s \n Hookers : %s \n --- \n Specials : \n --- \n \n Wheel of fortune : %s \n High or low : %s \n  --- \n Skills : \n --- \n \n GYM :  %s \n Travel :  %s \n Shootingskill :  %s \n Murder timer :  %s \n \n --- \n Family : \n --- \n \n Family crime :  %s \n Family organized crime :  %s \n \n ---End of profile --- \n ---------------------" % (level.text, xp.text, bescherming_timer.text, positie.text, rang.text, power.text, gangsters.text, hitmen.text, hookers.text, jail_timer.text, uitbreek_timer.text, credits.text, zakjes_drugs.text, flessen_drank.text, energie.text, kogels.text, cannabis.text, misdaad_timer.text, gijzel_timer.text, car_timer.text, overval_timer.text, georganiseerd_timer.text, hooker_timer.text, rad_of_fortune_timer.text, hoger_lager_timer.text, train_timer.text, travel_timer.text, shoot_timer.text, murder_timer.text, familie_misdaad.text, familie_org_misdaad.text))
        time.sleep(1)

        global wait

        wait = WebDriverWait(browser, 10)
        loop()

    except NoSuchElementException:
        print("Xpath are corrupt profile can not be read, maybe the website did got an update?")
        restart()    

def start_bot():
    global bot_ronde

    bot_ronde = 0
    inloggen()
    # Resize the window to the screen width/height
    browser.set_window_size(1024, 700)
    # Move the window to position x/y
    browser.set_window_position(1980, 0) #Original
    #browser.set_window_position(10 , 0) #non-Original
    get_profile()

def restart():
    browser.stop_client()
    browser.close()
    print("Bot will restart in 10 seconds, be patient..")
    global total_rounds
    total_rounds += 1
    time.sleep(10)
    start_bot()
    

if __name__ == '__main__':
    total_rounds = 0
    sys.setrecursionlimit(10000)
    start_bot()
    #Thread(target = start_bot).start()
    #Thread(target = checksum).start()


