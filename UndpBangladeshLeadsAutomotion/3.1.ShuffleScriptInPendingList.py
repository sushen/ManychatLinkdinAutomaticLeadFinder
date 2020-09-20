#  Copyright (c) 2020.
#  Version : 1.0.2
#  Script Author : Sushen Biswas and Pedro Brito
#
#  Sushen Biswas Github Link : https://github.com/sushen
#  Pedro Brito Github Link : https://github.com/XiBiTuH
#
#  !/usr/bin/env python
#  coding: utf-8
#
#  Sushen Biswas Github Link : https://github.com/sushen
#  Pedro Brito Github Link : https://github.com/XiBiTuH
#
#  !/usr/bin/env python
#  coding: utf-8

from selenium import webdriver
import time
import random
import os
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.chrome.options import Options



chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome("K:\Project\Python\LeadsAutomotionInLinkdIn\chromedriver.exe",chrome_options=chrome_options)
chrome_options.add_argument("user-data-dir=chrome-data")
driver.implicitly_wait(25)  # seconds



# What will be searched

# Time waiting for page
waiting_for_page = 10

driver.get("https://www.linkedin.com/")

'''f = open("user.txt", "r")
data = f.read()
username = str(data).split("\n")[0]
password = str(data).split("\n")[1]
'''

# Login
try:
    # I use environment veriable base on this tutorials https://www.youtube.com/watch?v=IolxqkL7cD8
    username = os.environ.get('my_Linkdin_username')
    password = os.environ.get('my_Linkdin_password')

    driver.find_element_by_id("session_key").send_keys(username)
    driver.find_element_by_id("session_password").send_keys(password)
    time.sleep(1)

    driver.find_element_by_class_name("sign-in-form__submit-button").click()
    time.sleep(waiting_for_page)
except:
    pass



# No 2 : Change
# #Replace this with the link of your list
url = "https://www.linkedin.com/sales/lists/people/6709657449168805888?sortCriteria=CREATED_TIME"

driver.get(url)
time.sleep(waiting_for_page)

try:
    pages = int(driver.find_element_by_class_name("search-results__pagination-list").find_elements_by_tag_name("li")[
                    -1].text.split("…")[-1])
except:
    pages = 1

for i in range(pages):

    people = driver.find_element_by_tag_name("table").find_elements_by_tag_name("tr")
    people = people[1:]

    aux_count = 0
    p = 0
    before = 0

    while p < len(people):

        is_pending = False
        is_connect = False

        people = driver.find_element_by_tag_name("table").find_elements_by_tag_name("tr")
        people = people[1:]

        if before != p:
            driver.execute_script("window.scrollTo(0, {})".format(aux_count))

        before = p

        time.sleep(1)

        people[p].find_elements_by_tag_name("button")[-1].click()

        time.sleep(2)

        aux = people[p].find_element_by_class_name("artdeco-dropdown__content-inner").find_elements_by_tag_name("li")
        aux2 = people[p].find_element_by_class_name("artdeco-dropdown__content-inner").find_elements_by_tag_name("div")

        # TO CHANGE
        #---------------------------------------------------------------------------------

        # List from where you wanna remove users - MAIN LIST
        list_to_remove = "UNDP Pending Member"



        #IS PENDING
        #--------------------------------------

        #List to add removed users
        list_to_add = "SlowLinkdinUNDPUser"

        #-------------------------------------------


        # IS CONNECT
        #-------------------------------------------
        message_to_connect = [
            "Hello Sir, \nI am serving International Organization for more than three years.\nOur company work in Unicef Somalia (Nairobi based) as a BI(Business Intelligence) Consultant. If you accept my invitation I will be a very glade.",
            "Hello Sir, \nI am working with UNDP base organization for more than three years.\nOur company work in Unicef Somalia (Nairobi based) as a BI(Business Intelligence) Consultant. If you accept my invitation I will be a very glade.",
            "Hello Sir, \nI am serving International Diplomate  for more than three years.my office is in Gulshan 2 near the Unicef hartal office.\nOur company work in Unicef Somalia (Nairobi based) as a BI(Business Intelligence) Consultant. If you accept my invitation I will be a very glade."
        ]

        email = "sushenbiswasaga@gmail.com"
        #-------------------------------------------


        #NO CONNECT AND NO PENDING
        #------------------------------------------
        list_to = "UNDP Connection"

        #-------------------------------------------------------------------------------------

        for m in range(len(aux2)):
            # No 3 : Change
            # Change to "Pending"
            if "Pending" in aux2[m].text:
                is_pending = True
                break

        for m in range(len(aux2)):
            # No 3 : Change
            # Change to "Connect"
            if "Connect" in aux2[m].text:
                is_connect = True
                break

        if is_pending:
            for m in range(len(aux)):
                # No 3 : Change
                # Change to "Add to another list"
                if "Add to another list" in aux[m].text:
                    aux[m].click()
                    time.sleep(3)

                    cont = driver.find_element_by_class_name("entity-lists-ta__ta-container")

                    btns = cont.find_elements_by_tag_name("button")

                    # Remove from list
                    for b in btns:
                        nm = ""
                        try:
                            nm = b.text.split("\n")[0]
                        except:
                            nm = b.text

                        if list_to_remove == nm:
                            b.click()

                    time.sleep(2)
                    mn = driver.find_element_by_class_name("entity-lists-ta__unselected-menu")
                    aux_btns = mn.find_elements_by_tag_name("button")

                    for xua in aux_btns:
                        nm = ""
                        try:
                            nm = xua.text.split(" (")[0]
                        except:
                            nm = xua.text

                        if list_to_add == nm:
                            xua.click()

                    time.sleep(1)
                    driver.find_element_by_class_name("edit-entity-lists-modal__save-btn").click()
                    p -= 1
                    break


        elif is_connect:
            pass


        else:
            for m in range(len(aux)):
                # No 3 : Change
                # Change to "Add to another list"
                if "Add to another list" in aux[m].text:
                    aux[m].click()
                    time.sleep(3)

                    cont = driver.find_element_by_class_name("entity-lists-ta__ta-container")

                    btns = cont.find_elements_by_tag_name("button")

                    # Remove from list
                    for b in btns:

                        nm = ""
                        try:
                            nm = b.text.split("\n")[0]
                        except:
                            nm = b.text
                        if list_to_remove == nm:
                            b.click()

                    time.sleep(2)
                    mn = driver.find_element_by_class_name("entity-lists-ta__unselected-menu")
                    aux_btns = mn.find_elements_by_tag_name("button")

                    for xua in aux_btns:
                        nm = ""
                        try:
                            nm = xua.text.split(" (")[0]
                        except:
                            nm = xua.text
                        if list_to == nm:
                            xua.click()

                    time.sleep(1)
                    driver.find_element_by_class_name("edit-entity-lists-modal__save-btn").click()
                    p -= 1
                    break

        driver.find_element_by_id("content-main").click()
        time.sleep(2)
        aux_count += 80
        p += 1

    try:
        driver.find_element_by_class_name("search-results__pagination-next-button").click()
    except:
        pass
    time.sleep(10)



# Close one and Start another
# Close the current browser
driver.close()



# Open another script after finish this one base on https://stackoverflow.com/questions/1027714/how-to-execute-a-file-within-the-python-interpreter/1027730
# exec(open("3.2.ShuffleScriptSlowLinkdinUNDPUserList.py").read())


