from rdffwk.knowledge_base import KnowledgeBase
from rdffwk.query_builder.block.block_star import BlockStar
from rdffwk.query_builder.query.query_star import QueryStar
from typing import Union


class KnowledgeBaseStar(KnowledgeBase):
    """A knowledge base that uses Turtle* syntax.

    This class is a subclass of KnowledgeBase, but it uses Turtle* syntax instead of vanilla Turtle syntax.
    Turtle* syntax is a superset of Turtle syntax, so it is possible to use Turtle* syntax in a Turtle knowledge base.

    :param graph_name: Name of the graph
    :type graph_name: str
    :param graph_uri: URI of the graph
    :type graph_uri: str
    :param prefixes: A dictionary containing prefixes
    :type prefixes: dict
    """

    def __init__(self, graph_name=None, graph_uri=None, prefixes=None) -> None:
        super().__init__(graph_name, graph_uri, prefixes)
        
    def query(self, *variables) -> QueryStar:
        """Creates a query object.

        :param variables: Any number of variables
        :type variables: str | Variable
        :return: A query object that uses Turtle* syntax
        """
        return QueryStar(self, variables)
    
    def block(self) -> BlockStar:
        """Creates a block object.

        :return: A block object that uses Turtle* syntax
        """
        return BlockStar(self)
    
    @staticmethod
    def create_quoted_triple(subj, pred, obj) -> tuple:
        """Creates a quoted triple from the Turtle* syntax.
        
        This method is not really needed, but it provides an easy-to-read way to create quoted triples.

        :param subj: Subject of the triple
        :type subj: str | Variable
        :param pred: Predicate of the triple
        :type pred: str | Variable
        :param obj: Object of the triple
        :type obj: str | Variable
        :return: A tuple containing the quoted triple
        """
        return subj, pred, obj
    
    
    