from typing import Iterable
from rdffwk.query_builder.block.block_model import BlockModel
from rdffwk.query_builder.query.query_model import QueryModel


class Queue(Iterable):

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

    def to_query_model(self, query) -> QueryModel:
        model = QueryModel(query.variables, query.get_prefixes())
        
        cur_model = model
        
        for node in self._queue:    
            if type(node) is type(query):
                cur_model.add_sub_query(QueryModel(node.variables, node.get_prefixes(), cur_model.depth + 2))
                cur_model = cur_model.subQueries[-1]
                
            else:
                node.add_to_model(cur_model)
                
        return model
    
    def to_block_model(self, block) -> BlockModel:
        model = BlockModel()
        
        cur_model = model
        
        for node in self._queue:    
            if type(node) is type(block):
                _aux = BlockModel(cur_model.depth + 2)
                cur_model.add_sub_query(_aux)
                cur_model = _aux
            else:
                node.add_to_model(cur_model)
                
        return model