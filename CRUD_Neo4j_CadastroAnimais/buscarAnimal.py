from neo4j import GraphDatabase
from crud import buscar_animal_por_tipo

# Configuração da conexão com o banco de dados Neo4j
neo4j_uri = ""  # URI do servidor Neo4j
neo4j_user = "neo4j"  # Nome de usuário
neo4j_password = ""  # Senha

# Criação do objeto do driver do Neo4j
neo4j_driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_user, neo4j_password))

with neo4j_driver.session() as session:
    tipo = "Cachorro"  # Tipo de animal a ser buscado
    buscar_animal_por_tipo(tipo)
