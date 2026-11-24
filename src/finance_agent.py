
from langchain_core.messages import SystemMessage, HumanMessage, ToolMessage
from pathlib import Path
from dotenv import load_dotenv

# Загружаем API-ключ из корневой папки проекта
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path, override=True)

from langchain_openai import ChatOpenAI
from langchain_core.tools import tool

from src.finance_tools import (
    calculate_monthly_savings,
    project_savings,
    check_savings_goal
)

# Создаём модель
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# Регистрируем финансовые инструменты
@tool
def monthly_savings_tool(income: float, expenses: float) -> dict:
    """Calculate monthly savings from income and expenses."""
    return calculate_monthly_savings(income, expenses)


@tool
def project_savings_tool(monthly_savings: float, months: int) -> dict:
    """Calculate total savings over several months."""
    return project_savings(monthly_savings, months)


@tool
def savings_goal_tool(
    monthly_savings: float,
    months: int,
    savings_goal: float
) -> dict:
    """Check whether a savings goal is achievable."""
    return check_savings_goal(monthly_savings, months, savings_goal)


# Передаём инструменты модели
tools = [
    monthly_savings_tool,
    project_savings_tool,
    savings_goal_tool
]

llm_with_tools = llm.bind_tools(tools)


# Запускаем финансового агента
def run_finance_agent(user_request: str, max_steps: int = 5) -> str:
    messages = [
        SystemMessage(
            content=(
                "You are a personal finance assistant. "
                "Use the available tools for financial calculations. "
                "Explain the results in simple language. "
                "Do not invent financial numbers. "
                "Only use the three registered finance calculation tools. "
                "Never transfer money, access bank accounts, or make payments. "
                "Never perform actions that change the user's financial data."
            )
        ),
        HumanMessage(content=user_request)
    ]

    tools_by_name = {tool.name: tool for tool in tools}

    allowed_tools = {
        "monthly_savings_tool",
        "project_savings_tool",
        "savings_goal_tool"
    }

    for step in range(max_steps):
        response = llm_with_tools.invoke(messages)
        messages.append(response)

        if not response.tool_calls:
            return response.content

        for tool_call in response.tool_calls:
            tool_name = tool_call["name"]

            if tool_name not in allowed_tools:
                messages.append(
                    ToolMessage(
                        content="Permission denied: this tool is not allowed.",
                        tool_call_id=tool_call["id"]
                    )
                )
                continue

            tool_args = tool_call["args"]

            selected_tool = tools_by_name[tool_name]
            result = selected_tool.invoke(tool_args)

            messages.append(
                ToolMessage(
                    content=str(result),
                    tool_call_id=tool_call["id"]
                )
            )

    return "Agent stopped: maximum execution steps reached."




