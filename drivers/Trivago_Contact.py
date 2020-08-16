from drivers.utils import history
from selenium.webdriver.common.by import By
from web.chrome_browser import Browser


class ContactLocators(object):
    URL = "https://magazine.trivago.com"
    CONTACT = (By.XPATH, "//a[contains(text(),'Contact')]")
    MESSAGE_INPUT = (By.XPATH, "//textarea[@class='contact-msg']")
    FULLNAME = (By.XPATH, "//div[contains(text(),'Full Name')]]")


class Contact(Browser):
    # Contact Actions
    # CLICK THE CONTACT SECTION
    def contact_link(self):
        assert self.driver.find_element(*ContactLocators.CONTACT).is_displayed()
        self.driver.find_element(*ContactLocators.CONTACT).click()

    # VERIFY THE CONTACT PAGE
    def verify_contactform(self):
        assert self.driver.find_element(*ContactLocators.MESSAGE_INPUT).is_displayed()
        history("INFO ------ Contact form is verified successfully")

    # ENTER THE MESSAGE INPUT IN CONTACT FORM
    def message_input(self):
        assert self.driver.find_element(*ContactLocators.MESSAGE_INPUT).is_displayed()
        self.driver.find_element(*ContactLocators.MESSAGE_INPUT).send_keys("This is Automation using "
                                                                           "Behave BDD Framework")

    # ENTER THE FULLNAME INPUT IN CONTACT FORM
    def fullname_input(self):
        assert self.driver.find_element(*ContactLocators.FULLNAME).is_displayed()
        self.driver.find_element(*ContactLocators.FULLNAME).click()

    def newsletter_verify_checked_in(self):
        str_checked_in = self.driver.find_element(*ContactLocators.NEWSLETTER_CHECKED_IN_STATUS).get_attribute("innerText")
        if str_checked_in == "You are now checked-in!":
            history("INFO ------" + "Newsletter successfully subscribed")
