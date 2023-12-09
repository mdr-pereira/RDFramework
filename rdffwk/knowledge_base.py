from rdffwk.query_builder.block.block import Block
from rdffwk.query_builder.query.query import Query
from rdffwk.utils import constants as const


class KnowledgeBase(object):

    def __init__(self, graph_name=None, graph_uri=None, prefixes=const.DEFAULT_PREFIXES) -> None:
        super().__init__()
        
        self._graph_name = graph_name
        self._graph_uri = graph_uri
        self._prefixes = prefixes if prefixes != None else {}
    
    def add_prefix(self, prefix, uri):
        self.prefixes[prefix] = uri

    def query(self, *variables) -> Query:
        return Query(self, variables)
    
    def block(self) -> Block:
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

