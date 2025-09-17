


import win32com.client

def test_inbox_access(limit=10):
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    inbox = outlook.GetDefaultFolder(6)  # 6 = Inbox

    messages = inbox.Items
    messages.Sort("[ReceivedTime]", True)  # newest first

    print(f"Total messages in inbox: {messages.Count}\n")
    print(f"Showing first {limit} messages:\n")

    count = 0
    for msg in messages:
        count += 1
        if count > limit:
            break

        # Only process MailItem
        if msg.Class != 43:  # 43 = olMail
            continue

        sender = getattr(msg, "SenderName", "<unknown>")
        subject = getattr(msg, "Subject", "<no subject>")
        print(f"{count}. From: {sender} | Subject: {subject}")

if __name__ == "__main__":
    test_inbox_access()
