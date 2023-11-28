from rdffwk.utils.variable import Variable


def create_variables(*variables: str):
    return [Variable(var) for var in variables]