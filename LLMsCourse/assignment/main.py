from fastapi import FastAPI
from pydantic import BaseModel
from langchain.chains import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_openai import ChatOpenAI
from langchain_pinecone import PineconeVectorStore
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone
from dotenv import load_dotenv
import os
load_dotenv()


# 🔹 Initialize FastAPI
app = FastAPI()

# 🔹 Set API Keys
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
PINECONE_API_KEY =  os.environ['PINECONE_API_KEY']
INDEX_NAME = "pubmedqa-index"

# 🔹 Initialize Embeddings & Pinecone VectorStore
embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
vectorstore = PineconeVectorStore(index_name=INDEX_NAME, embedding=embeddings)

# 🔹 Initialize LLM (GPT-4o)
llm = ChatOpenAI(model="gpt-4o", temperature=0.2, openai_api_key=OPENAI_API_KEY)

# 🔹 Create Retrieval-Augmented Generation (RAG) Chain
system_prompt = """
You are an expert assistant for biomedical question-answering tasks. 
You will be provided with context retrieved from medical literature, specifically PubMed Open Access Articles. 
Use the provided context to directly answer the question in the most accurate and concise manner possible. 
If the context does not provide sufficient information, state that the specific details are not available in the context.
Do not include statements about limitations of the context in your response. 
Your answer should sound authoritative and professional, tailored for a medical audience.

Context:
{context}
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}"),
])

combine_docs_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(vectorstore.as_retriever(), combine_docs_chain)

# 🔹 API Request Model
class QueryRequest(BaseModel):
    question: str

# 🔹 API Endpoint
@app.post("/ask")
def ask_question(query: QueryRequest):
    """Handles incoming questions and returns answers based on PubMedQA retrieval."""
    response = rag_chain.invoke({"input": query.question})
    return {"question": query.question, "answer": response["answer"]}

# Run FastAPI Server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
