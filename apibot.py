import openai

# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = 'gsk_XRHSGPwwQGDlIXMYc5UCWGdyb3FYjHXggDOjQYXqAt4Dy'

def chatbot(prompt):
    response = openai.ChatCompletion.create(
        model="llama3-70b-8192",  # or another available model
        messages=[
            {"role": "system", "content": "hello,how are you?"},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content'].strip()

if _name_ == "_main_":
    print("Simple Chatbot (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        reply = chatbot(user_input)
        print("Bot:", reply)