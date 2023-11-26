def create_variables(*variables: str):
    return [f"?{var}" for var in variables]