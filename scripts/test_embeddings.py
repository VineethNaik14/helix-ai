from app.embeddings.embedding_service import embedding_service

function = {
    "name": "scan",
    "args": ["self", "repository_path"],
    "return_type": "dict",
    "docstring": "Scans a repository recursively.",
}

embedding = embedding_service.embed_function(function)

print(len(embedding))
print(embedding[:10])
