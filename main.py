from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.tools import tool
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain_community.vectorstores import Chroma
import requests 

# hello world
model = ChatOpenAI(model="gpt-4", temperature=0)

prompt = ChatPromptTemplate.from_template("Gostaria que você atuasse como um expert em tecnologia. Responda a pergunta do usuário: {input} \n {agent_scratchpad}")

#chain = prompt | model
#result = chain.invoke({"input" : "Vai ter ZupCon?"})

@tool
def vai_ter_zupcon():
    """Tool que ajuda os Zuppers a saberem se vai ter ZupCom"""
    return "Sim, vai ter ZupCon e Ivete Sangalo!"

@tool 
def summarizacao_websites(url):
    """tool que é util para fazer sumarização de websites"""
    text = requests.get(url).text

    prompt = ChatPromptTemplate.from_template("sumarize esse conteudo: {text}")
    chain = prompt | model
    return chain.invoke({"text": text})

@tool
def apoio_review_performance(input):
    """tool que ajuda as pessoas BPs a conduzir processo de review de performance na Zup"""
    # 1. tenho que saber qual é o nível de Z da pessoa

    prompt = ChatPromptTemplate.from_template("Identifique o nível de Z (Z3-Z10) na review a seguir {input}. Retorne somente o nível de Z.")

    chain = prompt | model
    nivel_z = chain.invoke({"input" : input}).content
    print(nivel_z)

    # 2. buscar as diretrizes do nível de Z do banco

    db = Chroma(persist_directory="./stackspot", embedding_function=OpenAIEmbeddings())
    diretriz = db.similarity_search(nivel_z, k=1)

    # 3. pedir pro modelo fazer a avaliacao da pessoa com base nas diretrizes

    prompt = ChatPromptTemplate.from_template("Você é um profissional de recursos humanos e preicsa conduzir avaliação de desempenho na sua empresa, chamada Zup. Considerando o nível de senioridade na Zup vai de Z3 (menos experiente) até Z10 (mais experiente), avalie o seguinte profissional do nível {nivel_z}, que realisou os seguintes cases: {input}. Avalie com base nas diretrizes {diretriz}.")

    chain = prompt | model
    resultado = chain.invoke({"input": input, "nivel_z": nivel_z, "diretriz": diretriz})

    print(resultado)

    return resultado


tools = [vai_ter_zupcon, apoio_review_performance, summarizacao_websites]
agent = create_openai_functions_agent(model, tools, prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools)


user_input = """
    Me auxilie a compreender o desempenho de um desenvolvedor sênior (Z5) por meio dos casos reportados a seguir.
    ### Início Case 1
    Situação:
    <Coloque seu case aqui>
    ### Fim Case 1
    """

result = agent_executor.invoke({"input" : user_input})
print(result)