##-----------run in the Terminal-----------
##pip3 install selenium--- for download selenium
##pip3 install pytest--- for download pytest


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/'


def OpenWeb():
    return driver.get(url), driver.maximize_window(), time.sleep(2)


def find_element(Css):
    element = driver.find_element(By.CSS_SELECTOR, Css)
    return element

def Login_Customer(CssFromList):
    CustomerLogin = find_element('body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(1) > button').click()
    time.sleep(1)
    UserName = find_element(CssFromList).click()
    time.sleep(1)
    LoginButton = find_element('body > div > div > div.ng-scope > div > form > button').click()
    time.sleep(1)

def Diposit_by_Customer(Amount):
    DepositList = find_element('body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(2)').click()
    time.sleep(1)
    DepositAmount = find_element('body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > div > input').send_keys(Amount)
    time.sleep(1)
    DepositFinalButton = find_element('body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > button').click()


def Withdraw_by_Customer(Amount):
    WithdrawlList = find_element('body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(3)').click()
    time.sleep(1)
    WithdrawAmount = find_element('body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > div > input').send_keys(Amount)
    time.sleep(1)
    WithdrawFinalButton = find_element('body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > button').click()
    time.sleep(1)




def Customer_exist_in_listCust(first_name):
    x = False
    tabale = find_element('body > div > div > div.ng-scope > div > div.ng-scope > div > div > table')
    body = find_element('body > div > div > div.ng-scope > div > div.ng-scope > div > div > table > tbody')
    rows = driver.find_elements(By.TAG_NAME, "tr")
    for i in rows:
        columns = i.find_elements(By.TAG_NAME, "td")
        for j in range(len(columns)):
            if columns[j].text == first_name:
                x = True
    return x


def Add_New_customer(firstName, lastName, postalCode):
    ManagerLogin = find_element('body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(3) > button').click()
    time.sleep(1)
    AddCustomerList = find_element('body > div > div > div.ng-scope > div > div.center > button:nth-child(1)').click()
    time.sleep(1)
    NewF_name = find_element('body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(1) > input').send_keys(firstName)
    NewL_name = find_element('body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(2) > input').send_keys(lastName)
    time.sleep(1)
    NewPcode = find_element('body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(3) > input').send_keys(postalCode)
    time.sleep(1)
    AddCustomerButton = find_element('body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > button').click()
    time.sleep(3)

def Delete_customer_by_maneger(Css):
    ManagerLogin = find_element('body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(3) > button').click()
    time.sleep(1)
    CustomersList = find_element('body > div > div > div.ng-scope > div > div.center > button:nth-child(3)').click()
    time.sleep(1)
    DelcusButton = find_element(Css).click()
    time.sleep(2)

