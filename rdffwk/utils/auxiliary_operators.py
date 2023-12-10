from .variable import Variable

def STR(expr) -> str :
    return f"\"{expr}\""

def NOT(expr) -> Variable | str :
    return _solve_for_var("NOT", expr)

def EXISTS(expr) -> str:
    return f"EXISTS {expr}"

def IN(var, values) -> Variable | str :
    if values.__class__ == tuple or values.__class__ == list:
        values = ", ".join([str(v) for v in values])
        
    return f"{var} IN ({values})"

def AS(expr, alias) -> Variable | str :
    return f"({expr} AS {alias})"

def LANG(expr) -> Variable | str :
    return _solve_for_var("LANG", expr)

def ASC(expr) -> Variable | str:
    return _solve_for_var("ASC", expr)

def DESC(expr) -> Variable | str :
    return _solve_for_var("DESC", expr)

def COUNT(expr) -> Variable | str :
    return _solve_for_var("COUNT", expr)

def SUM(expr) -> Variable | str :
    return _solve_for_var("SUM", expr)

def DISTINCT(*expr) -> Variable | str :
    return f"DISTINCT {' '.join([str(e) for e in expr])}"

def REDUCED(expr) -> Variable | str :
    return _solve_for_var("REDUCED", expr)

def _solve_for_var(op, expr) -> Variable | str:
    if expr.__class__ == Variable:
        return Variable(f"{op}({expr})", True)
    
    return f"{op}({expr})"