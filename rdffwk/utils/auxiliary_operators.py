from __future__ import annotations

from typing import Tuple, List

from .variable import Variable

"""This module contains auxiliary operators that can be used in the query and block objects.

These operators return either strings or Variable representations of the resulting expressions, when those may
be used in subsequent expressions.

Example:
    STR("foo") -> "\"foo\""
    NOT("bar") -> "NOT bar"
    EXISTS("foobar") -> "EXISTS foobar"
"""


def STR(expr: str | Variable) -> str:
    """Returns a string representation of the expression. 
    Used to surround variables and strings with quotes.

    :param expr: The expression to be surrounded with quotes
    :return: The expression surrounded with quotes
    """
    return f"\"{expr}\""


def NOT(expr: str | Variable) -> Variable:
    """Returns the SPARQL negation of the expression.

    :param expr: The expression to be negated
    :return: The negated expression
    """
    return _solve_for_var("NOT", expr, False)


def EXISTS(expr: str | Variable) -> Variable:
    """Returns the SPARQL EXISTS clause using the expression.

    :param expr: The expression to be used in the EXISTS clause
    :return: The expression surrounded with EXISTS
    """
    return _solve_for_var("EXISTS", expr, False)


def IN(var: str | Variable, values: str | Tuple | List) -> str:
    """Returns the SPARQL IN clause using the variable and values.

    :param var: The variable to be used in the IN clause
    :param values: The values to be used in the IN clause
    :return: SPARQL IN clause using the variable and values
    """
    if values.__class__ == tuple or values.__class__ == list:
        values = ", ".join([STR(v) for v in values])

    return f"{var} IN ({values})"


def AS(expr: str | Variable, alias: str | Variable) -> str:
    """Returns the SPARQL AS modifier using the expression and alias.

    :param expr: The expression to be used in the AS clause
    :param alias: The alias to be used in the AS clause
    :return: SPARQL AS modifier using the expression and alias
    """
    return f"({expr} AS {alias})"


def LANG(expr: str | Variable) -> Variable:
    """Returns the SPARQL LANG modifier using the expression.

    :param expr: The expression to be used in the LANG clause
    :return: SPARQL LANG modifier using the expression
    """
    return _solve_for_var("LANG", expr)


def ASC(expr: str | Variable) -> Variable:
    """Returns the SPARQL ASC modifier using the expression.

    :param expr: The expression to be used in the ASC clause
    :return: SPARQL ASC modifier using the expression
    """
    return _solve_for_var("ASC", expr)


def DESC(expr: str | Variable) -> Variable:
    """Returns the SPARQL DESC modifier using the expression.

    :param expr: The expression to be used in the DESC clause
    :return: SPARQL DESC modifier using the expression
    """
    return _solve_for_var("DESC", expr)


def COUNT(expr: str | Variable) -> Variable:
    """Returns the SPARQL COUNT operation using the expression.

    :param expr: The expression to be used in the COUNT clause
    :return: SPARQL COUNT operation using the expression
    """
    return _solve_for_var("COUNT", expr)


def SUM(expr: str | Variable) -> Variable:
    """Returns the SPARQL SUM operation using the expression.

    :param expr: The expression to be used in the SUM clause
    :return: SPARQL SUM operation using the expression
    """
    return _solve_for_var("SUM", expr)


def DISTINCT(*expr: str | Variable) -> Variable | str:
    """Returns the SPARQL DISTINCT modifier using the expression.

    :param expr: The expressions to be used in the DISTINCT clause
    :return: SPARQL DISTINCT modifier using the expression
    """
    return f"DISTINCT {' '.join([str(e) for e in expr])}"


def REDUCED(expr: str | Variable) -> Variable:
    """Returns the SPARQL REDUCED modifier using the expression.

    :param expr: The expression to be used in the REDUCED clause
    :return: SPARQL REDUCED modifier using the expression
    """
    return _solve_for_var("REDUCED", expr)


def _solve_for_var(op: str, expr: str | Variable, parenthesis=True) -> Variable:
    """Returns a Variable representation of the expression using the given operator.

    :param op: The operator to be used
    :param expr: The expression to be used
    :param parenthesis: Whether to surround the expression with parenthesis
    :return: A Variable representation of the expression using the given operator
    """
    new_expr = f"{op}({expr})" if parenthesis else f"{op}{expr}"
    return Variable(new_expr, True)
