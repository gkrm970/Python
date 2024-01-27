*** Settings ***
Documentation       Schema API Sanity Tests

Resource    ../../resources/all.resource


*** Test Cases ***
List All Schemas
    [Setup]    Create Pubsub Session
    List All Schemas Should Be Successful
    [Teardown]    Delete All Sessions

Test git hub login
    Git hub login
