from rdffwk.query_builder.abstracts import AbstractInterface
from rdffwk.queue_builder.operators.group_operators import *
from rdffwk.queue_builder.operators.simple_operators import FromOperator
from rdffwk.queue_builder.queue import QueueOperator


class Query(AbstractInterface):
    """Wrapper class for the Query object, it provides the API for the user to build a query.
    Most methods are inherited from the AbstractInterface class.

    All methods are chainable, allowing the user to build a query in a pythonic way.

    The methods specific to the Query class are those that allow for operations on groupings. All other methods are
    shared with the Queue class.

    Example:
        kb.query("?name", "?age")
            .where("?name", ":age", "?age")
            .group_by("?name")
            .order_by("?age")
            .limit(10)
            .offset(5)
    """

    def __init__(self, knowledge_base, variables) -> None:
        super().__init__(knowledge_base)

        if variables.__class__ != tuple and variables.__class__ != list:
            variables = [variables]

        self.variables = variables

    def query(self, *args):
        if len(args) == 1 and args[0].__class__ == Query:
            self.queue.add(QueueOperator("query", args[0], False))
        else:
            self.queue.add(QueueOperator("query", Query(self.knowledge_base, args), True))
        return self

    def get_from(self, *args):
        """Adds a FromOperator to the queue.
        This operator is used to specify the graph from which the data is to be queried.

        :param args: The graph(s) to be queried.
        :return: self
        """
        self.queue.add(FromOperator(*args))
        return self

    def group_by(self, *args):
        """Adds a GroupByOperator to the queue.
        This operator is used to group the results of the query by the given variables.

        :param args: The variables to group by.
        :return: self
        """
        self.queue.add(GroupByOperator(*args))
        return self

    def order_by(self, *args):
        """Adds an OrderByOperator to the queue.
        This operator is used to order the results of the query by the given variables.

        :param args: The variables to order by.
        :return: self
        """
        self.queue.add(OrderByOperator(*args))
        return self

    def limit(self, limit: int):
        """Adds a LimitOperator to the queue.
        This operator is used to limit the number of results of the query.

        :param limit: The maximum number of results to return.
        :return: self
        """
        self.queue.add(LimitOperator(limit))
        return self

    def offset(self, offset: int):
        """Adds an OffsetOperator to the queue.
        This operator is used to offset the results of the query.

        :param offset: The number of results to skip.
        :return: self
        """
        self.queue.add(OffsetOperator(offset))
        return self

    def having(self, condition):
        """Adds a HavingOperator to the queue.
        This operator is used to filter the results of the grouped query.

        It requires that the query has been grouped by at least one variable.

        :param condition: The condition to filter by.
        :return: self
        """
        self.queue.add(HavingOperator(condition))
        return self

    def to_model(self):
        """Converts the query to a QueryModel object."""
        model = self.queue.to_query_model(self)
        return model
