from langchain_openai import OpenAIEmbeddings
from scipy.spatial import distance

from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document


embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

# query = embeddings.embed_query("qual a parte da casa que você mais gosta?")

# docs = [
#     "cachorro quente",
#     "pizza",
#     "quarto",
#     "google",
#     "cozinha"
# ]

# docs_embs = embeddings.embed_documents(docs)

# for id, doc in enumerate(docs_embs):
#     resultado = 1 - distance.cosine(query, doc)
#     print(resultado, docs[id])


user_query = "como cancelar um agendamento?"

faq_localiza = [
    "Como faço a reserva para alugar um carro?",
    "Como faço para consultar/ alterar e cancelar uma reserva de um carro feita pelo site ou APP?",
    "Reservei um carro por meio da Central de Reservas. Posso fazer a consulta, alteração e/ou cancelamento no site/APP?",
    "Reservei um carro pelo site, por qual caminho posso consultar, alterar e/ou cancelar essa reserva?",
    "É possível fazer uma reserva para aluguel de carro com motorista?",
    "O que acontece se eu não comparecer para retirada da minha reserva?",
    "Posso atravessar as fronteiras do Brasil com um carro alugado?",
    "Quanto tempo de antecedência é necessário para fazer a reserva de aluguel de carro da Localiza?",
    "Como sei que a minha reserva está confirmada?",
    "Reserva feita em sites como SMILES/ DECOLAR/ RENTCars parceiros da Localiza é possivel ser alterada na Central de Reservas?",
    "Qual é a diferença entre oferta standard e oferta promo?"
]


# docs = [Document(page_content=c) for c in faq_localiza]

# chroma_db = Chroma.from_documents(
#     documents=docs,
#     embedding=embeddings,
#     persist_directory="./localiza",  
# )

# chroma_db.persist()

db = Chroma(persist_directory="./localiza", 
            embedding_function=OpenAIEmbeddings())


resultados = db.similarity_search(user_query, k=3)
print(resultados)


# query_emb = embeddings.embed_query(user_query)
# faq_emb = embeddings.embed_documents(faq_localiza)

# for id, faq in enumerate(faq_emb):
#     resultado = 1 - distance.cosine(query_emb, faq)
#     if resultado > 0.5:
#         print(resultado, faq_localiza[id])



