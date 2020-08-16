from web.chrome_browser import Browser
from drivers.Trivago_Newsletter import Newsletter
from drivers.Trivago_Contact import Contact


# before all will work before all the scenario
def before_all(context):
    context.chrome_browser = Browser()
    context.newsletter = Newsletter()
    context.contact = Contact()


# after all will work after all the scenario
def after_all(context):
    context.chrome_browser.close()
