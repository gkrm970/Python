*** Settings ***
Documentation       Orange hrm test

Resource    ../../resources/all.resource


*** Test Cases ***
Test orange hrm login
    [Documentation]    Test the Dashboad text present in the page or not
    [Setup]    Organe HRM login
    Check page contain Dashboard keyword
    [Teardown]    Orange HRM logout
