from __future__ import annotations
from rdffwk.query_builder.query.query_builder import QueryBuilder

class QueryModel():

    def __init__(self, variables, prefixes, depth: int = 0) -> None:
        self.prefixes = prefixes
        self.variables = variables
        
        self.triples = []
        self.subQueries = []
        self.filters = []
        self.bindings = []
        self.values = []
        self.having = []
        self.services = []
        self.blocks = []
        
        self.grouping = None
        self.ordering = None
        self.limit = None
        self.offset = None
        
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
        
    def add_block(self, block: str):
        self.blocks.append(block)
        
    def add_sub_query(self, query: QueryModel):
        self.subQueries.append(query)
        
    def set_grouping(self, variables):
        self.grouping = variables
        
    def set_order_by(self, variables):
        self.ordering = variables
        
    def add_having(self, condition: str):
        self.having.append(condition)
        
    def set_limit(self, limit: str):
        self.limit = limit
        
    def set_offset(self, offset: str):
        self.offset = offset
        
    def to_sparql(self) -> str:
        if(self.triples == [] and self.subQueries == []):
            raise SystemExit("No triples or subqueries in query")
        
        return QueryBuilder(self).build()
    
     