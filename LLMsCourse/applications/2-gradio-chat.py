import openai
import gradio as gr

# Configure the OpenAI client
client = openai.OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="nokeyneeded",
)

# Function to interact with the model
def chat_with_model(history, new_message):
    try:
        # Build the conversation history in the required format
        messages = [{"role": "system", "content": "You are a helpful assistant."}]
        for user_message, assistant_response in history:
            messages.append({"role": "user", "content": user_message})
            messages.append({"role": "assistant", "content": assistant_response})
        
        # Add the new user message
        messages.append({"role": "user", "content": new_message})
        
        # Send the request to the model
        response = client.chat.completions.create(
            model="phi:latest",
            temperature=0.7,
            n=1,
            messages=messages,
        )
        
        # Extract the response
        assistant_message = response.choices[0].message.content
        history.append((new_message, assistant_message))
        return history, ""
    except Exception as e:
        history.append((new_message, f"Error: {str(e)}"))
        return history, ""

# Gradio Interface
def gradio_chat_app():
    with gr.Blocks() as app:
        gr.Markdown("# Ollama Phi Model Chat Interface")
        gr.Markdown("Chat with the Phi model in a conversational format.")

        chatbot = gr.Chatbot(label="Chat Interface")
        user_input = gr.Textbox(label="Your Message", placeholder="Type something...", lines=1)
        send_button = gr.Button("Send")
        
        # Chat functionality
        def clear_chat():
            return [], ""

        clear_button = gr.Button("Clear Chat")

        # Event handling
        send_button.click(
            fn=chat_with_model,
            inputs=[chatbot, user_input],
            outputs=[chatbot, user_input],
        )
        clear_button.click(
            fn=clear_chat,
            inputs=[],
            outputs=[chatbot, user_input],
        )

    return app

# Launch the app
if __name__ == "__main__":
    app = gradio_chat_app()
    app.launch()
