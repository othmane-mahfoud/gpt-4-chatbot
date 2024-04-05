from openai import OpenAI

from dotenv import dotenv_values

config = dotenv_values(".env")

api_key = config["OPENAI_API_KEY"]

client = OpenAI(api_key = api_key)

messages = []

while True:
    try:
        user_input = input("You: ")
        messages.append({"role": "user", "content": user_input})
        res = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        reply = {"role": "assistant", "content": res.choices[0].message.content}
        messages.append(reply)
        print("Assistant: " + res.choices[0].message.content)

    except KeyboardInterrupt:
        print("End of conversation .. Goodbye!")
        break