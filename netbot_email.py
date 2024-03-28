import json
import requests

# from robot.api.deco import keyword

access_token1 = ("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
                 ".eyJ1c2VyX25hbWUiOiJhbmdlbGluZS5hIiwic2NvcGUiOlsicmVhZCIsIndyaXRlIl0sInJvbGVzIjpbIm5ldGJvdHNfZ3Vlc3QiLCJuZXRib3RzX2FkbWluIiwibmV0Ym90c19hcHByb3ZlciIsIm5ldGJvdHNfcHJvZGFwdCJdLCJuYW1lIjoiQW5nZWxpbmUgU29waGlhIEEiLCJleHAiOjE3MTE1Njk0NTksImF1dGhvcml0aWVzIjpbIkFwcHJvdmVyIiwiQWRtaW4iLCJSZWFkIFdyaXRlIiwiUmVhZCBPbmx5Il0sImp0aSI6ImE2NGE5YWVjLWQwNmUtNDQ1MC1hYTI0LWM2NWI4NDM1ZjBlMCIsImVtYWlsIjoic29waGlhLmFAcHJvZGFwdC5jb20iLCJjbGllbnRfaWQiOiJhZG1pbiJ9.UcsAwNMqd6st04qpZUJv9_tAmAL4dUDsPTAAOBI5iRc")
mail_content1 = "Hi Gopalakrishna,<br/>Good Day to you from Netbot.<br/> Test Mail."


# @keyword
def send_mail(mail_content=mail_content1, mail_to="gopalakrishna.rm@prodapt.com ", access_token=access_token1):
    # Sends the mail to the given mails and respective mail content.
    try:
        mail_data = {
            "mailContent": mail_content,
            "to": mail_to,
            "cc": "",
            "Bcc": "",
            "testingRecipients": {"to": mail_to, "cc": "", "Bcc": ""},
            "entity": "IntakeMailTemplate.html",
            "subject": "Regarding netbot automation test",
            "file": [],
            # "file": "attachments_as_list"
        }
        headers = {
            "Content-Type": "application/json",
            "accept": "application/json",
            "Authorization": f"Bearer {access_token}"
        }
        mail_data = json.dumps(mail_data)

        response = requests.post(
            "http://10.168.170.180:8080/afService/mail/send/",
            headers=headers,
            data=mail_data,
            verify=False,
        )
        if response.status_code == 200:
            return f"response is {response},response.status_code is {response.status_code}"

        else:
            raise Exception(f"Failed At Sending Mail, Status_code: {response.status_code}, Error: {response.text}")


    except Exception as exc:
        raise Exception(
            f"Failed At Sending Mail, ERROR: {exc}"
        ) from exc


send_mail()


def check_and_reply_to_mails(access_token_for_mail=access_token1):
    # Use mail service API to get received emails (replace with actual API call)
    # get_received_emails api required
    # It can control only by internal mailing service
    received_emails = "get_received_emails"(access_token_for_mail)

    for email in received_emails:
        if "netbot" in email["subject"].lower():  # Check subject (case-insensitive)
            send_mail(f"Reply to netbot email , Hey you got email from net bot : ", mail_to="sender@example.com")

        elif "netbot" in email["body"].lower():
            # Send another email based on the reply content (replace with actual logic)
            send_mail(f"Reply to netbot email , Hey you  got email from net bot : ", mail_to="sender@example.com")
        else:
            print(f"Skipping email with subject: {email['subject']}")
            raise Exception(f"Skipping email with subject: {email['subject']}")


check_and_reply_to_mails()
