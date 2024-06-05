"""
DESAFIO: construa um programa que facilite a atividade de autoavaliação de performance dentro da Zup. 
Implemente um agente que facilite processo de avaliação de performance recebendo como entrada um texto descrevendo as entregas da pessoa, além do nível Z dela e sua carreira (frontend, backend etc). 
Utilize as dimensões de análise de performance registradas no Zenity para que você enriqueça o prompt final (RAG) enviado para a LLM para obter a resposta.
"""

from reviewperfdb import get_performance_guidelines

# 1. um texto descrevendo as entregas da pessoa
# 2. O nivel Z da pessoa
# 3. as diretrizes de analise de performance
# 4. enriquecer o prompt final
# 5. enviar para a LLM para obter a resposta final

auto_avaliacao = "Eu sou um dev backend que criei 28 serviços e revisei 300 pull-requests."
nivel_z = "z10_spec"
diretriz = get_performance_guidelines(auto_avaliacao, nivel_z)

from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI()

prompt = ChatPromptTemplate.from_messages([
            ("system", "Você é um especialista em avaliação de desempenho em uma empresa de tecnologia chamada Zup."),
            ("system", "Considere a auto avaliação abaixo de um Zupper."),
            ("user", "{auto_avaliacao}"),
            ("system", "Forneça um feedback com base nas diretrizes da Zup: {diretriz}. Caso a pessoa Zupper não tenha coberto algum item da diretriz, informe na sua avaliação."),
            ("system", "Escreva em no máximo 100 palavras. "),
        ]
)

chain = prompt.pipe(llm)

response = chain.invoke({"auto_avaliacao" : auto_avaliacao, 
              "diretriz" : diretriz})

print(response.content)

# response = llm.invoke(f"Me ajude a avaliar esse colaborador: {auto_avaliacao}. Considere as diretrizes da empresa: {diretriz}").content
# print(response)
