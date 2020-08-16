Feature: trivagoContactForm
    @contact_verify
    Scenario: Writing on ContactForm
        Given the user is on magazine.trivago.com
        When the user navigate to contact section
        Then new page opens with contact form