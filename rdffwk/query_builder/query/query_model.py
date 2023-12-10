from rdffwk.query_builder.abstracts import AbstractModel
from rdffwk.query_builder.query.query_builder import QueryBuilder

class QueryModel(AbstractModel):

    def __init__(self, variables, prefixes, depth: int = 0) -> None:
        super().__init__(depth)
        
        self.prefixes = prefixes
        self.variables = variables
        
        self.grouping = None
        self.ordering = None
        self.limit = None
        self.offset = None
        
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
    
     