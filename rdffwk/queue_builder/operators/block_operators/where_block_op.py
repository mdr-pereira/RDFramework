

class WhereBlockOperator(object):
    
    def __init__(self, block):
        super().__init__()
        self.block = block
        
    def __repr__(self):
        return f"{{ {self.block} }}"
    
    def add_to_model(self, model):
        model.add_block(self.block)