import unittest
import allure
from Pages.Scenario1 import Scenario_1
from Utitles.CustomLogger import customLogger as cl
import pytest


@pytest.mark.order ( order = 1)
@allure.title ( """Test""" )
@allure.description ( """Test""" )
@allure.severity ( allure.severity_level.CRITICAL )
@pytest.mark.Smoke
@pytest.mark.usefixtures ( "startdriver", "log_on_failure" )
class Scenario_1_Pg ( unittest.TestCase ):


    @pytest.fixture ( autouse = True )
    def class_objects (self):
        self.wl = Scenario_1 (self.driver)
        self.logs = cl ( )

    def test_scenario_1(self):
        allure.dynamic.title ( 'Test-Case-001' )
        allure.description('Checkout and validate the product details whether you are ordered the correct product')
        self.logs.info("===========TEST CASE 001============")
        self.logs.info("Login into website object has started")
        self.wl.loginintowebsite()
        self.logs.info ( "Login into website object has ended" )
        self.logs.info("add product to cart has started")
        self.wl.addproducttocart()
        self.logs.info ( "add product to cart has ended" )