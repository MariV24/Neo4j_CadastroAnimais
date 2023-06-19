# Utilizar pip install neo4j antes de executar o código
# Imortando bibliotecas
from neo4j import GraphDatabase

uri = ""
username = "neo4j"
password = ""

try:
    # Inicialização do driver do Neo4j
    driver = GraphDatabase.driver(uri, auth=(username, password))

    # Funcionalidades

    #Criar animal
    def criar_animal(tipo, nome, idade):
        with driver.session() as session:
            session.run(
                "CREATE (:Animal {tipo: $tipo, nome: $nome, idade: $idade})",
                tipo=tipo,
                nome=nome,
                idade=idade
            )


    #Buscar animal por tipo
    def buscar_animal_por_tipo(tipo):
        try:
            with driver.session() as session:
                result = session.run(
                    "MATCH (a:Animal) WHERE a.tipo = $tipo RETURN ID(a) AS id, a.nome AS nome, a.tipo AS tipo, a.idade AS idade",
                    tipo=tipo)
                for record in result:
                    id = record["id"]
                    nome = record["nome"]
                    tipo = record["tipo"]
                    idade = record["idade"]
                    print(f"ID: {id} - Nome: {nome} - Tipo: {tipo} - Idade: {idade}")
        except Exception as e:
            print(f"Ocorreu um erro ao buscar os animais por tipo: {e}")


    #Atualizar animal
    def atualizar_animal(id, nome, tipo, idade):
        try:
            with driver.session() as session:
                session.run("MATCH (a:Animal) WHERE ID(a) = $id SET a.nome = $nome, a.tipo = $tipo, a.idade = $idade",
                            id=id, nome=nome, tipo=tipo, idade=idade)
            print("Animal atualizado com sucesso!")
        except Exception as e:
            print(f"Ocorreu um erro ao atualizar o animal: {e}")


    #Excluir animal
    def excluir_animal(nome):
        with driver.session() as session:
            session.run(
                "MATCH (animal:Animal {nome: $nome}) DELETE animal",
                nome=nome
            )

except Exception as e:
    # Lidar com a exceção
    print("Ocorreu um erro:", str(e))

finally:
    # Fechamento da conexão com o banco de dados
    if 'driver' in locals() or 'driver' in globals():
        driver.close()