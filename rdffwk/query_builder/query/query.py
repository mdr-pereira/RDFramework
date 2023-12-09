from rdffwk.queue_builder.operators import *
from rdffwk.queue_builder.queue import Queue
from copy import deepcopy

class Query():

    def __init__(self, knowledge_base, variables) -> None:
        self.knowledge_base = knowledge_base
        self.variables = variables
        
        self.queue = Queue()

    def query(self, *args):
        self.queue.add(Query(self.knowledge_base, *args))
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

    def where(self, *args):
        if(len(args) > 3 or len(args) < 1):
            raise SystemExit("Invalid number of arguments for where clause")
        
        self.queue.add(WhereOperator(*args))
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
    
    def bind(self, var, as_var):
        self.queue.add(BindOperator(var, as_var))
        return self
    
    def values(self, var, values):
        self.queue.add(ValuesOperator(var, values))
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

    def to_sparql(self):
        return self.queue.to_query_model(self).to_sparql()

    def __str__(self):
        return str(self.queue)
    
    def get_prefixes(self):
        return self.knowledge_base.prefixes