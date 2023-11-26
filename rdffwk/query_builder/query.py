from typing import List
from rdffwk.queue_builder.operators.where_op import WhereOperator
from rdffwk.queue_builder.query_queue import QueryQueue


class Query:

    def __init__(self, knowledge_base, variables) -> None:
        self.knowledge_base = knowledge_base
        self.variables = variables
        
        self.queue = QueryQueue()

    def query(self, *args):
        self.queue.add(Query(self.knowledge_base, *args))
        return self

    def where(self, arg1: str, arg2: str, arg3 : str):
        self.queue.add(WhereOperator(arg1, arg2, arg3))
        return self
    
    def get_prefixes(self):
        return self.knowledge_base.prefixes

    def to_sparql(self):
        return self.queue.to_model(self).to_sparql()

    def __str__(self):
        return str(self.queue)