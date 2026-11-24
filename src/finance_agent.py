from langchain_core.messages import SystemMessage, HumanMessage, ToolMessage
import os
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
def run_finance_agent(user_request: str, max_steps: int = 5) -> str:
    messages = [
        SystemMessage(
            content=(
                "You are a personal finance assistant. "
                "Use the available tools for financial calculations. "
                "Explain the results in simple language. "
                "Do not invent financial numbers."
            )
        ),
        HumanMessage(content=user_request)
    ]

    tools_by_name = {tool.name: tool for tool in tools}

    for step in range(max_steps):
        response = llm_with_tools.invoke(messages)
        messages.append(response)

        if not response.tool_calls:
            return response.content

        for tool_call in response.tool_calls:
            tool_name = tool_call["name"]
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


from langchain_core.messages import HumanMessage, ToolMessage


def run_finance_agent(user_request: str):
    messages = [HumanMessage(content=user_request)]

    # Получаем ответ от LLM
    response = llm_with_tools.invoke(messages)
    messages.append(response)

    # Выполняем выбранные инструменты

    steps = 0
    max_steps = 5

    while response.tool_calls and steps < max_steps:
        steps += 1

        for tool_call in response.tool_calls:
            selected_tool = next(
                tool for tool in tools
                if tool.name == tool_call["name"]
            )

            result = selected_tool.invoke(tool_call["args"])

            messages.append(
                ToolMessage(
                    content=str(result),
                    tool_call_id=tool_call["id"]
                )
            )

        response = llm_with_tools.invoke(messages)
        messages.append(response)

    if steps >= max_steps and response.tool_calls:
        return "Execution stopped: maximum number of steps reached."

    return response.content


