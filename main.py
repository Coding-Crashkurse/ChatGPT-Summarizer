from revChatGPT.V2 import Chatbot
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()

chatbot = Chatbot(email=os.environ.get("EMAIL"), password=os.environ.get("PASSWORD"))

async def main():
    while True:
        question = input("Gebe eine Frage ein: ")
        async for line in chatbot.ask(question):
            print(line["choices"][0]["text"], flush=True, end="")
        print()

if __name__ == "__main__":
    asyncio.run(main())