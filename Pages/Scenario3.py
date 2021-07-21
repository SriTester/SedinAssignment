import time

import pytest
import allure
from Base.DriverClass import BaseClass
from ObjectsRepo.Objects_repo import objects_repo


class Scenario_3(BaseClass):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    Back_to_products=objects_repo.Back_to_products
    Products_details_price=objects_repo.Products_details_price
    Product_Cart_Added=objects_repo.Product_Cart_Added
    Product_Prices=objects_repo.Product_Prices
    Product_Particular_Name= objects_repo.Product_Particular_Name

    @allure.step
    def verifyproductvalues(self):
        try:
            time.sleep(5)
            Prices=self.getpriceandremovedollar(locator = self.Product_Prices)
            Elements=self.driver.find_elements_by_xpath(xpath = self.Product_Prices)
            for price,ele in enumerate(Elements,start = 0):
                if ele.text == Prices[price]:
                    self.logs.info("Price item is available and {}".format(Prices[price]))
                else:
                    self.logs.info("Price item is not available {}".format(Prices[price]))
        except Exception as e:
            self.logs.info("Problem in verifyproductvalues method {}".format(e))

    @allure.step
    def verifyproductdetailspage(self):
        try:
            Prices = self.getpriceandremovedollar ( locator = self.Product_Prices )
            products_name = self.driver.find_elements_by_xpath ( xpath = self.Product_Cart_Added)
            products_name_list = [ele.text for ele in products_name]
            self.logs.info(products_name_list)
            for ele in range(0,len(products_name_list)):
                self.clickonparameterizedfield(locator = self.Product_Particular_Name,data = products_name_list[ele])
                Prices_details=self.driver.find_element_by_xpath(xpath = self.Products_details_price).text
                self.Click ( self.Back_to_products )
                time.sleep(5)
                assert Prices_details != Prices[ele],"Price is equal"
        except Exception as e:
            self.logs.error("Problem with verifyproductdetails page {}".format(e))
