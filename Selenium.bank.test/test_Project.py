
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import datetime
import time
import pytest
from main import*




#---------------------------------TESTS BY CUSTOMER USER ---------------------------------

class TestsForCustomerUser:


    #-------------------positive check deposit by customer (Ron .W)---------------------------

    def test_deposit_Amount_1(self):
        driver = webdriver.Chrome()
        OpenWeb(driver)
        time.sleep(2)
        Login_Customer(driver, '#userSelect > option:nth-child(4)')
        BalanceBefore = find_element(driver, 'body > div > div > div.ng-scope > div > div:nth-child(3) > strong:nth-child(2)').text
        Diposit_by_Customer(driver, 250)
        Expected = 250
        Actual = int(BalanceBefore) + 250
        assert Actual == Expected



    #---------------positive check money transfer opertions (Deposit, Withdraw) by customer (Haary .P) --------------

    def test_deposit_and_withraw_customer_4(self):
        driver = webdriver.Chrome()
        OpenWeb(driver)
        Login_Customer(driver, '#userSelect > option:nth-child(3)')
        Diposit_by_Customer(driver, 1000)
        time.sleep(1)
        Withdraw_by_Customer(driver, 250)
        BalanceHarry = find_element(driver, 'body > div > div > div.ng-scope > div > div:nth-child(3) > strong:nth-child(2)')
        time.sleep(1)
        Expected = 750
        Actual = int(BalanceHarry.text)
        assert Expected == Actual


    #-------------------positive check transfer of money by customer (Hermoine .G) ---------------------------

    def test_transfer_money_6(self):
        driver = webdriver.Chrome()
        OpenWeb(driver)
        Login_Customer(driver, '#userSelect > option:nth-child(2)')
        Withdraw_by_Customer(driver, 1500)
        TransactionsList = find_element(driver, 'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(1)').click()
        now = datetime.datetime.now()
        tday = now.strftime("%d-%m-%Y")
        time.sleep(1)
        DateToday = find_element(driver, '#start').send_keys(tday)
        time.sleep(1)
        AmountTabeleTransactions = find_element(driver, '#anchor0 > td:nth-child(2)')
        Actual = AmountTabeleTransactions.text
        Expected = '1500'
        assert Actual == Expected



#---------------------------------TESTS BY MENEGER USER ---------------------------------

class TestsForMenegerUser:

    # -------------------positive check delete customer Albus by manager login---------------------------

    def test_delete_customer_2(self):
        driver = webdriver.Chrome()
        OpenWeb(driver)
        time.sleep(1)
        Delete_customer_by_maneger(driver, 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > table > tbody > tr:nth-child(4) > td:nth-child(5) > button')
        IsNotExist = Customer_exist_in_listCust(driver, 'Albus')
        assert IsNotExist == False


    # -------------------positive check create a new customer by manager login---------------------------

    def test_create_new_customer_3(self):
        driver = webdriver.Chrome()
        OpenWeb(driver)
        time.sleep(1)
        Add_New_customer(driver, 'Severus', 'Snape', 'E16AN')
        time.sleep(1)
        driver.switch_to.alert.accept()
        time.sleep(1)
        CustomersList = find_element(driver, 'body > div > div > div.ng-scope > div > div.center > button:nth-child(3)').click()
        time.sleep(1)
        ExistInList = Customer_exist_in_listCust(driver, 'Severus')
        assert ExistInList == True


    #-------------------positive check create a new account by maneger ---------------------------

    def test_create_new_account_5(self):
        driver = webdriver.Chrome()
        OpenWeb(driver)
        time.sleep(1)
        Add_New_customer(driver, 'Severus', 'Snape', 'E16AN')
        time.sleep(1)
        driver.switch_to.alert.accept()
        time.sleep(1)
        OpenAccountList = find_element(driver, 'body > div > div > div.ng-scope > div > div.center > button:nth-child(2)').click()
        time.sleep(1)
        NewAccountName = find_element(driver, '#userSelect > option:nth-child(7)').click()
        time.sleep(1)
        NewAccountCurrency = find_element(driver, '#currency > option:nth-child(3)').click()
        time.sleep(1)
        ProcessOpenAccount = find_element(driver, 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > button').click()
        time.sleep(2)
        driver.switch_to.alert.accept()
        Actual = driver.current_url
        Expected = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/openAccount'
        assert Actual == Expected



