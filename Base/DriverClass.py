import time

import allure
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

from Utitles import CustomLogger as cl
product_Added=0

class BaseClass:
    logs = cl.customLogger ( )

    def __init__ (self, driver):
        self.driver = driver

    @allure.step
    def Click (self, locator, data=None):
        try:
            Element_status = self.isElementpresent ( locator )
            if not Element_status == "False":
                Element_status.click ( )
                self.logs.info ( "Element has been clicked successfully" )
            else:
                raise ElementClickInterceptedException
        except Exception as e:
            self.logs.info ( "Cannot be able to click on given element {}".format ( locator ) )
            self.logs.error ( e )

    @allure.step
    def isElementpresent (self, locator,duration =1):
        global Element_Status
        self.logs.info ( "Beginning of is Element present keyword" )
        try:
            Element_Status = self.driver.find_element_by_xpath ( locator )
            original_style= Element_Status.get_attribute('style')
            self.driver.execute_script("arguments[0].setAttribute('style',arguments[1]);",Element_Status,"background:white;color:Red;border:4px dotted red;")
            if duration>0:
                time.sleep(duration)
                self.driver.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])",Element_Status,"style",original_style)
                return Element_Status
        except NoSuchElementException:
            self.logs.info ( "Element is not found {}".format ( locator ) )
            return "False"

    def openurl (self, URL):
        self.logs.info ( "Beginning of open url keyword" )
        try:
            self.driver.get ( URL )
            self.logs.info ( "Successfully Opened URL ---> {}".format ( URL ) )
        except Exception as e:
            self.logs.info ( "There is problem in opening the URL ==={}".format ( e ) )

    @allure.step
    def Input (self, locator, data):
        global Element_Input
        self.logs.info ( "Beginning of Input Keyword" )
        try:
            Element_Input = self.isElementpresent ( locator )
            if not Element_Input == "False":
                Element_Input.send_keys ( data )
                self.logs.info ( "Data has been inserted successfully" )
            else:
                raise NoSuchElementException
        except Exception as e:
            self.logs.error ( "There is no element with given locator {}".format ( e ) )

    @allure.step
    def maxwindow (self):
        self.logs.info ( "Beginning of Max Window Keyword" )
        try:
            self.driver.maximize_window ( )
        except Exception as e:
            self.logs.error ( e )

    @allure.step
    def productadd(self,locator,data):
        global product_Added
        self.logs.info("Beginning of product add keyword")
        try:
            replacement_expression = locator.replace('{0}',data)
            Element_Status = self.isElementpresent(replacement_expression)
            if not Element_Status == "False":
                self.Click(replacement_expression)
                product_Added +=1
            else:
                raise NoSuchElementException
        except Exception as e:
            self.logs.info("There is no such element --> {} --> {}".format(locator,e))

    @allure.step
    def verifyvalue(self,locator,data):
        self.logs.info("Beginning of cartvalue keyword")
        try:
            Element_status = self.isElementpresent(locator)
            if not Element_status =='False':
                carts_Value=Element_status.text
                assert carts_Value==data, "Your Value and Cart_Value is not matching"
        except AssertionError as e:
            self.logs.info("Problem in verifycartvalue keyword --> {}".format(e))

    @allure.step
    def getlistandverify(self,locator,data):
        self.logs.info("Beginning of getlistandverify keyword")
        try:
            Element_list = self.driver.find_elements_by_xpath(locator)
            for ele in Element_list:
                if ele.text == data:
                    self.logs.info("Your desired Element is there in the list {}".format(ele.text))
                else:
                    self.logs.info("Your searching element is not there in the list {}".format(ele.text))
        except Exception as e:
            self.logs.error("Problem in the keyword {}".format(e))

    @allure.step
    def verifymessage(self,locator):
        self.logs.info("Beginning of verifymessage keyword")
        try:
            Element_Status = self.isElementpresent(locator)
            if not Element_Status == "False":
                self.logs.info("Validation message is displayed")
            else:
                raise NoSuchElementException
        except Exception as e:
            self.logs.info("No Such Element Exception {}".format(e))

    @allure.step
    def getpriceandremovedollar(self,locator):
        prices =[]
        self.logs.info("Beginning of getpriceandremovedollar")
        try:
            Element_Stat = self.driver.find_elements_by_xpath( locator )
            for ele in Element_Stat:
                prices_list = ele.text
                final_Value = prices_list.replace('$','')
                prices.append(final_Value)
            return prices
        except Exception as e:
            self.logs.info("Problem in getpriceandremovedollar {}".format(e))

    @allure.step
    def clickonparameterizedfield(self,locator,data):
        self.logs.error("Beginning of clickonparameterized field keyword")
        try:
            self.logs.info("Before Changing Expression {}".format(locator))
            Change_Expression = locator.replace('{0}',data)
            self.logs.info("After Changing the Expression {}".format(Change_Expression))
            Element_Status = self.isElementpresent(Change_Expression)
            if not Element_Status == 'False':
                self.Click(Change_Expression)
            else:
                raise ElementClickInterceptedException
        except Exception as e:
            self.logs.info("Problem in clickonparameterizedfield {}".format(e))


