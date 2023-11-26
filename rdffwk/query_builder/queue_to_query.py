from rdffwk.query_builder.query_model import QueryModel

class QueueToQueryModel():
    
    def __init__(self, query) -> None:
        self.query = query
        self.queue = query.queue
        
    def to_model(self) -> QueryModel:
        model = QueryModel(self.query.variables, self.query.get_prefixes())
        
        for node in self.queue:
            cur_model = model
            
            if type(node) is type(self.query):
                cur_model.add_sub_query(QueryModel(node.query.variables, node.query.get_prefixes(), True))
                cur_model = cur_model.subQueries[-1]
            
            else:
                node.add_to_model(cur_model)
                
        return model