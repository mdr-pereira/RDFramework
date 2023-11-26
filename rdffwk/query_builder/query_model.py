from __future__ import annotations
from rdffwk.query_builder.query_builder import QueryBuilder

class QueryModel():

    def __init__(self, variables, prefixes, isSubQuery: bool = False) -> None:
        self.prefixes = prefixes
        self.variables = variables
        
        self.triples = []
        self.subQueries = []
        self.filter = []
        
        self.isSubQuery = isSubQuery
        
    def add_triple(self, triple: str):
        self.triples.append(triple)

    def add_filter(self, filter: str):
        self.filter.append(filter)
        
    def add_sub_query(self, query: QueryModel):
        self.subQueries.append(query)
        
    def set_is_sub_query(self, isSubQuery: bool):
        self.isSubQuery = isSubQuery
        
    def to_sparql(self) -> str:
        return QueryBuilder(self).build()
    
     