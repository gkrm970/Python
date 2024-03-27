*** Settings ***
Library   ../libraries/email_.py
Resource      variables_xpath.robot

*** Keywords ***
Sending an email
    [Documentation]    Going send an email
    send email       ${subject}      ${body}    ${receiver_email}
    Log    mail sent successfully

