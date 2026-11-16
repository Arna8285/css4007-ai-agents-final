
# Semester Week 11 Progress Report

## Completed Work

During Week 11, I started implementing my AI Personal Finance Agent.

I completed the following tasks:

- Checked the Python environment and installed libraries.
- Used Python 3.13.2 and Jupyter Notebook.
- Configured the OpenAI API key using a .env file.
- Added .env to .gitignore to protect the API key.
- Connected the gpt-4o-mini model using ChatOpenAI.
- Created my first successful LLM request.
- Added a SystemMessage to define the role of the financial assistant.
- Used HumanMessage to send financial questions.
- Tested the model with three financial scenarios.
- Saved the code in src/week11_llm.ipynb.

## Important Commits

- Commit hash: To be added after committing the Week 11 work.
- Description: Implement initial LLM integration for the finance agent.
- Link: To be added after pushing to GitHub.

## Current Functionality

The application can now communicate with an OpenAI language model.

The current prototype can:

1. Answer simple financial questions.
2. Calculate monthly savings from income and expenses.
3. Estimate savings over several months.
4. Evaluate whether a savings goal is realistic.
5. Suggest basic ways to improve a savings plan.

I successfully tested three examples:

Test 1: Monthly Savings
- Income: 250,000 KZT
- Expenses: 180,000 KZT
- Result: 70,000 KZT per month

Test 2: Six-Month Savings
- Income: 300,000 KZT
- Expenses: 220,000 KZT
- Result: 480,000 KZT in 6 months

Test 3: Savings Goal
- Income: 200,000 KZT
- Expenses: 170,000 KZT
- Goal: 500,000 KZT in 6 months
- Result: The goal is not realistic with the current budget.

All three manual tests produced correct results.

LangGraph workflows and financial tools are not implemented yet.

## Problems Encountered

During development, I had several problems:

1. Jupyter Notebook could not find the API key.
2. The OpenAI API returned an AuthenticationError (401).
3. Jupyter Notebook sometimes showed a File Save Error.
4. I needed to understand how to send messages to the LLM.

## Solutions

I solved these problems step by step:

1. Checked the location and content of the .env file.
2. Replaced the invalid API key and reloaded the environment variables.
3. Restarted the Jupyter Notebook server when the connection failed.
4. Used ChatOpenAI to connect to the model.
5. Used SystemMessage and HumanMessage to structure the requests.
6. Checked the financial calculations manually.

## What I Learned

During Week 11, I learned:

- How to connect Python to an OpenAI language model.
- How to use ChatOpenAI from LangChain.
- How to store an API key in a .env file.
- Why secret keys should not be uploaded to GitHub.
- The difference between SystemMessage and HumanMessage.
- How to send requests using llm.invoke().
- How to check LLM responses with simple calculations.

## Next Week

In Week 12, I plan to:

1. Start implementing the core finance agent.
2. Define the agent state using LangGraph.
3. Create a simple workflow with nodes and edges.
4. Add basic financial calculations in Python.
5. Connect the LLM to the workflow.
6. Test the initial agent.
7. Complete the Week 12 progress report.

