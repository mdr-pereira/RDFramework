from typing import Iterable

from rdffwk.query_builder.block.block_model import BlockModel
from rdffwk.query_builder.query.query_model import QueryModel


def _add_query_to_model(model, query, set_current):
    """Adds a subquery to the model.

    If the set_current flag is set to True, this query will be placed as the current subquery. This will effectively
    mean that all subsequent operators are associated to this query.

    The up() method can be used to move back to the parent query.

    If the set_current flag is set to False, the query will be added as a subquery to the current query, maintaining the
    parent query as the current query.

    :param model: The model to add the query to.
    :param query: The query to add.
    :param set_current: A flag indicating whether the query should be set as the current query.
    """
    if set_current:
        model.add_sub_query(QueryModel(query.variables, query.get_prefixes(), parent=model, depth=model.depth + 3))
        model = model.subQueries[-1]
    else:
        model.add_sub_query(query.to_model())
        model.subQueries[-1].set_precedents(model, model.depth + 3)
    return model


def _process_queue_operator(model, node):
    """Processes a queue operator. These "meta" operators are used to control the queue.

    :param model: The current model.
    :param node: The queue operator.
    :return: The updated model.
    """
    match node.id:
        case "query":
            model = _add_query_to_model(model, node.args[0], node.args[1])
        case "up":
            if model.parent is not None:
                model = model.parent
    return model


class Queue(Iterable):
    """A queue is a list of operators that are used to build a model (query or block model).
    It's a simple wrapper around a list, with some additional functionality."""

    def __init__(self):
        self._queue = []

    def add(self, operator):
        """Adds an operator to the queue.

        :param operator: The operator to add.
        """
        self._queue.append(operator)

    def pop(self, ix=-1):
        """Pops an operator from the queue.

        :param ix: The index of the operator to pop. Defaults to the last operator.
        :return: The popped operator.
        """
        return self._queue.pop(ix)

    def __str__(self):
        """For debugging purposes, returns a string representation of the queue.

        :return: A string representation of the queue.
        """
        return str(self._queue)
    
    def __iter__(self):
        """Returns an iterator over the queue."""
        return iter(self._queue)

    def to_query_model(self, query) -> QueryModel:
        """Converts the queue to a query model. This is the default model.

        :param query: The query to add to the model.
        :return: The query model.
        """
        model = QueryModel(query.variables, query.get_prefixes())
        self._iter_all_nodes(model)
        return model
    
    def to_block_model(self, depth=0) -> BlockModel:
        """Converts the queue to a block model. This model is used create BGPs (used internally in queries).

        :param depth: The depth of the block model. This is used to determine the indentation of the model.
        :return: The block model.
        """
        model = BlockModel(depth)
        self._iter_all_nodes(model)
        return model
    
    def _iter_all_nodes(self, model):
        """Iterates over all nodes in the queue and adds them to the model.

        It also processes queue meta-operators.

        :param model: The model to add the nodes to.
        """
        for node in self._queue:
            if node.__class__ == QueueOperator:
                model = _process_queue_operator(model, node)
            else:
                node.add_to_model(model)

    def _print_item_classes(self):
        """For debugging purposes, prints all item classes in the queue."""
        print([item.__class__ for item in self._queue])
        

class QueueOperator(object):
    """A queue operator is a meta-operator that controls the queue.

    The following operators are available:
    - query: Adds a subquery to the current query. Used as we need to deal with hierarchical issues.
    - up: Moves the current query to its parent query.
    """
    
    def __init__(self, _id, *args) -> None:
        super().__init__()
        self.id = _id
        self.args = args
        