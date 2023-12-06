
from rdffwk.query_builder.query.query import Query
from rdffwk.queue_builder.operators import *
from rdffwk.queue_builder.queue import Queue


class Block():
    def __init__(self, knowledge_base) -> None:
        self.knowledge_base = knowledge_base
        self.queue = Queue()
    
    def query(self, *variables):
        self.queue.add(Query(self.knowledge_base, *variables))
        return self
    
    def where(self, *args):
        if(len(args) > 3 or len(args) < 1):
            raise SystemExit("Invalid number of arguments for where clause")
        
        self.queue.add(WhereOperator(*args))
        return self
    
    def filter(self, condition):
        self.queue.add(FilterOperator(condition))
        return self
    
    def bind(self, var, as_var):
        self.queue.add(BindOperator(var, as_var))
        return self
    
    def to_sparql(self):
        return self.queue.to_block_model(self).to_sparql()
    
    def __repr__(self) -> str:
        return self.to_sparql()
    
    