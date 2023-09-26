import os

# Discovering modules
module_names = [f.split('.')[0] for f in os.listdir('/Users/lapiscine/Documents/WCS/python_caspar/idrv3') if f.startswith('gestion_') and f.endswith('.py')]
print(module_names)

modules = {}
for module_name in module_names:
    module = __import__(module_name)
    modules[module_name] = module

# Filtering out standard attributes of modules
standard_attrs = set(dir(object))

from flask import Blueprint

main = Blueprint('main', __name__)

for module_name, module in modules.items():
    for function_name, function in vars(module).items():
        if function_name not in standard_attrs and callable(function):
            # Create a unique route name
            unique_route_name = f"/{module_name}/{function_name}"
            print(f"Creating route for: {unique_route_name}")

            @main.route(unique_route_name, methods=['GET', 'POST'])
            def dynamic_route():
                return function()
