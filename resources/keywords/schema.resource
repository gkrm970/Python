*** Settings ***
Library    libraries.AuthLibrary
# Third-party
Library     RequestsLibrary
# Local
Resource    ../keywords/all.resource
# Variables
Resource    ../variables/all.resource


*** Keywords ***
List All Schemas Should Be Successful
    &{auth}    Get Auth Header
    ${response}    GET On Session    ${PUBSUB_SESSION}    schemas    headers=${auth}
    Should Be Equal As Integers    ${response.status_code}    200
    @{schemas}    Set Variable    ${response.json()["schemas"]}
    Log    List of schemas retrieved successfully
