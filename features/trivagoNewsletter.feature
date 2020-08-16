Feature: trivagoNewsletter
    @subscribe
    Scenario: Subscribe to Newsletter
        Given the user is on magazine.trivago.com
        When the user navigate to newsletter section
        Then user enters the mail id and click on Inspire me and verify the subscription is successful