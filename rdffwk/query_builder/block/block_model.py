from rdffwk.query_builder.abstracts import AbstractModel
from rdffwk.query_builder.block import BlockBuilder

class BlockModel(AbstractModel):
    
    def __init__(self, depth: int = 0) -> None:
        super().__init__(depth)
        
    def to_sparql(self) -> str:
        if(self.triples == [] and self.subQueries == []):
            return "{}"
        
        return BlockBuilder(self).build()