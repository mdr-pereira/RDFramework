
class QueryModel():

    def __init__(self) -> None:
        self._prefixes = {} # {prefix: uri}

        self.variables = []
        self._query = None
        self._query_type = None
        self._query_params = None

     