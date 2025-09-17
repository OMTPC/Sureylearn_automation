import win32com.client

# def fetch_surreylearn_emails(limit=50):
#     """
#     Fetch SurreyLearn assignment emails from inbox.
#     """
#     outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
#     inbox = outlook.GetDefaultFolder(6)
#     messages = inbox.Items
#     messages.Sort("[ReceivedTime]", True)

#     emails = []
#     count = 0

#     for msg in messages:
#         if msg.Class != 43:  # only MailItem
#             continue

#         count += 1
#         if count > limit:
#             break

#         sender = getattr(msg, "SenderName", "").lower()
#         subject = getattr(msg, "Subject", "").lower()

#         if "surreylearn notifications" in sender and "assignment submission" in subject:
#             emails.append(msg)

#     return emails


# def fetch_surreylearn_emails(limit=10):
#     outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
#     inbox = outlook.GetDefaultFolder(6)
#     messages = inbox.Items

#     emails = []

#     for msg in messages:
#         # TEMP: fetch all messages, don’t filter sender yet
#         emails.append(msg)
#         if len(emails) >= limit:
#             break

#     return emails


# import win32com.client

def fetch_surreylearn_emails(limit=10):
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    inbox = outlook.GetDefaultFolder(6)
    messages = inbox.Items

    emails = []

    for msg in messages:
        if "SurreyLearn Notifications" in msg.SenderName and msg.Subject.startswith("Assignment Submission:"):
            emails.append(msg)
            if len(emails) >= limit:
                break

    return emails
