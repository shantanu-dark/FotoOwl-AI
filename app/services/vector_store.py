import os
import chromadb

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(
    name="remotion_docs"
)


def load_documents():

    folder = "data/knowledge"

    for file in os.listdir(folder):

        path = os.path.join(folder, file)

        with open(path, "r", encoding="utf-8") as f:

            text = f.read()

        collection.upsert(

            documents=[text],

            ids=[file]

        )


def retrieve(query):

    result = collection.query(

        query_texts=[query],

        n_results=3

    )

    return result["documents"][0]