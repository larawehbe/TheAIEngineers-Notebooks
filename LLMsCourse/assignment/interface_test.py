import gradio as gr
import requests

# 🔹 FastAPI Endpoint (Ensure the FastAPI server is running)
API_URL = "http://127.0.0.1:8000/ask"

# 🔹 Function to send query to FastAPI server
def query_rag(question):
    response = requests.post(API_URL, json={"question": question})
    if response.status_code == 200:
        return response.json().get("answer", "No answer found.")
    else:
        return f"Error: {response.status_code}"

# 🔹 Create Gradio Chat Interface
with gr.Blocks() as app:
    gr.Markdown("# 📚 Biomedical AI Chatbot (RAG)")
    gr.Markdown("Ask me any medical research question!")

    with gr.Row():
        chatbot = gr.Chatbot(label="Medical AI Assistant")

    with gr.Row():
        user_input = gr.Textbox(placeholder="Enter your medical research question...")
        send_button = gr.Button("Ask")

    # Function to update chat history
    def chat_response(message, history):
        answer = query_rag(message)
        history.append((message, answer))
        return history, ""

    # 🔹 Connect UI Elements
    send_button.click(chat_response, inputs=[user_input, chatbot], outputs=[chatbot, user_input])

# 🔹 Launch Gradio App
app.launch()
