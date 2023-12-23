from rdffwk.query_builder.block.block import Block
from rdffwk.query_builder.query.query import Query
from rdffwk.utils.variable import Variable
from rdffwk.utils.constants import DEFAULT_PREFIXES

from typing import List


class KnowledgeBase(object):
    """The main class of the library. It is used to represent a knowledge base, ie. a store of information in the form
    of RDF triples.

    It may be used to create queries and blocks, and to add prefixes to the knowledge base.

    :param graph_name: The name of the graph, defaults to None
    :type graph_name: str, optional
    :param graph_uri: The uri of the graph, defaults to None
    :type graph_uri: str, optional
    :param prefixes: A dictionary of prefixes, defaults to DEFAULT_PREFIXES
    :type prefixes: dict, optional
    """

    def __init__(self, graph_name=None, graph_uri=None, prefixes=DEFAULT_PREFIXES) -> None:
        super().__init__()
        
        self._graph_name = graph_name
        self._graph_uri = graph_uri
        self._prefixes = prefixes if prefixes is not None else {}
    
    def add_prefix(self, prefix: str, uri: str):
        """Adds a prefix to the knowledge base.

        Args:
            prefix (str): The shorthand of the uri, e.g. "rdf"
            uri (str): The uri, e.g. "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
        """
        self.prefixes[prefix] = uri
        
    def create_variables(self, *variables: str) -> List[Variable]:
        """Creates a list of variables from a list of strings. Also accepts a single string.

        Returns:
            List[Variable]: A list of variables
        """
        return [Variable(var) for var in variables]

    def query(self, *variables) -> Query:
        """Creates a query object.

        Returns:
            Query: A query object
        """
        return Query(self, variables)
    
    def block(self) -> Block:
        """Creates a block object.

        Returns:
            Block: A block object
        """
        return Block(self)


    #Getters and setters
    @property
    def graph_name(self):
        return self._graph_name
    
    @graph_name.setter
    def graph_name(self, _):
        raise AttributeError("Cannot change attribute graph_name")
    
    @property
    def graph_uri(self):
        return self._graph_uri
    
    @graph_uri.setter
    def graph_uri(self, _):
        raise AttributeError("Cannot change attribute graph_uri")
    
    @property
    def prefixes(self):
        return self._prefixes
    
    @prefixes.setter
    def prefixes(self, prefixes):
        self._prefixes.update(prefixes)

