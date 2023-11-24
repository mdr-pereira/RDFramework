
class Query:

    def __init__(self, knowledge_base, variables, query_type, query_params) -> None:
        self.knowledge_base = knowledge_base
        self.variables = variables
        self.query_type = query_type
        self.query_params = query_params

        self.queue = QueryQueue()

    def query(self, *args):
        self.queue.add(self.query_type(*args))
        
        return self

    def where(self, arg1, arg2, arg3 : str or List[str]):
        if isinstance(arg3, list):
            for arg in arg3:
                self.queue.add(WhereOperator(arg1, arg2, arg))
        else:
            self.queue.add(WhereOperator(arg1, arg2, arg3))

        return self

    def to_sparql(self):
        return QueueToQuery(self).to_model()

    def __str__(self):
        return str(self.queue)