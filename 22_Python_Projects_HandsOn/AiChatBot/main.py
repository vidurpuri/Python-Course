from openai import OpenAI

key = '<API_KEY>'
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