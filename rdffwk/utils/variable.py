from __future__ import annotations


class Variable:
    """Represents a SPARQL variable.

    :param name: The name of the variable.
    :param f_op: If this variable has been created by an operator, then it is not a variable, but an expression.
    """

    def __init__(self, name, f_op: bool = False) -> None:
        # If this variable has been created by an operator, then it is not a variable, but an expression.
        self.name = name if f_op else f"?{name}"

    def __repr__(self) -> str:
        return self.name

    # Logical operators
    def __eq__(self, __value: object) -> Variable:
        """Returns a SPARQL expression that represents the equality between this variable and the given value.

        :param __value: The value to compare with.
        :return: The SPARQL expression.
        """
        return Variable(f"{self.name} = {__value}", True)

    def __ne__(self, __value: object) -> Variable:
        """Returns a SPARQL expression that represents the inequality between this variable and the given value.

        :param __value: The value to compare with.
        :return: The SPARQL expression.
        """
        return Variable(f"{self.name} != {__value}", True)

    def __lt__(self, __value: object):
        """Returns a SPARQL expression that represents the less than operation between this variable and the given
        value.

        :param __value: The value to compare with.
        :return: The SPARQL expression.
        """
        return Variable(f"{self.name} < {__value}", True)

    def __le__(self, __value: object):
        """Returns a SPARQL expression that represents the less than or equal operation between this variable and the
        given value.

        :param __value: The value to compare with.
        :return: The SPARQL expression.
        """
        return Variable(f"{self.name} <= {__value}", True)

    def __gt__(self, __value: object):
        """Returns a SPARQL expression that represents the greater than operation between this variable and the given

        :param __value: The value to compare with.
        :return: The SPARQL expression.
        """
        return Variable(f"{self.name} > {__value}", True)

    def __ge__(self, __value: object):
        """Returns a SPARQL expression that represents the greater than or equal operation between this variable and

        :param __value: The value to compare with.
        :return: The SPARQL expression.
        """
        return Variable(f"{self.name} >= {__value}", True)

    def __and__(self, __value: object):
        """Returns a SPARQL expression that represents the logical AND between this variable and the given value.

        :param __value: The value to conjugate with.
        :return: The SPARQL expression.
        """
        return Variable(f"({self.name}) && ({__value})", True)

    def __or__(self, __value: object):
        """Returns a SPARQL expression that represents the logical OR between this variable and the given value.

        :param __value: The value to conjugate with.
        :return: The SPARQL expression.
        """
        return Variable(f"({self.name}) || ({__value})", True)

    # Arithmetic operators

    def __add__(self, __value: object):
        """Returns a SPARQL expression that represents the addition between this variable and the given value.

        :param __value: The value to add.
        :return: The SPARQL expression.
        """
        return Variable(f"{self.name} + {__value}", True)

    def __sub__(self, __value: object):
        """Returns a SPARQL expression that represents the subtraction between this variable and the given value.

        :param __value: The value to subtract.
        :return: The SPARQL expression.
        """
        return Variable(f"{self.name} - {__value}", True)

    def __mul__(self, __value: object):
        """Returns a SPARQL expression that represents the multiplication between this variable and the given value.

        :param __value: The value to multiply by.
        :return: The SPARQL expression.
        """
        return Variable(f"{self.name} * {__value}", True)

    def __truediv__(self, __value: object):
        """Returns a SPARQL expression that represents the division between this variable and the given value.

        :param __value: The value to divide by.
        :return: The SPARQL expression.
        """
        return Variable(f"{self.name} / {__value}", True)
