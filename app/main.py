import os
from neo4j_operations import Neo4jOperations
from search_operations import SearchOperations

def main():
    neo4j_host = os.environ.get('NEO4J_HOST', 'localhost')
    neo4j_port = os.environ.get('NEO4J_PORT', '7687')
    neo4j_user = os.environ.get('NEO4J_USER', '')
    neo4j_password = os.getenv('NEO4J_PASSWORD') 
    
    if not neo4j_user:
        raise ValueError("NEO4J_USER environment variable is not set.")
    
    neo4j_ops = Neo4jOperations(f"bolt://{neo4j_host}:{neo4j_port}", neo4j_user, neo4j_password)
    search_ops = SearchOperations(neo4j_ops)
    
    try:
        # Neo4jデータベースに接続
        neo4j_ops.connect()

        # データベースに初期データを挿入
        print("Inserting example data:")
        print(neo4j_ops.insert_example_data())
        
        print("\nCreating greeting:")
        print(neo4j_ops.create_greeting("Hello, Neo4j!"))

        print("\nInserting person data:")
        print(neo4j_ops.insert_person("John Doe", 30))
        print(neo4j_ops.insert_person("Jane Smith", 25))
        print(neo4j_ops.insert_person("Alice Johnson", 35))

        # 検索操作の実行例
        print("\nSearching by name 'John':")
        results = search_ops.search_by_name("John")
        for result in results:
            print(result)

        print("\nSearching by partial name 'oh':")
        results = search_ops.search_by_name("oh")
        for result in results:
            print(result)

        print("\nSearching by age range 25-32:")
        results = search_ops.search_by_age_range(25, 32)
        for result in results:
            print(result)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Neo4jデータベースから切断
        neo4j_ops.close()

if __name__ == "__main__":
    main()