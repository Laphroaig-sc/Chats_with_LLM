from langchain_community.vectorstores.faiss import FAISS
from langchain_community.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
 
def search_by_rag(question, serch_num=2):
    # Specify storage path.
    index_path = "/root/app/storage_server"
 
    # Loading embedded models
    embedding_model = HuggingFaceEmbeddings(
        model_name="intfloat/multilingual-e5-large"
    )
    # Loading the index
    index = FAISS.load_local(
        folder_path=index_path,
        embeddings=embedding_model,
        allow_dangerous_deserialization=True
    )
    # Get search results for RAG
    search_results = index.search(question,search_type="similarity", k=serch_num) # Get the top two search results from the INDEX
 
    return search_results
 
if __name__ == '__main__':
    q='test'
    k=2
 
    results = search_by_rag(question=q, serch_num=k)
    for i in range(k):
        print(results[i].page_content, results[i].metadata)