from neo4j import GraphDatabase

class SearchOperations:
    def __init__(self, neo4j_operations):
        self.neo4j_operations = neo4j_operations

    def search_by_name(self, name):
        with self.neo4j_operations.driver.session() as session:
            results = session.read_transaction(self._find_by_name, name)
            return results

    @staticmethod
    def _find_by_name(tx, name):
        # CONTAINS を使用して部分一致検索を実現
        query = """
        MATCH (p:Person)
        WHERE p.name CONTAINS $name
        RETURN p.name AS name, id(p) AS id, p.age AS age
        """
        result = tx.run(query, name=name)
        return [{"name": record["name"], "id": record["id"], "age": record["age"]} for record in result]

    def search_by_age_range(self, min_age, max_age):
        with self.neo4j_operations.driver.session() as session:
            results = session.read_transaction(self._find_by_age_range, min_age, max_age)
            return results

    @staticmethod
    def _find_by_age_range(tx, min_age, max_age):
        query = """
        MATCH (p:Person)
        WHERE p.age >= $min_age AND p.age <= $max_age
        RETURN p.name AS name, id(p) AS id, p.age AS age
        """
        result = tx.run(query, min_age=min_age, max_age=max_age)
        return [{"name": record["name"], "id": record["id"], "age": record["age"]} for record in result]