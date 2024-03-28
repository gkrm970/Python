*** Settings ***
Library     netbot_email.py

*** Variables ***

*** Test Cases ***
Test sending an email throught netbot
    [Documentation]    Test sending an email throught netbot
    send mail    Hi Gopalakrishna,<br/>Good Day.<br/> Test Mail.     gopalakrishna.rm@prodapt.com    eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiJhbmdlbGluZS5hIiwic2NvcGUiOlsicmVhZCIsIndyaXRlIl0sInJvbGVzIjpbIm5ldGJvdHNfZ3Vlc3QiLCJuZXRib3RzX2FkbWluIiwibmV0Ym90c19hcHByb3ZlciIsIm5ldGJvdHNfcHJvZGFwdCJdLCJuYW1lIjoiQW5nZWxpbmUgU29waGlhIEEiLCJleHAiOjE3MTE1Njk0NTksImF1dGhvcml0aWVzIjpbIkFwcHJvdmVyIiwiQWRtaW4iLCJSZWFkIFdyaXRlIiwiUmVhZCBPbmx5Il0sImp0aSI6ImE2NGE5YWVjLWQwNmUtNDQ1MC1hYTI0LWM2NWI4NDM1ZjBlMCIsImVtYWlsIjoic29waGlhLmFAcHJvZGFwdC5jb20iLCJjbGllbnRfaWQiOiJhZG1pbiJ9.UcsAwNMqd6st04qpZUJv9_tAmAL4dUDsPTAAOBI5iRc
    Log    mail sent successfully

Test replaying to an email throught netbot
    [Documentation]    Test replaying to an email throught netbot
