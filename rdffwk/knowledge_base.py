from typing import Any
from rdffwk.query_builder.query import Query
from rdffwk.utils import constants as const


class KnowledgeBase():

    def __init__(self, graph_name, graph_uri, prefixes=const.DEFAULT_PREFIXES) -> None:
        self._graph_name = graph_name
        self._graph_uri = graph_uri
        self._prefixes = prefixes if prefixes != None else {}

        self.shorthands = {} # {shorthand: translation}

    
    def add_prefix(self, prefix, uri):
        self.prefixes[prefix] = uri

    def add_shorthand(self, shorthand, translation):
        self._shorthands[shorthand] = translation

    def query(self, variables, query_type, query_params) -> Query:
        return Query(self, variables, query_type, query_params)


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

