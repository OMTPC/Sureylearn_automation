# SurreyLearn Email Automation

This project automates the collection of SurreyLearn assignment submission emails from Microsoft Outlook and parses them into structured data for further processing.

## Features
- Connects to Outlook via `win32com`.
- Fetches the 10 most recent unread assignment submission emails from the **SurreyLearn Submissions** subfolder.
- Parses useful metadata (submission ID, student details, course code, etc.).
- Logs results for verification before further processing.
- Designed to be safe: emails are not marked as read or moved automatically, allowing manual verification.

## Limitations
Due to server and Outlook permission restrictions:
- Emails are not automatically marked as read.
- Emails are not automatically moved into a "Processed" folder.  
Instead, the workflow is:
1. Run the script to process the 10 most recent emails.
2. Verify the results.
3. Manually move processed emails into another folder for archiving.

## Requirements
- Python 3.10+
- Microsoft Outlook (desktop client, with access to the mailbox)
- Windows OS (due to `pywin32` dependency)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/OMTPC/surreylearn-automation.git
   cd surreylearn-automation
