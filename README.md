# Academic Assistant – Engenharia de Software (v1)

Este projeto implementa um **assistente acadêmico baseado em IA** capaz de responder perguntas sobre a matriz curricular do curso de **Engenharia de Software**.

A ideia principal é permitir que um utilizador faça perguntas em **linguagem natural**, enquanto um agente de IA consulta uma base de dados estruturada da matriz curricular e retorna respostas relevantes.

---

# 📚 Objetivo

Criar um **assistente inteligente para estudantes**, capaz de responder perguntas como:

- Quais são os pré-requisitos de uma disciplina?
- Quantos créditos tem determinada cadeira?
- Quais disciplinas precisam ser feitas antes de outra?
- Que disciplinas pertencem a determinado período?

O assistente utiliza um **modelo de linguagem (LLM)** juntamente com acesso a uma **base de dados SQL contendo a matriz curricular tratada**.

---

# ⚙️ Como funciona

O fluxo do sistema é:

1. O utilizador faz uma pergunta em linguagem natural.
2. Um **agente baseado em LLM** interpreta a pergunta.
3. O agente gera uma **query SQL** apropriada.
4. A query é executada na base de dados.
5. O resultado é interpretado e devolvido ao utilizador em linguagem natural.


---

# 🗂️ Estrutura de dados

A base de dados foi construída a partir da **matriz curricular de Engenharia de Software**, contendo informações como:

- disciplinas
- créditos
- códigos das disciplinas
- relações de pré-requisitos

Esses dados foram **extraídos e tratados** antes de serem armazenados no banco SQLite utilizado pelo agente.

---

# 🧠 Tecnologias utilizadas

- Python
- LangChain
- Ollama (LLM local)
- SQLite
- SQL

O modelo de linguagem é executado **localmente**, permitindo testar o sistema sem depender de APIs externas.

---

# 🚀 Versão atual (v1)

Nesta primeira versão, o assistente responde perguntas **com base em dados estruturados da matriz curricular** armazenados numa base SQL.

Exemplos de perguntas:

- "Quais são os pré-requisitos de Sistemas Operacionais?"
- "Quantos créditos tem a disciplina de Processos de Software?"
- "Quais disciplinas são pré-requisito de Engenharia de Requisitos?"

---

# 🔜 Próximos passos (v2)

A próxima versão do projeto irá expandir o assistente para responder perguntas baseadas em **documentação do curso**, como:

- planos de ensino
- regulamentos do curso
- documentos institucionais
- materiais informativos

Esses conteúdos virão de **PDFs e outros documentos**, utilizando uma arquitetura baseada em **RAG (Retrieval-Augmented Generation)**.


Isso permitirá perguntas como:

- "Qual é o objetivo da disciplina X?"
- "O que é abordado em Engenharia de Requisitos?"
- "Quais competências o curso pretende desenvolver?"

---

# 💡 Motivação

Este projeto explora o uso de **LLMs aplicados a dados educacionais**, investigando como agentes baseados em IA podem facilitar o acesso a informações académicas.

Além disso, serve como estudo prático de:

- agentes de IA
- geração automática de SQL
- integração de LLMs com bases de dados
- arquiteturas RAG

---

# 📌 Estado do projeto

Versão atual: **v1 (SQL Agent)**  
Próxima etapa: **v2 (RAG com documentos do curso)**

---

# 👨‍💻 Autor

Luan Pacheco Lima

