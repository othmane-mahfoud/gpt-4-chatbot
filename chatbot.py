from openai import OpenAI
from dotenv import dotenv_values
import argparse

config = dotenv_values(".env")
api_key = config["OPENAI_API_KEY"]

client = OpenAI(api_key = api_key)

def main():
    parser = argparse.ArgumentParser(description="Simple command line chatbot with GPT-4")
    parser.add_argument("--personality", type=str, help="chatbot personality", default="friendly and helpful assistant")
    args = parser.parse_args()
    initial_prompt = f"You are a conversational chatbot. Your personality is: {args.personality}" 
    messages = [{"role": "system", "content": initial_prompt}]
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

if __name__ == "__main__":
    main()