import ast
from pathlib import Path


class PythonParser:
    def parse(self, file_path: Path):
        with open(file_path, "r", encoding="utf-8") as file:
            source = file.read()

        tree = ast.parse(source)

        functions = []
        classes = []
        imports = []

        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.append(alias.name)

            elif isinstance(node, ast.ImportFrom):
                module = node.module or ""
                for alias in node.names:
                    imports.append(f"{module}.{alias.name}")

            if isinstance(node, ast.FunctionDef):
                functions.append(
                    {
                        "name": node.name,
                        "args": [arg.arg for arg in node.args.args],
                        "line": node.lineno,
                        "docstring": ast.get_docstring(node),
                    }
                )

            elif isinstance(node, ast.ClassDef):
                classes.append(
                    {
                        "name": node.name,
                        "line": node.lineno,
                        "docstring": ast.get_docstring(node),
                        "methods": [
                            child.name
                            for child in node.body
                            if isinstance(child, ast.FunctionDef)
                        ],
                    }
                )

        return {
            "functions": functions,
            "classes": classes,
            "imports": imports,
        }


python_parser = PythonParser()
