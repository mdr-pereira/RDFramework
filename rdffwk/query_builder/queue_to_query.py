from . import query
from rdffwk.query_builder.query_model import QueryModel


class QueueToQuery():
    
    def __init__(self, query) -> None:
        self.query = query
        self.queue = query.queue
        
    def to_model(self):
        model = QueryModel()
        
        for node in self.queue:
            cur_model = model
            
            print(node.__class__)
            
            if (node.isInstance(Query)):
                cur_model.add_sub_query(QueryModel(True))
                cur_model = cur_model.subQueries[-1]
            
            else:
                pass