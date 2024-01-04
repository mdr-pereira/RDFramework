from copy import deepcopy

from rdffwk.queue_builder.operators.simple_operators import *
from rdffwk.queue_builder.queue import Queue, QueueOperator


class AbstractInterface(object):
    """Abstract class that defines the interface for the Query and Queue classes.
    It provides the API for the user to build a query and all internal BGPs of the query.

    All methods are chainable, allowing the user to build a query in a pythonic way.

    The methods here included are those that allow for operations on the internal BGPs of the query, not allowing those
    that operate on the groupings. Those methods are defined in the Query class.
    """
    def __init__(self, knowledge_base) -> None:
        self.knowledge_base = knowledge_base
        self.queue = Queue()
        
    def query(self, _):
        """Adds a QueryOperator to the queue.
        This operator declares a subquery to be executed.

        :param _: The subquery to be executed.
        :return: self
        """
        raise NotImplementedError("Abstract method")
        
    def where(self, *args):
        """Adds a WhereOperator to the queue.
        This operator is used to specify triple patterns to be queried.

        This operator can be used in many ways:
            - where("?s :p ?o")
            - where("?s", ":p", "?o")
            - where("?s", [(":p1", "?o1"), (":p2", "?o2")])
            - where("?s, ":p", ["?o1", "?o2"])
            - where("?s", [":p1", ":p2"], "?o")

        :param args: The triple patterns to be queried.
        :return: self
        """
        if not (1 < len(args) < 3):
            raise SystemExit("Invalid number of arguments for where clause")
    
        self.queue.add(WhereOperator(*args))
        return self
    
    def filter(self, condition):
        """Adds a FilterOperator to the queue.
        This operator is used to filter the results of the query.

        :param condition: The condition to be applied.
        :return: self
        """
        self.queue.add(FilterOperator(condition))
        return self
    
    def filter_exists(self, block, negation=False):
        """Adds a FilterExistsOperator to the queue.
        This operator is a specific case of the FilterOperator, and is used to filter based on the existence of a triple
        pattern.

        This operator is superfluous, as it can be achieved with the FilterOperator, but it is included for convenience.

        :param block: The triple pattern to be checked.
        :param negation: Whether the triple pattern should exist or not.
        :return: self
        """
        self.queue.add(FilterExistsOperator(block, negation))
        return self
    
    def filter_not_exists(self, block):
        """Adds a FilterExistsOperator to the queue.
        This operator is a specific case of the FilterExistsOperator, and is used to filter based on the non-existence
        of a triple pattern.

        This operator is superfluous, as it can be achieved with the FilterExistsOperator, but it is included for
        convenience.

        :param block: The triple pattern to be checked.
        :return: self
        """
        self.queue.add(FilterExistsOperator(block, True))
        return self
    
    def filter_in(self, var, values, negation=False):
        """Adds a FilterInOperator to the queue.
        This operator is a specific case of the FilterOperator, and is used to filter based on the values of a variable.

        This operator is superfluous, as it can be achieved with the FilterOperator, but it is included for convenience.

        :param var: The variable to be checked.
        :param values: The values to check against.
        :param negation: Whether the variable should have one of the values or not.
        :return: self
        """
        self.queue.add(FilterInOperator(var, values, negation))
        return self
    
    def filter_not_in(self, var, values):
        """Adds a FilterInOperator to the queue.
        This operator is a specific case of the FilterInOperator, and is used to filter based on the non-existence of

        This operator is superfluous, as it can be achieved with the FilterInOperator, but it is included for
        convenience.

        :param var: The variable to be checked.
        :param values: The values to check against.
        :return: self
        """
        self.queue.add(FilterInOperator(var, values, True))
        return self
    
    def optional(self, block):
        """Adds an OptionalOperator to the queue.
        This operator is used to specify triple patterns that are optional.

        :param block: The triple patterns to be queried.
        :return: self
        """
        self.queue.add(OptionalOperator(block))
        return self
    
    def union(self, block1, block2):
        """Adds a UnionOperator to the queue.
        This operator is used to specify the union of two blocks.

        The blocks can be either a single triple pattern or a BGP.

        :param block1: The first block.
        :param block2: The second block.
        :return: self
        """
        self.queue.add(UnionOperator(block1, block2))
        return self
    
    def minus(self, block):
        """Adds a MinusOperator to the queue.
        This operator is used to specify the difference between a query and a block.

        The block can be either a single triple pattern or a BGP.

        :param block: The block to be subtracted.
        :return: self
        """
        self.queue.add(MinusOperator(block))
        return self
    
    def graph(self, graph, group):
        """Adds a GraphOperator to the queue.
        This operator is used to specify the graph from which the data is to be queried.

        :param graph: The graph to be queried.
        :param group: The group to be queried.
        :return: self
        """
        self.queue.add(GraphOperator(graph, group))
        return self
    
    def service(self, url, block):
        """Adds a ServiceOperator to the queue.
        This operator is used to specify a service from which a query is to be executed.

        :param url: The url of the service to be queried.
        :param block: The query to be executed.
        :return: self
        """
        self.queue.add(ServiceOperator(url, block))
        return self
    
    def values(self, var, values):
        """Adds a ValuesOperator to the queue.
        This operator is a shorthand used to define a set of values for a variable.

        :param var: The variable to be defined.
        :param values: The values from which the variable may take.
        :return: self
        """
        self.queue.add(ValuesOperator(var, values))
        return self
    
    def bind(self, expr, as_var):
        """Adds a BindOperator to the queue.
        This operator is used to bind an expression to a variable.

        :param expr: The expression to be bound.
        :param as_var: The variable to bind to.
        :return: self
        """
        self.queue.add(BindOperator(expr, as_var))
        return self
    
    def get_prefixes(self):
        """Returns the prefixes of the query.

        :return: The prefixes of the query.
        """
        return self.knowledge_base.prefixes
    
    def cache(self):
        """This method is used to cache the query.
        This allows the user to reuse the query without having to rebuild it.

        If this method is not called then whenever the query is affected by an operator, it will alter all other
        instances of it.

        :return: A copy of the query.
        """
        return deepcopy(self)
    
    def up(self):
        """This method is used to go up one level in the query.
        Useful whenever sub-queries are used, or even blocks, as they can block access to the parent query.

        :return: self
        """
        self.queue.add(QueueOperator("up"))
        return self
    
    def to_model(self):
        """Returns the query as a model. (ABSTRACT)"""
        raise NotImplementedError("Abstract method")
    
    def to_sparql(self):
        """This method returns the current query as a SPARQL query string.
        It's the central method of the class, as it allows the user to get the query in a format that can be executed.

        :return: The query as a SPARQL query string.
        """
        return self.to_model().to_sparql()
    
    def __str__(self) -> str:
        return str(self.queue)
    
    def __repr__(self) -> str:
        return self.to_sparql()
