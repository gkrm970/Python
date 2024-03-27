import json
import requests
from robot.api.deco import keyword


@keyword
def send_mail(mail_content, mail_to):
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
            "Authorization": f"Bearer access_token"
        }
        mail_data = json.dumps(mail_data)

        response = requests.post(
            "send_mail_url",
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
