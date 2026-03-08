import os
import pathlib
import requests

from langchain_ollama import ChatOllama
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent

def carregar_llm():
    llm = ChatOllama(
        model="llama3",
        temperature=0
    )
    return llm

model = carregar_llm()

def carregar_db():
    """
    Conecta à base de dados SQLite
    """
    db = SQLDatabase.from_uri("sqlite:///matriz.db",sample_rows_in_table_info=3)
    return db
print(f"[INFO] Tabelas disponiveis: {carregar_db().get_usable_table_names()}")

prefix = """
You are an expert SQL agent.

Rules:
- Always inspect table schemas before writing SQL
- Use JOIN correctly
- Only return the columns needed
- Limit results to 5 when possible
- Interpret the SQL results and answer in natural language
"""
def criar_agente(model, db):
    agent = create_sql_agent(
        llm=model,
        db=db,
        verboso=True,
        prefix=prefix
    )
    return agent


def responder_pergunta(agent, pergunta: str) -> str:
    """
    Envia a pergunta ao agente
    """
    try:
        resposta = agent.invoke(pergunta)
        output = resposta["output"]

        if isinstance(output, list):
            return "\n".join(str(x) for x in output)

        return str(output)

    except Exception as e:
        return f"Erro ao executar agente: {str(e)}"


if __name__ == "__main__":

    print("\n[INFO] A carregar modelo...")
    llm = carregar_llm()

    print("[INFO] A ligar à base de dados...")
    db = carregar_db()

    print(f"[INFO] Tabelas disponíveis: {db.get_usable_table_names()}")

    print("[INFO] A criar agente SQL...")
    agent = criar_agente(llm, db)

    print("\n[INFO] Agente SQL pronto.")
    print("[INFO] Faça perguntas sobre a base de dados.")
    print("[INFO] Exemplo: 'Quais são os 5 artistas com mais álbuns?'")
    print("[INFO] Para sair: CTRL+C\n")

    while True:
        try:
            pergunta = input("Pergunta: ").strip()

            if not pergunta:
                continue

            print("\n[A AGENTE] A pensar...\n")

            resposta = responder_pergunta(agent, pergunta)

            print("Resposta:\n")
            print(resposta)

            print("\n" + "-" * 60 + "\n")

        except KeyboardInterrupt:
            print("\n[INFO] A terminar.")
            break



