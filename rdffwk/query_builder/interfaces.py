class BlockInterface():
    def query(self, *args):
        pass

    def where(self, *args):
        pass

    def filter(self, condition):
        pass

    def service(self, url, query):
        pass

    def bind(self, var, as_var):
        pass

    def cache(self):
        pass

    def to_sparql(self):
        pass


class QueryInterface(BlockInterface):
    def group_by(self, *args):
        pass

    def limit(self, limit: int):
        pass

    def offset(self, offset: int):
        pass

    def having(self, condition):
        pass
