import os
from neo4j_operations import Neo4jOperations
from search_operations import SearchOperations

def test_search():
    neo4j_host = os.environ.get('NEO4J_HOST', 'localhost')
    neo4j_port = os.environ.get('NEO4J_PORT', '7687')
    neo4j_auth = os.environ.get('NEO4J_AUTH', 'neo4j/your_password_here')

    neo4j_ops = Neo4jOperations(neo4j_host, neo4j_port, neo4j_auth)
    search_ops = SearchOperations(neo4j_ops)

    neo4j_ops.connect()
    results = search_ops.search_by_name("John")
    print("Search results:")
    for result in results:
        print(result)
    neo4j_ops.close()

if __name__ == "__main__":
    test_search()