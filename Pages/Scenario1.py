import time

import pytest
import allure
from Base.DriverClass import BaseClass
from ObjectsRepo.Objects_repo import objects_repo


class Scenario_1 (BaseClass):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    username= objects_repo.username
    password=objects_repo.password
    submit =objects_repo.submit
    product_add = objects_repo.product_add
    Cart_Value = objects_repo.Cart_Value
    Cart_Check_Product_Check =objects_repo.Cart_Check_Product_Check
    Cart_Checkout_Button = objects_repo.Cart_Checkout_Button
    Product_Cart_Added = objects_repo.Product_Cart_Added

    @allure.step
    def loginintowebsite(self):
        self.openurl(URL = "https://www.saucedemo.com")
        self.maxwindow()
        self.Input(locator = self.username,data ="standard_user" )
        time.sleep(2)
        self.Input(locator = self.password,data = "secret_sauce")
        time.sleep (2)
        self.Click(self.submit)
        time.sleep (2)

    @allure.step
    def addproducttocart(self):
        self.productadd(locator = self.product_add,data = 'Sauce Labs Backpack')
        time.sleep (2)
        self.verifyvalue(locator = self.Cart_Value,data = '1')
        time.sleep(2)
        self.Click(locator = self.Cart_Value)
        time.sleep(2)
        self.verifyvalue(locator = self.Product_Cart_Added,data = 'Sauce Labs Backpack')