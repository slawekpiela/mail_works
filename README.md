# mail_works

This project provides modules to:
a) pull emails from email account and store in airbase table:
  - mail ID
  - date/time
  - sender
  - recipient
  - subject
  - body (text only)
  
b) place the same emails in a txt file to make inference easier

c) run query on each email with specified purpose and send SMS if inference criterion is met

d) periodically summarise emails for a given period of time and send summary to predefined email

e) inference will be run concurently with GPT3.5 and a local model (or models). 
    results will be logged
d) all inference done from the webpage level


