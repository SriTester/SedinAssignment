import unittest
import allure
from Pages.Scenario1 import Scenario_1
from Pages.Scenario2 import Scenario_2
from Utitles.CustomLogger import customLogger as cl
import pytest


@pytest.mark.order(order = 2)
@allure.title ( """Test""" )
@allure.description ( """Test""" )
@allure.severity ( allure.severity_level.CRITICAL )
@pytest.mark.Smoke
@pytest.mark.usefixtures ( "startdriver", "log_on_failure" )
class Scenario_2_Pg ( unittest.TestCase ):

    @pytest.fixture ( autouse = True )
    def class_objects (self):
        self.wl = Scenario_1 (self.driver)
        self.pr = Scenario_2(self.driver)
        self.logs = cl ( )

    def test_scenario_2(self):
        allure.dynamic.title('=============Test-Case-002============')
        allure.description('Get all the product lists and check the particular product "Sauce Labs Bolt T-Shirt" is available.')
        self.logs.info("TEST CASE 002")
        self.logs.info("Login into website object has started")
        self.wl.loginintowebsite()
        self.logs.info("Login into website object has ended")
        self.logs.info("Products list to cart has started")
        self.pr.verifyproduct()