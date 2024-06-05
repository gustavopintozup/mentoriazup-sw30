from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import pprint

model = ChatOpenAI(model="gpt-4o", temperature=0)
#resultado = model.invoke("Oi, meu nome é Gustavo e estou aprendendo Python. Você poderia me fazer um guia de estudos? Devolva o conteudo em formato de JSON. Foque somente em assuntos avançados. Use no maximo 25 palavras.")
#pprint.pp(resultado.content)


prompt = ChatPromptTemplate.from_messages([
            ("system", "Você é um assistente de código muito habilidoso."),
            ("user", "{input}"),
            ("system", "Se a pergunta não for sobre código, responda 'Eu não sei'."),
            ("system", "Responda em no máximo 30 palavras."),
            ("system", "Responda somente o trecho de código."),
        ])


chain = prompt | model 
#codigo_fast_api = chain.invoke({"input" : "Gostaria de fazer um hello world com fastapi."})

prompt_quick_command = ChatPromptTemplate.from_messages([
            ("system", "Você é um assistente de código muito habilidoso em transformar código Python em Java."),
            ("user", "{input}"),
            ("system", "Você deve utilizar esses frameworks: {stack_ai}"),
            ("system", "Devolva somente o código Java equivalente."),
        ])

# zero shot

chain = prompt_quick_command | model 
#codigo_java = chain.invoke({"input" : codigo_fast_api,  "stack_ai" : "micronaut"})

#pprint.pp(codigo_java.content)

# few-shot 
forma_de_avaliacao = """
Quanto maior a quantidade de ifs, maior deve ser a nota de complexidade.

codigo 1: if x > 0: return True
nota: 1

codigo 2: if x > 0: if y < 0: return True else: return False
nota: 3

codigo 3:
"""

prompt_quick_command = ChatPromptTemplate.from_messages([
            ("system", "Você é um assistente de código muito habilidoso descrever imagens."),
            ("user", "{input}"),
        ])

chain = prompt_quick_command | model 
#descricao_imagem = chain.invoke({"input" : "https://www.stackspot.com/wp-content/uploads/2024/05/TELAS-AI-2-1.png"})


from langchain_core.messages import HumanMessage


# Substitua 'url_da_imagem_aqui' pela URL real da imagem que você deseja descrever
url_da_imagem = "https://www.stackspot.com/wp-content/uploads/2024/05/TELAS-AI-2-1.png"

# Cria uma mensagem que inclui a URL da imagem e uma solicitação de descrição
mensagem = [
    HumanMessage(
        content=[
            {"type": "text", "text": "Descreva essa imagem:"},
            {"type": "image_url", "image_url": {"url": url_da_imagem}},
        ]
    )
]

resposta = model.invoke(mensagem)

# Imprime a descrição fornecida pelo modelo
print(resposta.content)
