from openai import OpenAI

key = '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'

messages = []

client = OpenAI(api_key=key)

def completion(message):
    global messages
    messages.append({"role": "user", "content": message})
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages
    )
    messages.append({"role": "assistant", "content": response.choices[0].message.content})
    print(response.choices[0].message.content)

if __name__ == "__main__":
    print(f'Joe: ')
    while True:
        user_input = input("You: ")
        completion(user_input)

#This will not work as i have not subscribed to OpenAI using paymnet method , but this code works for automated testing purposes.