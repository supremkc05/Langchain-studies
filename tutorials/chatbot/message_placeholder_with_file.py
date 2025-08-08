from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

# chat template
chat_template = ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

# Version 1: Reading from text file (limited approach)
print("=== VERSION 1: Reading from text file ===")
chat_history_raw = []
try:
    with open('chat_history.txt') as f:
        lines = f.readlines()
        # Convert text lines to alternating Human/AI messages
        for i, line in enumerate(lines):
            line = line.strip()
            if i % 2 == 0:  # Even lines = Human messages
                chat_history_raw.append(HumanMessage(content=line))
            else:  # Odd lines = AI messages
                chat_history_raw.append(AIMessage(content=line))
    
    print("Chat history from file:")
    for msg in chat_history_raw:
        print(f"{type(msg).__name__}: {msg.content}")
    
    prompt1 = chat_template.invoke({'chat_history':chat_history_raw, 'query':'Where is my refund'})
    print(f"\nPrompt from file: {prompt1}")
    
except FileNotFoundError:
    print("chat_history.txt not found!")

print("\n" + "="*60 + "\n")

# Version 2: Using proper message objects (recommended)
print("=== VERSION 2: Using proper message objects ===")
chat_history_proper = [
    HumanMessage(content="Hello, I need help with my order"),
    AIMessage(content="I'd be happy to help you with your order. Can you provide your order number?"),
    HumanMessage(content="My order number is 12345")
]

print("Chat history with proper objects:")
for msg in chat_history_proper:
    print(f"{type(msg).__name__}: {msg.content}")

prompt2 = chat_template.invoke({'chat_history':chat_history_proper, 'query':'Where is my refund'})
print(f"\nPrompt with proper objects: {prompt2}")
