*** Settings ***
Library       ../../libraries/netbot_email.py

*** Keywords ***
Send netbot email
    [Documentation]    Send an email
    [Arguments]    ${access_token}
    send mail    Hi Gopalakrishna,<br/>Good Day.<br/> Test Mail.     gopalakrishna.rm@prodapt.com    ${access_token}
    Log    mail sent successfully