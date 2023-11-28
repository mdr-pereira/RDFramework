from rdffwk.queue_builder.operators import *
from rdffwk.queue_builder.query_queue import QueryQueue
from copy import deepcopy

class Query:

    def __init__(self, knowledge_base, variables) -> None:
        self.knowledge_base = knowledge_base
        self.variables = variables
        
        self.queue = QueryQueue()

    def query(self, *args):
        self.queue.add(Query(self.knowledge_base, *args))
        return self
    
    def filter(self, condition):
        self.queue.add(FilterOperator(condition))
        return self

    def where(self, arg1, arg2, arg3):
        self.queue.add(WhereOperator(arg1, arg2, arg3))
        return self
    
    def bind(self, var, as_var):
        self.queue.add(BindOperator(var, as_var))
        return self
    
    def group_by(self, *args):
        self.queue.add(GroupByOperator(*args))
        return self
    
    def limit(self, limit: int):
        self.queue.add(LimitOperator(limit))
        return self
    
    def offset(self, offset: int):
        self.queue.add(OffsetOperator(offset))
        return self
    
    def get_prefixes(self):
        return self.knowledge_base.prefixes
    
    def cache(self):
        return deepcopy(self)

    def to_sparql(self):
        return self.queue.to_model(self).to_sparql()

    def __str__(self):
        return str(self.queue)