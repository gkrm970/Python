*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Git hub login
    [Documentation]    trying
    Open Browser    https://github.com/login    chrome
    Maximize Browser Window
    Sleep    5