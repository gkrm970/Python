*** Settings ***
# Third-party
Library     RequestsLibrary
# Local
Resource    all.resource
# Variables
Resource    all.resource


*** Keywords ***
Create Pubsub Session
    Create Session    ${PUBSUB_SESSION}    ${BASE_URL}
