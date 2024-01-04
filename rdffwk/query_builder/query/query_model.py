from rdffwk.query_builder.abstracts import AbstractModel
from rdffwk.query_builder.query.query_builder import QueryBuilder


class QueryModel(AbstractModel):
    """Query model, an extension of the AbstractModel.
    This class represents a query, and acts as an aggregate for all the operators that make up the query.

    The superclass, AbstractModel holds all other aggregate operators which are common to both the query and the block.

    Not all operators are specific to the SPARQL query language, so this framework could very possibly be extended
    to other query languages, such as Cypher.
    """

    def __init__(self, variables, prefixes, parent=None, depth: int = 0) -> None:
        super().__init__(parent, depth)

        self.prefixes = prefixes
        self.variables = variables

        self.from_uri = None

        self.grouping = None
        self.ordering = None
        self.limit = None
        self.offset = None

    def set_from(self, uri):
        """Adds a URI to be used in the FROM clause of the query.

        :param uri: The URI to be set.
        """
        self.from_uri = uri

    def set_grouping(self, variables):
        """Sets the variables which will be used in the GROUP BY clause of the query.

        :param variables: The variables to be set.
        """
        self.grouping = variables

    def set_order_by(self, variables):
        """Sets the variables which will be used in the ORDER BY clause of the query.

        :param variables: The variables to be set.
        """
        self.ordering = variables

    def add_having(self, condition: str):
        """Adds a HAVING condition to the query.

        :param condition: The condition to be added.
        """
        self.having.append(condition)

    def set_limit(self, limit: str):
        """Sets the limit of the query.

        :param limit: The limit to be set.
        """
        self.limit = limit

    def set_offset(self, offset: str):
        """Sets the offset of the query.

        :param offset: The offset to be set.
        """
        self.offset = offset

    def to_sparql(self) -> str:
        """Returns the SPARQL representation of the query.
        Internally, this method calls the QueryBuilder class to build the query.

        :return: The SPARQL representation of the query.
        """
        if self.triples == [] and self.subQueries == []:
            raise SystemExit("No triples or sub-queries in query")

        return QueryBuilder(self).build()
