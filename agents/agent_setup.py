from langchain.agents import initialize_agent, Tool
from langchain.chat_models import ChatOpenAI
from agents.tools import fraud_prediction_tool

tools = [
    Tool(
        name="Fraud Prediction Tool",
        func=fraud_prediction_tool,
        description="Predict fraud probability of a transaction"
    )
]

llm = ChatOpenAI(temperature=0)

agent = initialize_agent(
    tools,
    llm,
    agent="zero-shot-react-description",
    verbose=True
)