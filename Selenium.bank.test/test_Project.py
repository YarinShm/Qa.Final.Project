##-----------run in the Terminal-----------
##pip3 install selenium--- for download selenium
##pip3 install pytest--- for download pytest


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
        OpenWeb()
        Login_Customer('#userSelect > option:nth-child(4)')
        BalanceBefore = find_element('body > div > div > div.ng-scope > div > div:nth-child(3) > strong:nth-child(2)').text
        Diposit_by_Customer(250)
        excepted = 250
        actual = int(BalanceBefore) + 250
        assert actual == excepted



    #---------------positive check money transfer opertions (Deposit, Withdraw) by customer (Haary .P) --------------

    def test_deposit_and_withraw_customer_4(self):
        OpenWeb()
        Login_Customer('#userSelect > option:nth-child(3)')
        Diposit_by_Customer(1000)
        time.sleep(1)
        Withdraw_by_Customer(250)
        BalanceHarry = find_element('body > div > div > div.ng-scope > div > div:nth-child(3) > strong:nth-child(2)')
        time.sleep(1)
        excepted = 750
        actual = int(BalanceHarry.text)
        assert excepted == actual


    #-------------------positive check transfer of money by customer (Hermoine .G) ---------------------------

    def test_transfer_money_6(self):
        OpenWeb()
        Login_Customer('#userSelect > option:nth-child(2)')
        Withdraw_by_Customer(1500)
        TransactionsList = find_element('body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(1)').click()
        now = datetime.datetime.now()
        tday = now.strftime("%d-%m-%Y")
        time.sleep(1)
        DateToday = find_element('#start').send_keys(tday)
        time.sleep(1)
        AmountTabeleTransactions = find_element('#anchor0 > td:nth-child(2)')
        actual = AmountTabeleTransactions.text
        excepted = '1500'
        assert actual == excepted



#---------------------------------TESTS BY MENEGER USER ---------------------------------

class TestsForMenegerUser:

    # -------------------positive check delete customer Albus by manager login---------------------------

    def test_delete_customer_2(self):
        OpenWeb()
        Delete_customer_by_maneger('body > div > div > div.ng-scope > div > div.ng-scope > div > div > table > tbody > tr:nth-child(4) > td:nth-child(5) > button')
        IsNotExist = Customer_exist_in_listCust('Albus')
        assert IsNotExist == False

    # -------------------positive check create a new customer by manager login---------------------------

    def test_create_new_customer_3(self):
        OpenWeb()
        Add_New_customer('Severus', 'Snape', 'E16AN')
        time.sleep(1)
        driver.switch_to.alert.accept()
        time.sleep(1)
        CustomersList = find_element('body > div > div > div.ng-scope > div > div.center > button:nth-child(3)').click()
        time.sleep(1)
        ExistInList = Customer_exist_in_listCust('Severus')
        assert ExistInList == True


    #-------------------positive check create a new account by maneger ---------------------------

    def test_create_new_account_5(self):
        OpenWeb()
        Add_New_customer('Severus', 'Snape', 'E16AN')
        time.sleep(1)
        driver.switch_to.alert.accept()
        time.sleep(1)
        OpenAccountList = find_element('body > div > div > div.ng-scope > div > div.center > button:nth-child(2)').click()
        time.sleep(1)
        NewAccountName = find_element('#userSelect > option:nth-child(7)').click()
        time.sleep(1)
        NewAccountCurrency = find_element('#currency > option:nth-child(3)').click()
        time.sleep(1)
        ProcessOpenAccount = find_element('body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > button').click()
        time.sleep(2)
        driver.switch_to.alert.accept()
        actual = driver.current_url
        excepted = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/openAccount'
        assert actual == excepted



