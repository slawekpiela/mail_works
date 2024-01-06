import email
import imaplib
import re
import requests

from configuration import sender_passwords, user_mail


def extract_email_address(raw_from):
    # Convert Header object to string, if necessary
    if isinstance(raw_from, email.header.Header):
        raw_from = str(raw_from)

    if raw_from is None:
        return None
    # Use regular expression to find text between < and >
    match = re.search(r'<(.+?)>', raw_from)
    if match:
        return match.group(1)

    return raw_from  # Return the original string if no match or raw_from is not None


def get_email_content(message):
    """Extract content from email message, focusing on plain text."""
    parts = []

    if message.is_multipart():
        for part in message.walk():
            # Check content type, skip if not text/plain
            if part.get_content_type() != 'text/plain':
                continue

            # Get the payload, skip if it's None
            payload = part.get_payload(decode=True)
            if payload is None:
                continue

            charset = part.get_content_charset()
            if charset is not None:
                try:
                    # Decode using the charset specified in the email
                    parts.append(payload.decode(charset))
                except UnicodeDecodeError:
                    # In case of decoding error, skip this part
                    continue
            else:
                # If no charset specified, try UTF-8 as a default
                try:
                    parts.append(payload.decode('utf-8'))
                except UnicodeDecodeError:
                    continue
    else:
        # If the message is not multipart, decode directly
        payload = message.get_payload(decode=True)
        if payload:
            try:
                # Attempt to decode with UTF-8
                parts.append(payload.decode('utf-8'))
            except UnicodeDecodeError:
                # Fallback to a different encoding, like ISO-8859-1
                parts.append(payload.decode('iso-8859-1'))

    return "\n".join(parts)


def fetch_all_emails():
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(user_mail, sender_passwords)

    status, mailboxes = mail.list()

    for mailbox in mailboxes:
        mailbox_name = mailbox.decode().split(' "/" ')[1].strip('"')
        if mailbox_name:
            print(f"Processing mailbox: {mailbox_name}")

            mail.select(f'"{mailbox_name}"', readonly=True)
            result, data = mail.search(None, 'ALL')
            email_ids = data[0].split()

            for email_id in email_ids:
                result, email_data = mail.fetch(email_id, '(RFC822)')
                raw_email = email_data[0][1]
                msg = email.message_from_bytes(raw_email)

                # Extract and print email addresses
                sender = extract_email_address(str(msg['from']))
                recipient = extract_email_address(str(msg['to']))

                print(f"Email ID: {email_id.decode()}")
                print(f"Sender: {sender}")
                print(f"Recipient: {recipient}")

                # Print all headers
                print("Email Headers:")
                for header in msg.items():
                    print(header)

                print("-" * 50)

# Call the function to fetch all emails
fetch_all_emails()