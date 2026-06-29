from qdrant_client.models import PointStruct

from app.embeddings.embedding_service import embedding_service
from app.vectorstore.qdrant_client import client

class VectorService:

    COLLECTION = "helix_functions"

    def semantic_search(
        self,
        query: str,
        limit: int = 5,
    ):
        embedding = embedding_service.generate_embedding(query)

        results = client.query_points(
            collection_name=self.COLLECTION,
            query=embedding,
            limit=limit,
        )

        return [
            {
                "score": point.score,
                "name": point.payload["name"],
                "file": point.payload["file"],
                "line": point.payload["line"],
            }
            for point in results.points
        ]

    def index_function(
        self,
        function_id: int,
        function: dict,
        file_path: str,
    ):
        embedding = embedding_service.embed_function(function)

        client.upsert(
            collection_name=self.COLLECTION,
            points=[
                PointStruct(
                    id=function_id,
                    vector=embedding,
                    payload={
                        "name": function["name"],
                        "file": file_path,
                        "line": function["line"],
                    },
                )
            ],
        )
    
    


vector_service = VectorService()
