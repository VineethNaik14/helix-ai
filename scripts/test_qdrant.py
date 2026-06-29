from app.vectorstore.qdrant_client import client

points, _ = client.scroll(
    collection_name="helix_functions",
    limit=10,
)

print(f"Found {len(points)} vectors\n")

for point in points:
    print(point.id)
    print(point.payload)
    print("-" * 40)
