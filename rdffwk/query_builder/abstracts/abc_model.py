class AbstractModel(object):
    
    def __init__(self, depth=0) -> None:
        super().__init__()
        
        self.triples = []
        self.subQueries = []
        self.filters = []
        self.bindings = []
        self.values = []
        self.having = []
        self.services = []
        
        self.depth = depth
    
    
    def add_triple(self, triple: str):
        self.triples.append(triple)

    def add_filter(self, filter: str):
        self.filters.append(filter)
        
    def add_bind(self, bind: str):
        self.bindings.append(bind)
        
    def add_values(self, values: str):
        self.values.append(values)
        
    def add_service(self, service: str):
        self.services.append(service)
        
    def add_sub_query(self, query):
        self.subQueries.append(query)
        
    def set_depth(self, depth: int):
        self.depth = depth
        
    def to_sparql(self) -> str:
        raise NotImplementedError("Method not implemented")
    
    def __repr__(self) -> str:
        return self.to_sparql()