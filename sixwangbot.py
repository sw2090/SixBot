                
import os
os.environ['OPENAI_API_KEY'] = "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"


# Load you data into 'Documents' a custom type by LlamaIndex

from llama_index import SimpleDirectoryReader

documents = SimpleDirectoryReader('./data').load_data()

from llama_index import GPTVectorStoreIndex

index = GPTVectorStoreIndex.from_documents(documents)


# Query your index!
query_engine = index.as_query_engine()
response = query_engine.query("what are the articles about?")
print(response)

