


import win32com.client 


def fetch_surreylearn_emails():
    """
    Fetch unread emails from SurreyLearn and return a list of dictionaries:
    [{'student_name': ..., 'assignment_name': ..., 'course_offering': ...}, ...]
    """
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    inbox = outlook.GetDefaultFolder(6)  # 6 refers to the inbox
    messages = inbox.Items
    messages = messages.Restrict("[Unread] = true")


    emails = []


    for msg in messages:
        if msg.SenderEmailAddress.lower() == "surreylearnhelp@surrey.ac.uk":
            body = msg.body.splitlines()


            # parse the email body to extract relevant information
            try:
                student_name = [l for l in body if l.startswith("User:")][0].split(":")[1].strip()
                assignment_name = [l for l in body if l.startswith("Assignment:")][0].split(":")[1].strip()     
                course_offering = [l for l in body if l.startswith("Course Offering:")][0].split(":")[1].strip()


                emails.append({
                    "student_name": student_name,
                    "assignment_name": assignment_name,
                    "course_offering": course_offering,
                    "msg": msg
                })
            

            except IndexError:
                continue
    

    return emails


            