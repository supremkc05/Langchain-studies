from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()
 
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
chat_history = []

while True:
    user_input = input("You: ")
    if user_input == 'exit':
        break
    
    chat_history.append(HumanMessage(content=user_input))
    result = model.invoke(chat_history)
    
    chat_history.append(AIMessage(content=result.content))
    
    print("AI:", result.content)

print("Chat History:", chat_history)
