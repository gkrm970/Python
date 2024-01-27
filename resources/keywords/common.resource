*** Settings ***
# Third-party
Library     RequestsLibrary
# Local
Resource    resources/keywords/all.resource
# Variables
Resource    resources/variables/all.resource


*** Keywords ***
Create Pubsub Session
    Create Session    ${PUBSUB_SESSION}    ${BASE_URL}
