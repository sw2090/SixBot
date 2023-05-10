import streamlit as st
from llama_index import GPTVectorStoreIndex
from llama_index import StorageContext, load_index_from_storage
import os

import config

os.environ['OPENAI_API_KEY'] = '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'



@st.cache_resource
def load_indexes():
    """load the pipeline object for preprocessing and the ml model"""
    
    # rebuild storage context
    storage_context = StorageContext.from_defaults(persist_dir="./storage")

    # load index
    index = load_index_from_storage(storage_context)
    return index


def main():

# api key
    os.environ['OPENAI_API_KEY'] = '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'

# load indices
    index = load_indexes()

    st.header('Six BOT v 1.2')

    st.write("Ask me about Sixiang Wang's research on Korean and East Asian history")
    data = index

# query the selected index
    query = st.text_input('Enter Your Query')
    query_engine = index.as_query_engine()
    button = st.button(f'Respond')
    if button:
        st.write(query_engine.query(query))

if __name__ == '__main__':
    main()
