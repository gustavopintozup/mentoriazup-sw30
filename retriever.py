from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document

def init_database():
    """Ajuda Recursos Humanos a fazer avaliação de desempenho dos stackers."""

    z3 = """
    Como a pessoa Stacker Z3 gera impacto na StackSpot?
    O impacto gerado na StackSpot de um Z3 está diretamente ligado com entregas de funcionalidades e recursos que geram valor para clientes e mercado e também para o próprio produto/negócio. 
    A pessoa Stacker Z3:
    - Apoia e oferece suporte ao time para alcançarem juntos os resultados esperados;
    - Cumpre prazos das suas entregas com qualidade, garantindo assim a sequência saudável da esteira de desenvolvimento e/ou do que foi planejado;
    - Entrega com maestria suas atividades;
    - Contribui diariamente com processos de melhoria e evolução para o produto.
    """

    z4 = """
    Como a pessoa Stacker Z4 gera impacto na StackSpot?
    O impacto gerado na StackSpot de um Z4 está diretamente ligado com entregas de funcionalidades e recursos que geram valor para clientes e mercado e também para o próprio produto/negócio. 
    A pessoa Stacker Z4:
    - Contribui para o desenvolvimento do produto (ou processo) entregando com qualidade aquilo que lhe foi atribuído;
    - Realiza atividades e/ou implementa funcionalidades de baixa e média complexidade;
    - Corrige bugs e/ou resolve problemas específicos evitando retrabalho e débitos técnicos;
    - Busca contexto para sua execução;
    - Contribui diariamente com processos de melhoria e evolução para o produto.
    """

    z5 = """
    Como a pessoa Stacker Z5 gera impacto na StackSpot?
    O impacto gerado na StackSpot de um Z5 está diretamente ligado com entregas de funcionalidades e recursos que geram valor para clientes e mercado e também para o próprio produto/negócio. 
    A pessoa Stacker Z5:
    - Usa StackSpot (para times de engenharia), possui dominio do produto e fornece feedbacks para a melhoria do produto;
    - Consegue cumprir o planejamento negociando prazos quando necessário;
    - Preza pela qualidade e eficiência das entregas com autonomia;
    - Realiza atividades e/ou implementa funcionalidades média complexidade;
    - Identifica problemas e bugs corrigindo de forma escalável.
    """

    z6 = """
    Como a pessoa Stacker Z6 gera impacto na StackSpot?
    O impacto gerado na StackSpot de um Z6 está diretamente ligado com entregas de funcionalidades e recursos que geram valor para clientes e mercado e também para o próprio produto/negócio. 
    A pessoa Stacker Z6:
    - Domina Stackspot e usa o produto (para times de engenharia), tem conhecimento do negócio e visão de mercado;
    - Faz entregas eficientes com aderência no mercado e nos clientes dentro do tempo necessário;
    - Participa do planejamento das atividades, sempre de forma contextualizada, sugerindo prioridades, propondo melhorias relevantes para o produto/processo;
    - Implementa funcionalidades de alta complexidade, resilientes e escaláveis e com qualidade, evitando retrabalho;
    - Colabora com o desenvolvimento do time aprimorando a capacidade técnica e produtiva.
    """

    z7_spec = """"
    Como a pessoa Stacker Z7 especialista gera impacto na StackSpot?
    O impacto gerado na StackSpot de um Z7 especialista está diretamente ligado com entregas de funcionalidades e recursos que geram valor para clientes e mercado e também para o próprio produto/negócio. 
    A pessoa Stacker Z7 especialista :
    - Domina Stackspot e usa o produto (para times de engenharia), tem alto contexto e conhecimento do negócio e tendências de mercado;
    - Diagnostica e propõe preditivamente inovações, correções e soluções, com aderência de mercado;
    - Define prioridades equilibrando tempo de entrega, eficiência dos entregáveis e qualidade;
    - Implementa funcionalidades de alta complexidade, resilientes e escaláveis e sem retrabalho;
    - Atua proativamente no desenvolvimento do time aprimorando a capacidade técnica e produtiva da equipe.
    """

    z7_gestao = """
    Como a pessoa Stacker Z7 gestora gera impacto na StackSpot?
    O impacto gerado na StackSpot Z7 gestora está diretamente ligado com entregas de funcionalidades e recursos que geram valor para clientes e mercado e também para o próprio produto/negócio. 
    A pessoa Stacker Z7 gestora:
    - Domina Stackspot e usa o produto (para times de engenharia), tem alto conhecimento do negócio e tendências de mercado;
    - Diagnostica e propõe preditivamente para o time, inovações, correções e soluções, garantindo aderência de mercado;
    - Define prioridades garantindo que o time equilibre tempo de entrega, eficiência dos entregáveis e qualidade;
    - Conduz a equipe a implementar funcionalidades resilientes e escaláveis e sem retrabalho;
    - Desenvolve do time aprimorando a capacidade técnica e produtiva da equipe;
    - Tem uma comunicação clara dando contexto para o time sobre a estratégia e prioridades, garantindo contexto, alinhamento e fomentando o protagonismo individual das pessoas.
    """

    z8_spec = """
    Como a pessoa Stacker Z8 especialista gera impacto na StackSpot?
    O impacto gerado na StackSpot Z8 especialista está diretamente ligado com entregas de funcionalidades e recursos que geram valor para clientes e mercado e também para o próprio produto/negócio. 
    A pessoa Stacker Z8 especialista:
    - Domina StackSpot e usa o produto (para times de engenharia), é referência no negócio, desenvolve funcionalidades no timing do mercado;
    - Identifica pontos críticos, elabora estratégias e desenvolve soluções e funcionalidades complexas;
    - Suas entregas sao inovadoras, escaláveis e se sustentam em ambientes de alta complexidade, sempre de forma contextualizada, elevando o produto à outros patamares;
    - É referência no seu ecossistema evoluindo a régua técnica do time;
    - Colabora com a evolução dos processos e melhoria contínua. 
    """

    z8_gestao = """
    Como a pessoa Stacker Z8 gestora gera impacto na StackSpot?
    O impacto gerado na StackSpot Z8 gestora está diretamente ligado com entregas de funcionalidades e recursos que geram valor para clientes e mercado e também para o próprio produto/negócio. 
    A pessoa Stacker Z8 gestora:
    - Domina StackSpot e usa o produto (para times de engenharia), é referência no negócio, desenvolve funcionalidades no timing do mercado;
    - Identifica pontos críticos, elabora estratégias e desenvolve soluções e funcionalidades complexas;
    - Sua entregas sao inovadoras, escaláveis e se sustentam em ambientes de alta complexidade, sempre de forma contextualizada, elevando o produto à outros patamares;
    - É referência no seu ecossistema evoluindo a régua técnica do time;
    - Colabora com a evolução dos processos e melhoria contínua. 
    """

    z9_spec = """
    Como a pessoa Stacker Z9 especialista gera impacto na StackSpot?
    O impacto gerado na StackSpot Z9 especialista está diretamente ligado com entregas de funcionalidades e recursos que geram valor para clientes e mercado e também para o próprio produto/negócio. 
    A pessoa Stacker Z9 especialista:
    - Domina StackSpot, tem conhecimento de multitecnologias e disciplinas atuais;
    - Toma decisões assertivas acerca das inovações mudanças e estratégia do produto/processos;
    - Desenha estratégias, melhora os processos do seu ecossistema garantindo comunicação e contexto;
    - Conecta diferentes verticais afim de evoluir o produto/área que atua e suas entregas tem boa aderência e aceitação no cliente/mercado;
    - É referência técnica em seu ecossistema por desenvolver e implementar soluções de alto nível e alta complexidade, incentivando a busca e pesquisa por caminhos inovadores, e por propor e criar um ambiente colaborativo e de melhoria contínua.
    """

    z9_gestao = """
    Como a pessoa Stacker Z9 gestora gera impacto na StackSpot?
    O impacto gerado na StackSpot Z9 gestora está diretamente ligado com entregas de funcionalidades e recursos que geram valor para clientes e mercado e também para o próprio produto/negócio. 
    A pessoa Stacker Z9 gestora:
    - Domina StackSpot, tem conhecimento de multitecnologias e disciplinas atuais e por isso toma decisões assertivas acerca das inovações, mudanças e estratégia do produto/processos;
    - Desenha estratégias, melhora os processos do seu ecossistema garantindo comunicação e contexto para seus liderados;
    - Conecta diferentes verticais afim de evoluir o produto/área que atua;
    - As entregas de seu time tem boa aderência e aceitação no cliente/mercado;
    - É referência em seu ecossistema e conviado a co-criar junto ao cliente e áreas parceiras;
    - Influencia decisões corporativas que elevam nossos resultados e impactos finanaceiros.
    """

    z10_spec = """ 	
    Como a pessoa Stacker Z10 especialista gera impacto na StackSpot?
    O impacto gerado na StackSpot Z10 especialista está diretamente ligado com entregas de funcionalidades e recursos que geram valor para clientes e mercado e também para o próprio produto/negócio. 
    A pessoa Stacker Z10 especialista:
    - Sua atuação deve elevar o produto, o negócio e a Zup a outros patamares de mercado;
    - Desenha estratégias corporativas assertivas, garante e cadencia com excelência dando contexto e clareza a todo o ecossistema de onde queremos chegar;
    - O impacto de sua atuação pode ser visto através dos resultados dos domínios, métricas de sucesso do produto e vendas.
    """

    z10_gestao = """
    Como a pessoa Stacker Z10 gestora gera impacto na StackSpot?
    O impacto gerado na StackSpot Z10 gestora está diretamente ligado com entregas de funcionalidades e recursos que geram valor para clientes e mercado e também para o próprio produto/negócio. 
    A pessoa Stacker Z10 gestora:
    - Sua atuação deve elevar o produto, o negócio e a Zup a outros patamares de mercado;
    - Desenha estratégias corporativas assertivas, garante e cadencia com excelência dando contexto e clareza a todo o ecossistema de onde queremos chegar;
    - Seus liderados são autonomos, protagonistas, agentes de mudança e melhoria contínua, sempre alinhados e com muito contexto;
    - O impacto de sua atuação pode ser visto através dos resultados dos domínios, métricas de sucesso do produto e vendas.
    """

    zs = [z3, z4, z5, z6, z7_gestao, z7_spec, z8_gestao, z8_spec, z9_gestao, z9_spec, z10_gestao, z10_spec]

    docs = [Document(page_content=z) for z in zs]
    embeddings = OpenAIEmbeddings()

    db = Chroma.from_documents(
        documents=docs, 
        embedding=embeddings, 
        persist_directory="./stackspot")

    db.persist()


if __name__ == "__main__":
    db = Chroma(persist_directory="./stackspot", embedding_function=OpenAIEmbeddings())
    diretriz = db.similarity_search("eu sou stacker Z10 diretor", k=1)
    print(diretriz)

    diretriz = db.similarity_search("eu sou stacker Z8 gestor", k=1)
    print(diretriz)

    diretriz = db.similarity_search("eu sou um profissional Z5", k=1)
    print(diretriz)

