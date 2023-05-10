                
import os
os.environ['OPENAI_API_KEY'] = "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"

import logging
import sys


# Load you data into 'Documents' 

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, load_index_from_storage, StorageContext
from IPython.display import Markdown, display


# Load Data

documents = SimpleDirectoryReader('./data').load_data()


index = GPTVectorStoreIndex.from_documents(documents)


# save index to disk
index.set_index_id("vector_index")
index.storage_context.persist('storage')

