*** Settings ***
Documentation    Test email
Resource        ../../resources/all.resource


*** Test Cases ***
Test Netbot Email
    [Documentation]    Test email sending with Robot Framework
    Send netbot email
    Log    mail sent successfully