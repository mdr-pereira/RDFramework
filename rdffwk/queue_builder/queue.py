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
        self._iter_all_nodes(model)
        return model
    
    def to_block_model(self, depth=0) -> BlockModel:
        model = BlockModel(depth)
        self._iter_all_nodes(model)
        return model
    
    def _iter_all_nodes(self, model):
        for node in self._queue:
            if node.__class__ == QueueOperator:
                model = self._process_queue_operator(model, node)
            else:
                node.add_to_model(model)
            
    def _process_queue_operator(self, model, node):
        match node.id:
            case "query":
                model = self._add_query_to_model(model, node.args[0], node.args[1])
            case "up":
                if model.parent != None:
                    model = model.parent
        return model
    
    def _add_query_to_model(self, model, query, keep_currrent):
        if keep_currrent:
            model.add_sub_query(QueryModel(query.variables, query.get_prefixes(), parent=model, depth=model.depth + 3))
            model = model.subQueries[-1]
        else:
            model.add_sub_query(query.to_model())
            model.subQueries[-1].set_precedents(model, model.depth + 3)
        return model
     
    def _print_item_classes(self):
        print([item.__class__ for item in self._queue])
        

class QueueOperator(object):
    
    def __init__(self, id, *args) -> None:
        super().__init__()
        self.id = id
        self.args = args
        