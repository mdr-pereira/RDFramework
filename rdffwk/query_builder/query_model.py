from __future__ import annotations
from typing import List
from rdffwk.query_builder.query_builder import QueryBuilder

class QueryModel():

    def __init__(self, variables, prefixes, isSubQuery: bool = False) -> None:
        self.prefixes = prefixes
        self.variables = variables
        
        self.triples = []
        self.subQueries = []
        
        self.isSubQuery = isSubQuery
        
    def add_triple(self, triple: List[str]):
        _triple = []
        
        for elem in triple:
            _triple.append(f"?{elem}" if elem in self.variables else elem)
     
        self.triples.append(_triple[0] + " " + _triple[1] + " " + _triple[2])
        
    def add_sub_query(self, query: QueryModel):
        self.subQueries.append(query)
        
    def set_is_sub_query(self, isSubQuery: bool):
        self.isSubQuery = isSubQuery
        
    def to_sparql(self) -> str:
        return QueryBuilder(self).build()
    
     