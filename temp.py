import string
import time
import os
from openai import OpenAI

from configuration import api_key, assistant_id, assistant_id3, assistant_id4, Models

api_key = api_key
# form env
# api_key = os.getenv('api_key')
# assistant_id = os.getenv('assistant_id'),
# assistant_id3 = os.getenv('assistant_id3'),
# assistant_id4 = os.getenv('assistant_id4'),

client = OpenAI(api_key=api_key)


# thread = client.beta.threads.create()


def query_model(prompt, instructions, assistent, thread):
    print("tki wątek podano do query model: ",thread)

    try:
        thread = client.beta.threads.create()

        message = client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=prompt
        )
    except:
        thread_messages = client.beta.threads.messages.list(thread)

    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistent,
        instructions=instructions

        # tools=[{"type": "retrieval"}]
    )
    print("\n a to jest thread.id: ",thread.id)
    status = "start"
    count = 0
    print("\n")
    while status != "completed":
        result = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )
        status = result.status
        print("\rStatus: ", status, count, end="")  # "Status",count, result.status, end="\r")  # print current status
        count = count + 1
        time.sleep(1)

    messages = client.beta.threads.messages.list(thread_id=thread.id)  # ststus is complete. get completion

    result = messages.data[0].content[0].text.value  # extract text from cpmpletion
    full_result = messages
    print("taki watek qm zwraca: ", thread.id)
    return result, full_result, thread.id
