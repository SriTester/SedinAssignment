import unittest
import allure
from Pages.Scenario4 import Scenario_4
from Utitles.CustomLogger import customLogger as cl
import pytest


@pytest.mark.order ( order = 4 )
@allure.title ( """Test""" )
@allure.description ( """Test""" )
@allure.severity ( allure.severity_level.CRITICAL )
@pytest.mark.Smoke
@pytest.mark.usefixtures ( "startdriver", "log_on_failure" )
class Scenario_4_Pg ( unittest.TestCase ):


    @pytest.fixture ( autouse = True )
    def class_objects (self):
        self.wl = Scenario_4 (self.driver)
        self.logs = cl ( )

    def test_scenario_4(self):
        allure.dynamic.title ( '=========Test-Case-004==========' )
        allure.description('Validate the error message')
        self.logs.info("TEST CASE 004")
        self.logs.info("Veriy validation message object has started")
        self.wl.verifyloginerrormessage()
        self.logs.info("Verify Validation message object has ended")