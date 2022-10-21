import Booking_Functionality.variables as var
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time


# So that the class can use the webdriver methods as well.
class Booking(webdriver.Chrome):
    def __int__(self, driver_path=r"C:\Users\Saifia\PycharmProjects\Selenium\chromedriver.exe", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ["PATH"] += self.driver_path
        # Creating an instance of Booking class as well.
        super(Booking, self).__init__()
        # This method will allow us to wait a certain amount of time
        # until the elements are loaded.
        self.implicitly_wait(15)

    def land_first_page(self):
        self.get(var.website_url)
        self.maximize_window()

    def check_the_selected_currency(self):
        element = self.find_element(By.CLASS_NAME, "bui-button__text")
        print(f"Selected Currency: {element.text[0:3]}")

    def change_the_currency(self, currency=None):
        element = self.find_element(By.CLASS_NAME, "bui-button__text")
        element.click()
        currency_element = self.find_element(By.XPATH, f"//a[@data-modal-header-async-url-param='changed_currency=1&"
                                                       f"selected_currency={currency}&top_currency=1']")
        currency_element.click()
        self.back()

    def check_the_selected_search_query(self):
        element = self.find_element(By.CLASS_NAME, "bui-tab__text")
        print(f"Selected Search Query: {element.text}")

    def change_the_search_query(self, search=None):
        print("Change the search query.")
        print("Default: Stays, Options: Flights, Car rentals (bookinggo), Attractions (attractions), "
              "Airport taxis (rideways)")
        element = self.find_element(By.XPATH, f"//a[@data-decider-header='{search}']")
        element.click()

    def choose_the_destination(self, destination=None):
        element = self.find_element(By.ID, "ss")
        element.clear()
        element.send_keys(destination)
        time.sleep(2)
        option = self.find_element(By.XPATH, "//li[@data-i='0']")
        option.click()
        time.sleep(1)

    def set_the_dates(self, check_in_date, check_out_date):
        check_in = self.find_element(By.XPATH, f"//td[@data-date='{check_in_date}']")
        check_in.click()
        check_out = self.find_element(By.XPATH, f"//td[@data-date='{check_out_date}']")
        check_out.click()
        time.sleep(2)
    
    def set_adults(self, number_of_adults):
        pass
    
