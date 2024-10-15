import os
from neo4j_operations import Neo4jOperations

def test_neo4j_connection():
    neo4j_host = os.environ.get('NEO4J_HOST', 'localhost')
    neo4j_port = os.environ.get('NEO4J_PORT', '7687')
    neo4j_user = os.environ.get('NEO4J_USER', '')  # デフォルト値を空文字列に変更
    
    if not neo4j_user:
        raise ValueError("NEO4J_USER environment variable is not set.")
    
    neo4j_ops = Neo4jOperations(f"bolt://{neo4j_host}:{neo4j_port}", neo4j_user)
    
    neo4j_ops.connect()
    greeting = neo4j_ops.create_greeting("Hello, world!")
    print(greeting)
    neo4j_ops.close()

if __name__ == "__main__":
    test_neo4j_connection()