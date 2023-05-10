import streamlit as st
from llama_index import GPTVectorStoreIndex
from llama_index import StorageContext, load_index_from_storage
import os
import openai
import config

openai.api_key = os.environ["OPENAI_API_KEY"]


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
    ### Please add your own key here:
    ### os.environ['OPENAI_API_KEY'] = "add key here"


# load indices
    index = load_indexes()

    st.header('Six BOT v 1.2')

    st.write("A bot about Sixiang Wang's research on Korean and East Asian history")
    data = index

# query the selected index
    query = st.text_input('What are your questions?')
    query_engine = index.as_query_engine()
    button = st.button(f'See my answers')
    if button:
        st.write(query_engine.query(query))

if __name__ == '__main__':
    main()
