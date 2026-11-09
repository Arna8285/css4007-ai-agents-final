
# Project Proposal — Semester Week 10

## Project Title

AI Personal Finance Agent — Intelligent Budget and Savings Planner

## Problem Description

Many people have difficulty managing their personal money. They do not always know where they spend the most money or how much they can save.

This project will create an AI agent that analyzes personal income and expenses, creates a monthly budget, and helps users reach their savings goals.

The agent will use an LLM and financial calculation tools to make plans and update them when the user's situation changes.

## Target Users

- University students
- Young adults
- People who want to manage their monthly budget
- People saving money for personal goals

## Selected Difficulty

A — Advanced

## Expected Functionality

1. Accept user income, expenses, and savings goals.
2. Read financial data from a local CSV file.
3. Calculate total income, expenses, and remaining money.
4. Analyze spending by category.
5. Create a monthly budget.
6. Calculate a savings plan.
7. Check if a financial goal is realistic.
8. Update the plan when income or expenses change.
9. Save the current plan and agent state.
10. Handle invalid inputs and tool errors.
11. Ask for user approval before saving changes.
12. Show clear financial recommendations.

## Proposed Functions

### 1. load_transactions(file_path)

- **Purpose:** Load income and expense records.
- **Input:** Path to a CSV file.
- **Output:** Validated transaction records.
- **Dependencies:** Python, pandas, CSV file.

### 2. analyze_expenses(transactions)

- **Purpose:** Calculate total spending and spending by category.
- **Input:** Transaction records.
- **Output:** Expense summary and category totals.
- **Dependencies:** Python, pandas.

### 3. calculate_budget(income, expenses)

- **Purpose:** Calculate remaining money and prepare a monthly budget.
- **Input:** Monthly income and expenses.
- **Output:** Budget summary.
- **Dependencies:** Python.

### 4. plan_savings(goal_amount, months, available_money)

- **Purpose:** Calculate the monthly savings needed to reach a goal.
- **Input:** Savings goal, number of months, and available money.
- **Output:** Savings plan and feasibility result.
- **Dependencies:** Python.

### 5. update_financial_plan(current_plan, changes)

- **Purpose:** Update the budget when the user's financial situation changes.
- **Input:** Current plan and new financial information.
- **Output:** Updated financial plan.
- **Dependencies:** Python, saved agent state.

### 6. save_plan(plan, approved)

- **Purpose:** Save the final financial plan after user approval.
- **Input:** Financial plan and approval status.
- **Output:** Saved file path or a clear error message.
- **Dependencies:** Python, JSON, local storage.

## Proposed Agent Tools

The LLM will select and call these tools:

1. **analyze_expenses** — to understand spending habits.
2. **calculate_budget** — to calculate the monthly budget.
3. **plan_savings** — to check savings goals.
4. **update_financial_plan** — to adjust a plan when conditions change.

The agent will use tool results to make decisions. Financial calculations will be performed by Python functions, not guessed by the LLM.

## Model Selection

- **Programming language:** Python
- **Development environment:** Jupyter Notebook
- **Agent framework:** LangGraph
- **LLM provider:** OpenAI API
- **Proposed model:** gpt-4o-mini
- **Data storage:** CSV and JSON files

The OpenAI API will help the agent understand requests, select tools, and explain results.

LangGraph will manage the agent workflow and state.

## Architecture

User Request  
↓  
Input Validation  
↓  
LLM Agent (LangGraph)  
↓  
Task Planning  
↓  
Tool Selection and Execution  
↓  
Financial Analysis and Calculations  
↓  
Result Validation  
↓  
Check Goal and Budget  
↓  
If needed: Update Plan  
↓  
User Approval for Saving  
↓  
Final Financial Report

The agent will have a maximum number of execution steps to prevent infinite loops.

## Example Requests

**Example 1**

"My monthly income is 250,000 KZT. I spend 80,000 KZT on rent, 60,000 KZT on food, and 30,000 KZT on transport. Create a monthly budget."

**Example 2**

"I want to save 500,000 KZT in six months. Check if my current budget can support this goal."

**Example 3**

"My transport expenses increased by 20,000 KZT. Update my savings plan."

**Example 4**

"Analyze my expenses and tell me which category uses the most money."

## Evaluation Plan

The project will include at least 12 tests.

### Functional Tests

1. Analyze valid expense data.
2. Calculate a monthly budget.
3. Calculate a realistic savings goal.
4. Detect an unrealistic savings goal.
5. Update a budget after an expense change.
6. Process a request requiring multiple tools.
7. Handle missing financial information.
8. Handle a tool failure and stop safely.

### Guardrail Tests

9. Reject negative expense values.
10. Reject unauthorized file changes.
11. Reject instructions that try to bypass safety rules.
12. Stop when the maximum execution step limit is reached.

The agent will also be tested with different financial scenarios. Results and tool execution traces will be saved for evaluation.

## Weekly Milestones

### Week 10 — Proposal and Planning

- Choose the project topic and A level.
- Define the problem and target users.
- Plan functions and tools.
- Design the architecture.
- Complete the project proposal.

### Week 11 — Initial LLM Integration

- Set up Python and required libraries.
- Connect the OpenAI API.
- Create the first working LLM request.
- Test a simple financial question.

### Week 12 — Core Functionality

- Create sample financial data.
- Implement transaction loading.
- Implement expense analysis and budget calculations.
- Add input validation and initial tests.

### Week 13 — Tool Integration

- Register financial functions as LLM tools.
- Implement tool selection and execution.
- Test requests requiring different tools.

### Week 14 — Agent Workflow

- Build the multi-step LangGraph workflow.
- Add agent state and planning.
- Implement plan updates and stopping conditions.
- Select a recent research paper about AI agents.

### Week 15 — Reliability and Guardrails

- Add input and tool validation.
- Add execution limits.
- Require approval before saving.
- Test unauthorized actions and failures.
- Save execution traces.

### Week 16 — Evaluation and Improvement

- Run at least 12 tests.
- Fix identified problems.
- Evaluate agent performance.
- Prepare the research paper presentation.
- Complete the evaluation report.

### Week 17 — Final Submission and Defense

- Complete the final report.
- Update the README.
- Check the GitHub repository.
- Submit the final commit hash.
- Demonstrate the working agent.
- Explain the architecture, tools, and guardrails.
