from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

## create a chat template
chat_template = ChatPromptTemplate.from_messages([
    ('system', 'You are a helpful chat assistant'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{query}')
])

# initialize chat history
chat_history = []

# load chat history
with open('chat_history.txt') as f:
    for line in f:
        line = line.strip()

        if line.startswith("Human:"):
            chat_history.append(HumanMessage(content=line.replace("Human:", "").strip()))
        elif line.startswith("AI:"):
            chat_history.append(AIMessage(content=line.replace("AI:", "").strip()))

print(chat_history)

# create a prompt
prompt = chat_template.invoke({
    'chat_history': chat_history,
    'query': 'where is my refund?'
})

print(prompt)