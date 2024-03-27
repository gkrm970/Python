*** Settings ***
Library       ../libraries/netbot_email.py
Resource      all.resource

*** Keywords ***
Send netbot email
    [Documentation]    Send an email
    send mail    ${mail_content}   ${mail_to}   ${mail_to}
    Log    mail sent successfully