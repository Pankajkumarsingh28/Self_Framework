from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select

# Here we have Element locators of QA Click Acdemy.
driver=Chrome("C://Users//nirup//Desktop//Python//chromedriver.exe")
Radio_button="//input[@value='radio2']"
Drop_down_select="//select[@id='dropdown-class-example']"
Check_box="checkBoxOption2"


class OperationOnQAclickAcdemy():
    def OpenBrowser(self=None):
        # driver=Chrome("C://Users//pankaj_kumar4//OneDrive - S&P Global//Desktop//Chrome Driver//chromedriver_win32//chromedriver.exe")
        url="https://www.rahulshettyacademy.com/AutomationPractice/"
        driver.get(url)
        driver.set_page_load_timeout(20)
        driver.maximize_window()

    # This is for radio Button Selection
    def clickOnRadioButton(self=None):
        driver.find_element_by_xpath(Radio_button).click()

    #This is for drop down selection using select class.
    def selectDropdown(self=None):
        obj1=Select(driver.find_element_by_xpath(Drop_down_select))
        obj1.select_by_index(3)

    #This is for Checkbox selection.
    def Checkbox(self=None):
        driver.find_element_by_id(Check_box).click()




    def CloseBroswser(self=None):
        driver.quit()

