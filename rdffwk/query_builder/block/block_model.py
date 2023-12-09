from __future__ import annotations

from rdffwk.query_builder.block.block_builder import BlockBuilder

class BlockModel():
    
    def __init__(self, depth: int = 0) -> None:
        self.triples = []
        self.subQueries = []
        self.filters = []
        self.bindings = []
        self.services = []
        
        self.depth = depth
        
    def add_triple(self, triple: str):
        self.triples.append(triple)
        
    def add_filter(self, filter: str):
        self.filters.append(filter)
        
    def add_bind(self, bind: str):
        self.bindings.append(bind)
        
    def add_service(self, service: str):
        self.services.append(service)
        
    def add_sub_query(self, query: BlockModel):
        self.subQueries.append(query)
        
    def to_sparql(self) -> str:
        if(self.triples == [] and self.subQueries == []):
            return "{}"
        
        return BlockBuilder(self).build()
    
    def __repr__(self) -> str:
        return self.to_sparql()