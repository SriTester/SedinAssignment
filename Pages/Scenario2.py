import time

import pytest
import allure
from Base.DriverClass import BaseClass
from ObjectsRepo.Objects_repo import objects_repo

class Scenario_2 (BaseClass):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    Products_list = objects_repo.Products_list

    @allure.step
    def verifyproduct(self):
        self.getlistandverify(self.Products_list,data = "Sauce Labs Bolt T-Shirt")
