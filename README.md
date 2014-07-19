### snipplrbak.py

**Description:**
Python script which connects to [Snipplr](www.snipplr.com) via your API key. Creates a text file in format YYYY-MM-DD_snipplrbak.txt. For each item on in your Snipplr, it outputs: Title, Language, Source and fills with your data from Snipplr. Creates a log of when last backup was pulled called baklog.txt

**Requirements:**
Python 2.7

**Directions:**
Edit the script (Each line which requires a change has a `#USER SPECIFIC` comment line):

1) Choose directory where you want to store the snipplr backups.  
2) Replace yourUniqueAPIKeyGoesHere with your API Key from Snipplr  
3) Choose directory where you want the backlog.txt file to go.

Either run manually or create a Cron job or other automated job for snipplrbak.py

**Limitations:**
baklog.txt is the only "error reporting" at this time.
