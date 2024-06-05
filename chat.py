from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.callbacks import get_openai_callback

model = ChatOpenAI(model="gpt-4o", temperature=0)

sent_mensagens = []

print("% Olá, eu sou o SuperBot, e sou especialista em música Rap.")

while True:
    with get_openai_callback() as cb:
        messages = [
            ("system", "Olá, eu sou o SuperBot, e sou especialista em música Rap."),
            *sent_mensagens[:10],
            ("user", "{user_input}"),
        ]
        print(messages)

        prompt = ChatPromptTemplate.from_messages(messages)

        chain = prompt | model

        user_input = input("> ")
        if user_input == "q":
            import sys; sys.exit(0)

        response_ai = chain.invoke({"user_input" : user_input})

        sent_mensagens.append(("user", user_input))
        sent_mensagens.append(("ai", response_ai.content))

        print(response_ai.content)
        print(cb.total_tokens)

