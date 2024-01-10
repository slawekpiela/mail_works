import string
import time
import os
from openai import OpenAI

from configuration import api_key, assistant_id, assistant_id3, assistant_id4, Models

# Assuming other configurations (api_key, etc.) are set correctly

client = OpenAI(api_key=api_key)

def query_model(prompt, instructions, assistant, thread_id=None):
    print("Thread ID provided to query_model: ", thread_id)

    try:
        # Check if a thread ID is provided, else create a new thread
        if thread_id is None:
            thread = client.beta.threads.create()
            thread_id = thread.id
            # Send initial prompt as a message if it's a new thread
            client.beta.threads.messages.create(
                thread_id=thread_id,
                role="user",
                content=prompt
            )
        else:
            # If a thread ID is provided, use it without creating a new thread
            thread_id = thread_id

        # Create a run
        run = client.beta.threads.runs.create(
            thread_id=thread_id,
            assistant_id=assistant,
            instructions=instructions
            # tools=[{"type": "retrieval"}]  # Uncomment if needed
        )

        # Wait for the run to complete
        status = "start"
        count = 0
        while status != "completed":
            result = client.beta.threads.runs.retrieve(
                thread_id=thread_id,
                run_id=run.id
            )
            status = result.status
            print("\rStatus: ", status, count, end="")  # Print current status
            count += 1
            time.sleep(1)

        # Retrieve messages after run is complete
        messages = client.beta.threads.messages.list(thread_id=thread_id)

        result_text = messages.data[0].content[0].text.value  # Extract text from completion
        full_result = messages
        print("Thread ID returned by query_model: ", thread_id)
        return result_text, full_result, thread_id

    except Exception as e:
        print("Error in query_model:", e)
        return None, None, None

# Usage example
result, full_result, new_thread_id = query_model("Your prompt here", "Your instructions here", assistant_id, None)
