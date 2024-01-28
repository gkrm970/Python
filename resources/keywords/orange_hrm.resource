*** Settings ***
Library    SeleniumLibrary
Library    XML

*** Keywords ***
Organe HRM login
    [Documentation]    trying
    Open Browser    https://opensource-demo.orangehrmlive.com/web/index.php/auth/login    edge
    Maximize Browser Window
    Sleep    5

#    login credentials
    ${username_locator}    Set Variable    xpath://input[@placeholder='Username']
    Clear Element Text    ${username_locator}
    Input Text    ${username_locator}    Admin
    ${password_locator}    Set Variable    xpath://input[@placeholder='Password']
    Clear Element Text    ${password_locator}
    Input Text    ${password_locator}    admin123
    Click Button    xpath://button[contains(.,'Login')]



Orange HRM logout
    [Documentation]    orange hrm logout process
    Log To Console    trying to logout
    ${logout}    Set Variable    xpath://a[normalize-space()='Logout']
    ${_logout_text}=   Get Text    ${logout}
    Log To Console    _logout_text is{_logout_text}
    Click Link    ${logout}
    Sleep    10

Check page contain Dashboard keyword
    [Documentation]    Checking the page contain Dashboard keyword present or not.
    ${dashboard}    Set Variable    xpath://h6[normalize-space()='Dashboard']
    Wait Until Element Is Visible    ${dashboard}
    Wait Until Element Is Visible    ${dashboard}

    ${dashborad_text}=    Get Text    ${dashboard}
    Log To Console    get text is ${dashborad_text}
#    Element Text Should Be    ${dashboard}    Dashboard
    SeleniumLibrary.Element Text Should Be    ${dashboard}    Dashboard
    Page Should Contain Element    ${dashboard}
    Log To Console    dashboard is ${dashboard}
    Sleep    5
    ${get_text}=    Get Text    xpath://span[@class='oxd-userdropdown-tab']
    Log To Console    ${get_text}
    Click Element    xpath://span[@class='oxd-userdropdown-tab']
    Sleep    10
