


import imaplib
import email        
import logging 
from src.config import EMAIL_ADDRESS, EMAIL_PASSWORD, IMAP_SERVER, IMAP_PORT, MAIL_FOLDER


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def connect_to_mailbox():
    """
    Connect to the IMAP server and select the mailbox.
    Returns the IMAP connection object.
    """
    try:
        logging.info("Connecting to IMAP server %s...", IMAP_SERVER)
        mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
        mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        logging.info("Connected to mailbox successfully.")
        mail.select(MAIL_FOLDER)
        logging.info("Mailbox '$s' selected", MAIL_FOLDER)
        return mail
    
    except Exception as e:
        logging.error(f"Failed to connect to IMAP server: %s: {e}")
        return None
    

def fetch_unread_messages(mail, sender_filter=None):
    """
    Fetch unread emails optionally filtered by sender.
    Returns a list of email.message.Message objects.
    """
    if mail is None:
        logging.error("IMAP connection is None")
        return []
    
    # build search criterion
    criteria = ["UNSEEN"] # unread emails only
    if sender_filter:
        criteria.append(f'FROM "{sender_filter}"')

    search_criteria = ' '.join(criteria)
    logging.info("Searching for emails with criteria: %s", search_criteria)

    result, data = mail.search(None, *criteria)
    if result != 'OK':
        logging.error("Failed to search emails: %s", result)
        return []
    
    message = []
    for num in data[0].split():
        result, msg_data = mail.fetch(num, '(RFC822)')
        if result != 'OK':
            logging.warning("Failed to fetch message %s", num)
            continue
        
        msg = email.message_from_bytes(msg_data[0][1])
        message.append(msg)

    logging.info("Fetched %d message", len(message))
    return message

if __name__ == "__main__":
    mail = connect_to_mailbox()
    if mail:
        msgs = fetch_unread_messages(mail, sender_filter="surreylearnhelp@surrey.ac.uk")
        print(f"Number of unread messages from SurreyLearn: {len(msgs)}")


