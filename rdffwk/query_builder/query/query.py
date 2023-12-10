from rdffwk.query_builder.abc_query_block import Abstract
from rdffwk.queue_builder.operators import *
from rdffwk.queue_builder.queue import Queue
from copy import deepcopy

class Query(Abstract):

    def __init__(self, knowledge_base, variables) -> None:
        super().__init__(knowledge_base)
        self.variables = variables
        
    def query(self, *args):
        self.queue.add(Query(self.knowledge_base, *args))
        return self
    
    def group_by(self, *args):
        self.queue.add(GroupByOperator(*args))
        return self
    
    def order_by(self, *args):
        self.queue.add(OrderByOperator(*args))
        return self
    
    def limit(self, limit: int):
        self.queue.add(LimitOperator(limit))
        return self
    
    def offset(self, offset: int):
        self.queue.add(OffsetOperator(offset))
        return self
    
    def having(self, condition):
        self.queue.add(HavingOperator(condition))
        return self
    
    def cache(self):
        return deepcopy(self)
    
    def to_model(self):
        return self.queue.to_query_model(self)