def NOT(expr) -> str :
    return f"NOT {expr}"

def EXISTS(expr) -> str :
    return f"EXISTS {{{expr}}}"

def ASC(expr) -> str :
    return f"ASC({expr})"

def DESC(expr) -> str :
    return f"DESC({expr})"

def COUNT(expr) -> str :
    return f"COUNT({expr})"

def SUM(expr) -> str :
    return f"SUM({expr})"

def AS(expr, alias) -> str :
    return f"{expr} AS {alias}"