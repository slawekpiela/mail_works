# mail_works

This project provides modules to:
a) pull emails from email account and store in airbase table:
- - mail ID
  - sender
    recepient
  - subject
  - body (text only)
  
b) place same emails in a txt file to make inference easier

c) run query on each email with specified purpose and send SMS if inference criterion is met

d) periodically summarise emails and sent summary to predefined email

e) inference will be run concurently with GPT3.5 and a local model (or models). 
    results will be logged


