from behave import *
import time


@given('the user is on magazine.trivago.com')
def step_impl(context):
    context.newsletter.navigate()
    time.sleep(3)


@when('the user navigate to newsletter section')
def step_impl(context):
    context.newsletter.verify_newsletter_section()
    time.sleep(3)


@then('user enters the mail id and click on Inspire me and verify the subscription is successful')
def step_impl(context):
    context.newsletter.newsletter_email_input()
    time.sleep(3)
    context.newsletter.newsletter_inspire_me()
    time.sleep(3)
    context.newsletter.newsletter_verify_checked_in()
