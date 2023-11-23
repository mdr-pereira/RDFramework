from typing import List
from rdffwk.queue_builder.operators.where_op import WhereOperator
from rdffwk.queue_builder.query_queue import QueryQueue


class Query:

    def __init__(self, knowledge_base, variables, query_type, query_params) -> None:
        self.knowledge_base = knowledge_base
        self.variables = variables
        self.query_type = query_type
        self.query_params = query_params

        self.queue = QueryQueue()

    def query(self, *args):
        self.queue.add(self.query_type(*args))
        
        return self

    def where(self, arg1, arg2, arg3 : str or List[str]):
        if isinstance(arg3, list):
            for arg in arg3:
                self.queue.add(WhereOperator(arg1, arg2, arg))
        else:
            self.queue.add(WhereOperator(arg1, arg2, arg3))

        return self

    def to_sparql(self):
        pass

    def __str__(self):
        return str(self.queue)