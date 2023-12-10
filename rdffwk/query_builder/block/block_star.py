from rdffwk.query_builder.block.block import Block
from rdffwk.query_builder.query.query_star import QueryStar


class BlockStar(Block):
    def __init__(self, knowledge_base) -> None:
        super().__init__(knowledge_base)
        
    def query(self, *variables):
        return QueryStar(self.knowledge_base, variables)
    
    def block(self):
        return BlockStar(self.knowledge_base)