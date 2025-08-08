from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

# chat template
chat_template = ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

# Create sample chat history with proper message objects
chat_history = [
    HumanMessage(content="Hello, I need help with my order"),
    AIMessage(content="I'd be happy to help you with your order. Can you provide your order number?"),
    HumanMessage(content="My order number is 12345")
]

print("Chat History:")
for msg in chat_history:
    print(f"{type(msg).__name__}: {msg.content}")

print("\n" + "="*50 + "\n")

# create prompt
prompt = chat_template.invoke({'chat_history':chat_history, 'query':'Where is my refund'})

print("Generated Prompt:")
print(prompt)