
responses = {
    "hi": "Hello! I am Sherrybot  How can I Help you today?",
    "how are you": "Alhumdullilah, Allah Ka shukar Hai ! How Are You  ! ",
    "What is Ai": "AI, or Artificial Intelligence, refers to the simulation of human intelligence in machines or computer systems.",
    "what is you name ": "My Name Is Chatbot ",
    "bye": "Allah Hafiz Boht Acha Laga Apsay Baat Krkay ! . Have a great day!",
    
}

while True:
    user_input = input("You: ").lower()
    if user_input in responses:
        print("Chatbot:", responses[user_input])
        if user_input == "bye":
            print("Chatbot: Goodbye!")
            break
    else:
        print("Chatbot: Ask Another Question ")
