import importlib
import re

def get_table_columns(table_name):
    module_name = f"gestion_{table_name}"
    module = importlib.import_module(module_name)
    
    # Get the function by its name
    add_function_name = f"ajouter_{table_name}"
    add_function = getattr(module, add_function_name, None)
    
    if not add_function:
        raise ValueError(f"No function named {add_function_name} in {module_name}")
    
    # Extract function source code
    source_code = inspect.getsource(add_function)
    
    # Use regular expressions to extract columns
    match = re.search(r"INSERT INTO \w+ \(([^)]+)\)", source_code)
    if not match:
        raise ValueError(f"Could not find INSERT INTO statement in {add_function_name}")
    
    columns = match.group(1).split(',')
    columns = [column.strip() for column in columns]
    
    return columns
