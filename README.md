# Mentoria Software 3.0 

Olá Zupper! Nesse repositório tem alguns trechos de código apresentados nos Alinhas Zup Técnicos e sessões de mentoria sobre Software 3.0.

Os arquivos são:

- [main.py](main.py): contem a criação dos modelos, tools e agentes. 
- [retriever.py](retriever.py): cria a base de dados vetorial.
- [prompt.py](prompt.py): exemplos sobre construção de prompts.
- [embeddings.py](embeddings.py): criação e manipulação básica de embeddings.
- [chat.py](chat.py): código com exemplos de como guardar histórico de conversa.

### Mentoria 5 de Junho

- [reviewperf.py]: consulta as diretirzes de avaliação de performance do banco e passa para um modelo através de um prompt enriquecido 
- [reviewperfdb.py]: salva as diretrizes de avaliação de performance no chromadb

## Rode localmente

1. Crie um ambiente `env` e ative-o:

```bash
python3 -m venv env
source env/bin/activate
```

2. Instale as dependências

```bash
pip3 install -r requirements.txt
```

## Questionamentos 

Caso você tenha alguma dúvida, entre em contato via chat com gustavo.pinto ou abra uma issue nesse repositório.