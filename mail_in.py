import email
import imaplib
import re
import requests

from configuration import sender_passwords, user_mailin


def extract_email_address(raw_from):
    # Use regular expression to find text between < and >
    match = re.search(r'<(.+?)>', raw_from)
    if match:
        return match.group(1)

    return None


def get_email_content(message):
    """Extract content from email message."""
    parts = []
    for part in message.walk():
        # Check if part is an attachment
        if "attachment" in str(part.get("Content-Disposition")):
            continue

        # Get the payload, skip if it's None
        payload = part.get_payload(decode=True)
        if payload is None:
            continue

        # Decode and append the payload
        parts.append(payload.decode())

    return "\n".join(parts)


def fetch_mail_content_and_sender():
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(user_mailin, sender_passwords)
    mail.select('inbox')

    result, data = mail.search(None, '(UNSEEN SUBJECT "Ask Koios AI")')
    email_ids = data[0].split()

    if email_ids:
        # Sort the email IDs and get the latest one
        latest_email_id = sorted(email_ids, key=int)[-1]

        # Fetch the latest email
        result, email_data = mail.fetch(latest_email_id, '(RFC822)')
        raw_email = email_data[0][1]
        msg = email.message_from_bytes(raw_email)

        # Extract relevant information
        sender = extract_email_address(msg['from'])
        subject = msg['subject']
        # Assuming you have a function to extract content
        content = get_email_content(msg)

        return sender, content
    else:
        return None

    # to nigdy nie zostanie wywołane, martwy kod
    print("from: ", sender, " content in the emial: ", content)
    mail.logout()
    print("emails: ", emails)
    return emails
# print("mail in as this:")
# print(fetch_mail_content_and_sender())
