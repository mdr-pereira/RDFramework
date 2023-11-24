from __future__ import annotations

class QueryModel():

    def __init__(self, isSubQuery: bool = False) -> None:
        self.subQueries = []
        
        self.isSubQuery = isSubQuery
        
    def add_sub_query(self, query: QueryModel):
        self.subQueries.append(query)
    
     