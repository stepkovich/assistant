import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from datetime import datetime


async def chat_answer(response, ids):
    load_dotenv()
    start = datetime.now()
    client = AsyncOpenAI(
        api_key=os.getenv("API_KEY"))

    assist_id = os.getenv('ID_ASSIST')
    topic = await client.beta.threads.create()
    message = await client.beta.threads.messages.create(
        thread_id=ids,
        role="user",
        content=response
    )

    run = await client.beta.threads.runs.create_and_poll(
        thread_id=ids,
        assistant_id=assist_id,
    )

    thread_messages = await client.beta.threads.messages.list(ids)
    run = await client.beta.threads.runs.create_and_poll(
        thread_id=ids,
        assistant_id=assist_id,
    )

    return (f'{thread_messages.data[0].content[0].text.value.strip()}\n\n'
            f'время выполнения запроса: {datetime.now() - start}')
