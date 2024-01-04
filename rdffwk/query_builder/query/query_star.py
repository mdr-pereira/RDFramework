from rdffwk.query_builder.query.query import Query
from rdffwk.queue_builder.operators.star_operators import WhereStarOperator


class QueryStar(Query):
    """QueryStar class. Inherits from Query class.

    This class is used to build a query using the Turtle* syntax.

    As per the documentation, this syntax only alters the WHERE clause of the query, allowing for the usage of quoted
    triple patterns and path expressions.
    """
    def __init__(self, knowledge_base, variables) -> None:
        super().__init__(knowledge_base, variables)
        
    def where(self, *args):
        if not (1 < len(args) < 4):
            raise SystemExit("Invalid number of arguments for where clause")

        self.queue.add(WhereStarOperator(*args))
        return self
