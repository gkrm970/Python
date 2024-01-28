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
    ${dashboard}=    Page Should Contain    xpath://*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span/h6
    Log To Console    dashboard is ${dashboard}
    Sleep    5
    Close Browser


Orange HRM logout
    [Documentation]    orange hrm logout process
    Log To Console    trying to logout
    Click Image    xpath://p[@class='oxd-userdropdown-name'] /ancestor::li
    Sleep    10
#    Click Link    xpath://a[contains(text(),'Logout')]
