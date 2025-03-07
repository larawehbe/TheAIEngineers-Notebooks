from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.memory import ConversationBufferMemory


load_dotenv()

@tool
def run_python_code(code: str ) -> str:
    """Run a python code"""
    try:
        exec_globals = {}
        exec(code, exec_globals)
        return str(exec_globals.get("result" , "Code Executed Successfully"))
    except Exception as e : 
        return f"Error: {e}"
    
tools = [run_python_code, TavilySearchResults()]

prompt = ChatPromptTemplate.from_messages(
    [
        ("system" , "You are a helpful coding assistant. Use tools when needed"),
        ("placeholder", "{chat_history}"),
        ("human", "{input}"),
        ("placeholder" , "{agent_scratchpad}")
    ]
)

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

agent = create_tool_calling_agent(llm, tools, prompt)

agent_executor = AgentExecutor(
    agent = agent,
    tools = tools,
    memory = memory,
    verbose=True
)

def coding_assistant(message, history):
    response = agent_executor.invoke({"input" :message})
    return response['output']
if __name__ == "__main__":
    import gradio as gr
    iface = gr.ChatInterface(
        fn = coding_assistant,
        title="💬 Coding Assistant Chat",
        description="Chat with an AI that can execute Python code, debug, and search!",
    )
    iface.launch()