from behave import *
import time


@when('the user navigate to contact section')
def step_impl(context):
    context.contact.contact_link()
    time.sleep(3)


@then('new page opens with contact form')
def step_impl(context):
    context.contact.verify_contactform()