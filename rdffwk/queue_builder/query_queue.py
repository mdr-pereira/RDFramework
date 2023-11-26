from typing import Iterable

from rdffwk.query_builder.query_model import QueryModel

class QueryQueue(Iterable):

    def __init__(self):
        self._queue = []

    def add(self, query):
        self._queue.append(query)

    def pop(self, ix=-1):
        return self._queue.pop(ix)

    def __str__(self):
        return str(self._queue)
    
    def __iter__(self):
        return iter(self._queue)

    def to_model(self, query) -> QueryModel:
        model = QueryModel(query.variables, query.get_prefixes())
        
        for node in self._queue:
            cur_model = model
            
            if type(node) is type(query):
                cur_model.add_sub_query(QueryModel(node.variables, node.get_prefixes(), True))
                cur_model = cur_model.subQueries[-1]
            
            else:
                node.add_to_model(cur_model)
                
        return model