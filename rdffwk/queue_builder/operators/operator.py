
class Operator:

    def __init__(self, id):
        self.id = id

    def __str__(self):
        return self.id
    
    def __repr__(self):
        raise NotImplementedError("This method must be implemented by the subclass")
    
    def add_to_model(self, _) -> None:
        """Abstract method that must be implemented by the subclass. It must call the appropiate method of the model to add the operator to the model.

        Args:
            _ (_type_): _description_

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError("This method must be implemented by the subclass")
    
    
