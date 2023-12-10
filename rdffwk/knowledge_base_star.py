from rdffwk.knowledge_base import KnowledgeBase
from rdffwk.query_builder.block.block_star import BlockStar
from rdffwk.query_builder.query.query_star import QueryStar


class KnowledgeBaseStar(KnowledgeBase):
    
    def __init__(self, graph_name=None, graph_uri=None, prefixes=None) -> None:
        super().__init__(graph_name, graph_uri, prefixes)
        
    def query(self, *variables) -> QueryStar:
        return QueryStar(self, variables)
    
    def block(self) -> BlockStar:
        return BlockStar(self)
    
    def create_quoted_triple(self, subj, pred, obj):
        return (subj, pred, obj)
    
    
    