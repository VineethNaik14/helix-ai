from pathlib import Path


class LanguageDetector:
    EXTENSIONS = {
        ".py": "Python",
        ".java": "Java",
        ".js": "JavaScript",
        ".ts": "TypeScript",
        ".cpp": "C++",
        ".c": "C",
        ".go": "Go",
        ".rs": "Rust",
        ".txt": "Text"
    }

    def detect(self, file_path: Path) -> str:
        return self.EXTENSIONS.get(file_path.suffix.lower(), "Unknown")


language_detector = LanguageDetector()
