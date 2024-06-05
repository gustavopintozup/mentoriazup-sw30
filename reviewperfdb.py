import chromadb

def init_database():
    """Ajuda Recursos Humanos a fazer avaliação de desempenho dos stackers"""

    z3 = """bla bla bla"""

    z4 = """bla bla bla"""

    z5 = """bla bla bla"""

    z6 = """bla bla bla"""

    z7_spec = """bla bla bla"""

    z7_gestao = """bla bla bla"""

    z8_spec = """bla bla bla"""

    z8_gestao = """bla bla bla"""

    z9_spec = """bla bla bla"""

    z9_gestao = """bla bla bla"""

    z10_spec = """bla bla bla"""

    z10_gestao = """bla bla bla"""

    client = chromadb.PersistentClient(path="./stackspot")
    collection = client.get_or_create_collection("ReviewPerformance")

    documents = [z3, z4, z5, z6, z7_gestao, z7_spec, z8_gestao, z8_spec, z9_gestao, z9_spec, z10_gestao, z10_spec]
    ids = [f"id{i}" for i in range(1, len(documents) + 1)]

    collection.add(
        documents = documents,
        metadatas = [
            {"source": "z3"},
            {"source": "z4"},
            {"source": "z5"},
            {"source": "z6"},
            {"source": "z7_spec"},
            {"source": "z7_gestao"},
            {"source": "z8_spec"},
            {"source": "z8_gestao"},
            {"source": "z9_spec"},
            {"source": "z9_gestao"},
            {"source": "z10_spec"},
            {"source": "z10_gestao"}
            ],
        ids = ids
        )


def get_performance_guidelines(user_query, z_level):
    client = chromadb.PersistentClient(path="./stackspot")
    collection = client.get_or_create_collection("ReviewPerformance")
    
    results = collection.query(
        query_texts=[user_query],
        n_results=1,
        where={"source": z_level}
    )

    return results['documents'][0][0]
