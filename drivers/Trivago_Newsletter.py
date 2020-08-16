from drivers.utils import history
from selenium.webdriver.common.by import By
from web.chrome_browser import Browser
from datetime import datetime
from random import randint


class NewsletterLocators(object):
    URL = "https://magazine.trivago.com"
    NEWSLETTER_SECTION = (By.XPATH, "//section[@class='newsletter newsletter-rover-2']")
    NEWSLETTER_EMAIL_INPUT = (By.XPATH, "//input[@placeholder='Your e-mail address']")
    NEWSLETTER_INSPIRE_ME = (By.XPATH, "//button[@class='submit']")
    NEWSLETTER_CHECKED_IN_STATUS = (By.XPATH, "//p[@class='submitted h1']")


class Newsletter(Browser):
    # Newsletter Actions
    # NAVIGATING TO THE URL
    def navigate(self):
        self.driver.get(NewsletterLocators.URL)

    # VERIFY THE NEWSLETTER SECTION
    def verify_newsletter_section(self):
        assert self.driver.find_element(*NewsletterLocators.NEWSLETTER_SECTION).is_displayed()

    # ENTER THE EMAIL INPUT IN NEWSLETTER
    def newsletter_email_input(self):
        assert self.driver.find_element(*NewsletterLocators.NEWSLETTER_EMAIL_INPUT).is_displayed()
        random_number = randint(100, 999)
        Email_usage = "abc" + str(random_number) + "@abc.com"
        self.driver.find_element(*NewsletterLocators.NEWSLETTER_EMAIL_INPUT).send_keys(Email_usage)
        history("INFO ------ Email used to subscribe the newsletter is " + str(Email_usage))

    # ENTER THE EMAIL INPUT IN NEWSLETTER
    def newsletter_inspire_me(self):
        assert self.driver.find_element(*NewsletterLocators.NEWSLETTER_INSPIRE_ME).is_displayed()
        self.driver.find_element(*NewsletterLocators.NEWSLETTER_INSPIRE_ME).click()

    def newsletter_verify_checked_in(self):
        str_checked_in = self.driver.find_element(*NewsletterLocators.NEWSLETTER_CHECKED_IN_STATUS).get_attribute("innerText")
        if str_checked_in == "You are now checked-in!":
            history("INFO ------" + "Newsletter successfully subscribed")