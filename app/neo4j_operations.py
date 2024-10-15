from neo4j import GraphDatabase
import os

class Neo4jOperations:
    def __init__(self, uri, user, password):
        self.uri = uri
        self.user = user
        self.password = password
        self.driver = None

    def connect(self):
        self.driver = GraphDatabase.driver(self.uri, auth=(self.user, self.password))

    def close(self):
        if self.driver:
            self.driver.close()

    def create_greeting(self, message):
        with self.driver.session() as session:
            greeting = session.write_transaction(self._create_and_return_greeting, message)
            return greeting

    @staticmethod
    def _create_and_return_greeting(tx, message):
        result = tx.run("CREATE (a:Greeting) "
                        "SET a.message = $message "
                        "RETURN a.message + ', from node ' + id(a)", message=message)
        return result.single()[0]

    def insert_example_data(self):
        with self.driver.session() as session:
            result = session.write_transaction(self._create_and_return_example_data)
            return result

    @staticmethod
    def _create_and_return_example_data(tx):
        result = tx.run("CREATE (n:Example {name: $name}) RETURN n.name + ' created with ID ' + id(n)", 
                        name="Example Node")
        return result.single()[0]

    def insert_person(self, name, age):
        with self.driver.session() as session:
            result = session.write_transaction(self._create_and_return_person, name, age)
            return result

    @staticmethod
    def _create_and_return_person(tx, name, age):
        result = tx.run("CREATE (p:Person {name: $name, age: $age}) RETURN p.name + ' created with ID ' + id(p)", 
                        name=name, age=age)
        return result.single()[0]