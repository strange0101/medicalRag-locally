import streamlit as st
import os
from utils.build_graph import build_medical_graph
from utils.hybrid_retriever import create_vectorstore_from_text, get_vector_results
from pyvis.network import Network
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_community.llms import Ollama
import streamlit.components.v1 as components

# Set page config
st.set_page_config(page_title="Medical Hybrid RAG", layout="wide")

MODEL = "llama2"  # Change if you pull a different model in Ollama

st.title("🩺 Medical Hybrid RAG (Local, No API Key)")
st.markdown("**Disclaimer:** Educational demo only. Not medical advice.")

# Load medical data
with open("data/medical_data.txt", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

# Sidebar: Build Vector DB
if st.sidebar.button("(Re)build vector DB"):
    create_vectorstore_from_text(lines)
    st.sidebar.success("Vector DB created.")

# Load Vector DB
try:
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectordb = Chroma(persist_directory="chromadb_dir", embedding_function=embeddings)
except:
    vectordb = None

# Build Knowledge Graph
G = build_medical_graph()

col1, col2 = st.columns([2, 1])

with col1:
    query = st.text_input("Ask a medical question:", "")
    k = st.slider("Vector results", 1, 6, 4)

    if st.button("Search") and query.strip():
        if not vectordb:
            st.error("No Vector DB found. Build it first.")
        else:
            # Vector results
            docs = get_vector_results(vectordb, query, k)
            vector_text = "\n\n".join([d.page_content for d in docs])

            # Graph search
            matched_nodes = [node for node in G.nodes() if node.lower() in query.lower()]
            graph_results = set()
            for node in matched_nodes:
                graph_results.update(list(G.neighbors(node)))

            # Combine context
            context = f"Vector:\n{vector_text}\n\nGraph:\n{', '.join(graph_results)}"

            # Local LLM via Ollama
            llm = Ollama(model=MODEL)
            answer = llm.predict(
                f"Use the following medical context to answer:\n{context}\nQuestion: {query}"
            )

            st.subheader("🔎 Answer")
            st.write(answer)

            st.subheader("📚 Retrieved Chunks")
            for i, d in enumerate(docs):
                st.markdown(f"**Chunk {i+1}:** {d.page_content}")

with col2:
    st.subheader("Knowledge Graph")
    net = Network(height="650px", width="100%", notebook=False)
    color_map = {"disease": "#e63946", "symptom": "#ffd166", "treatment": "#2a9d8f"}
    for node in G.nodes():
        ntype = G.nodes[node].get("type", "symptom")
        net.add_node(node, label=node, color=color_map.get(ntype, "#cccccc"))
    for u, v, d in G.edges(data=True):
        net.add_edge(u, v, title=d.get("relation", ""))
    net.repulsion(node_distance=120)
    net.save_graph("graph.html")
    with open("graph.html", "r", encoding="utf-8") as f:
        components.html(f.read(), height=650, scrolling=True)


