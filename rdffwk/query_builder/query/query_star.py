from rdffwk.query_builder.query.query import Query
from rdffwk.queue_builder.operators.star_operators import WhereStarOperator


class QueryStar(Query):
    
    def __init__(self, knowledge_base, variables) -> None:
        super().__init__(knowledge_base, variables)
        
    def where(self, *args):
        if(len(args) > 4 or len(args) < 1):
            raise SystemExit("Invalid number of arguments for where clause")

        self.queue.add(WhereStarOperator(*args))
        return self