import time
import os
from openai import OpenAI
#from configuration import api_key, assistant_id, assistant_id3, assistant_id4, Models

#form env
api_key = os.getenv('api_key')
assistant_id = os.getenv('assistant_id'),
assistant_id3 = str(os.getenv('assistant_id3')),
assistant_id4 = os.getenv('assistant_id4'),


client = OpenAI(api_key=api_key)
print ("start query")
thread = client.beta.threads.create()

def query_model(prompt, instructions):
    #thread = client.beta.threads.create()
    print(assistant_id, assistant_id3, assistant_id4)
    print(thread)
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=prompt
    )

    thread_messages = client.beta.threads.messages.list(thread.id)

    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant_id,
        instructions=instructions

        #tools=[{"type": "retrieval"}]
    )

    status = "start"
    count=0
    print("\n")
    while status != "completed":
     result = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
     )
     status=result.status
     print("\rStatus: ",status, count, end="") #"Status",count, result.status, end="\r")  # print current status
     count=count+1
     time.sleep(1)

    messages = client.beta.threads.messages.list(thread_id=thread.id) # ststus is complete. get completion

    result= messages.data[0].content[0].text.value # extract text from cpmpletion
    full_result= messages

    return result, full_result, thread




