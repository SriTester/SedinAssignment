import time

import pytest
import allure
from Base.DriverClass import BaseClass
from ObjectsRepo.Objects_repo import objects_repo


class Scenario_4 (BaseClass):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    username = objects_repo.username
    password = objects_repo.password
    submit = objects_repo.submit
    Error_Message =objects_repo.Error_Message

    @allure.step
    def verifyloginerrormessage(self):
        self.openurl ( URL = "https://www.saucedemo.com" )
        self.maxwindow ( )
        self.Input ( locator = self.username, data = "ABV" )
        time.sleep ( 5 )
        self.Input ( locator = self.password, data = "XYZ" )
        time.sleep ( 5 )
        self.Click(locator = self.submit)
        self.verifymessage(self.Error_Message)