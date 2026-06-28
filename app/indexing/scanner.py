from pathlib import Path

from app.indexing.language_detector import language_detector
from app.parsers.python_parser import python_parser
from app.graphs.dependency_graph import dependency_graph


class RepositoryScanner:
    IGNORE_DIRS = {
        ".git",
        ".venv",
        "venv",
        "__pycache__",
        "node_modules",
        "dist",
        "build",
    }

    def scan(self, repository_path: str):
        root = Path(repository_path)

        if not root.exists():
            raise FileNotFoundError(f"Repository not found: {repository_path}")

        files = []
        total_size = 0
        language_distribution = {}
        python_metadata = {}

        for path in root.rglob("*"):
            # Skip ignored directories
            if any(part in self.IGNORE_DIRS for part in path.parts):
                continue

            if path.is_file():
                files.append(path)
                total_size += path.stat().st_size

                language = language_detector.detect(path)
                language_distribution[language] = (
                    language_distribution.get(language, 0) + 1
                )

                if language == "Python":
                    try:
                        python_metadata[str(path.relative_to(root))] = (
                            python_parser.parse(path)
                        )
                    except Exception:
                        pass

        graph = dependency_graph.build(python_metadata)

        return {
            "name": root.name,
            "path": str(root.resolve()),
            "total_files": len(files),
            "total_size_bytes": total_size,
            "languages": language_distribution,
            "files": [str(file.relative_to(root)) for file in files],
            "python_metadata": python_metadata,
            "dependency_graph": graph,
        }


repository_scanner = RepositoryScanner()
