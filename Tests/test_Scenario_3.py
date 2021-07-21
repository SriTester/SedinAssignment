import unittest
import allure
from Pages.Scenario1 import Scenario_1
from Pages.Scenario3 import Scenario_3
from Utitles.CustomLogger import customLogger as cl
import pytest


@pytest.mark.order ( order = 3)
@allure.title ( """Test""" )
@allure.description ( """Test""" )
@allure.severity ( allure.severity_level.CRITICAL )
@pytest.mark.Smoke
@pytest.mark.usefixtures ( "startdriver", "log_on_failure" )
class Scenario_3_Pg ( unittest.TestCase ):


    @pytest.fixture ( autouse = True )
    def class_objects (self):
        self.wl = Scenario_3(self.driver)
        self.s1 = Scenario_1(self.driver)
        self.logs = cl ( )

    def test_scenario_3(self):
        allure.dynamic.title ( '==========Test-Case-003========' )
        allure.description('Validate the price with product listing with product individual page (which will be displayed if you click the product name')
        self.logs.info("TEST CASE 003")
        self.logs.info("Login into website object has started")
        self.s1.loginintowebsite()
        self.logs.info ( "Login into website object has ended" )
        self.logs.info("Verifyproductvalues has started")
        self.wl.verifyproductvalues()
        self.logs.info ( "Verifyproductvalues has ended" )
        self.logs.info("Verifyproductdetails page has started")
        self.wl.verifyproductdetailspage()
        self.logs.info("Verify product details page has ended")