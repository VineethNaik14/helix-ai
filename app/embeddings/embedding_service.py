from sentence_transformers import SentenceTransformer


class EmbeddingService:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def generate_embedding(self, text: str):
        embedding = self.model.encode(text)
        return embedding.tolist()

    def embed_function(self, function: dict):
        text = f"""
        Function Name: {function["name"]}

        Arguments: {", ".join(function["args"])}

        Return Type: {function["return_type"]}

        Docstring:
        {function["docstring"]}
        """

        return self.generate_embedding(text)


embedding_service = EmbeddingService()
