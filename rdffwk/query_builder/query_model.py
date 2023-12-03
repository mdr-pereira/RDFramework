from __future__ import annotations
from rdffwk.query_builder.query_builder import QueryBuilder

class QueryModel():

    def __init__(self, variables, prefixes, depth: int = 0) -> None:
        self.prefixes = prefixes
        self.variables = variables
        
        self.triples = []
        self.subQueries = []
        self.filters = []
        self.bindings = []
        self.having = []
        
        self.grouping = None
        self.limit = None
        self.offset = None
        
        self.depth = depth
        
    def add_triple(self, triple: str):
        self.triples.append(triple)

    def add_filter(self, filter: str):
        self.filters.append(filter)
        
    def add_bind(self, bind: str):
        self.bindings.append(bind)
        
    def add_sub_query(self, query: QueryModel):
        self.subQueries.append(query)
        
    def set_grouping(self, variables):
        self.grouping = variables
        
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
    
     