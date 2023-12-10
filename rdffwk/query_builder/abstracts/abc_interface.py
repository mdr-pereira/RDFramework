from rdffwk.queue_builder.queue import Queue, QueueOperator
from rdffwk.queue_builder.operators.simple_operators import *
from copy import deepcopy

class AbstractInterface(object):
    """Abstract class that represents a query or a block, will only contain
    methods that are common to both.
    This is, methods that can occur within the WHERE clause of a query.

    The query method is the only one that despite being common to both, is
    different in each one, so it is only included here as an abstract method.
    
    Args:
        object (_type_): _description_
    """
    def __init__(self, knowledge_base) -> None:
        self.knowledge_base = knowledge_base
        self.queue = Queue()
        
    def query(self, _):
        raise NotImplementedError("Abstract method")
        
    def where(self, *args):
        if(len(args) > 3 or len(args) < 1):
            raise SystemExit("Invalid number of arguments for where clause")
    
        self.queue.add(WhereOperator(*args))
        return self
    
    def filter(self, condition):
        self.queue.add(FilterOperator(condition))
        return self
    
    def filter_exists(self, block, negation=False):
        self.queue.add(FilterExistsOperator(block, negation))
        return self
    
    def filter_not_exists(self, block):
        self.queue.add(FilterExistsOperator(block, True))
        return self
    
    def filter_in(self, var, values, negation=False):
        self.queue.add(FilterInOperator(var, values, negation))
        return self
    
    def filter_not_in(self, var, values):
        self.queue.add(FilterInOperator(var, values, True))
        return self
    
    def optional(self, block):
        self.queue.add(OptionalOperator(block))
        return self
    
    def union(self, block1, block2):
        self.queue.add(UnionOperator(block1, block2))
        return self
    
    def minus(self, block):
        self.queue.add(MinusOperator(block))
        return self
    
    def graph(self, graph, group):
        self.queue.add(GraphOperator(graph, group))
        return self
    
    def service(self, url, query):
        self.queue.add(ServiceOperator(url, query))
        return self
    
    def values(self, var, values):
        self.queue.add(ValuesOperator(var, values))
        return self
    
    def bind(self, var, as_var):
        self.queue.add(BindOperator(var, as_var))
        return self
    
    def get_prefixes(self):
        return self.knowledge_base.prefixes
    
    def cache(self):
        return deepcopy(self)
    
    def up(self):
        self.queue.add(QueueOperator("up"))
        return self
    
    def to_model(self, depth=0):
        raise NotImplementedError("Abstract method")
    
    def to_sparql(self):
        return self.to_model().to_sparql()
    
    def __str__(self) -> str:
        return str(self.queue)
    
    def __repr__(self) -> str:
        return self.to_sparql()