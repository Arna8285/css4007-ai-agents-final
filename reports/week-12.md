# Semester Week 12 Progress Report

## Completed Work

During Week 12, I created my first LangGraph workflow for the AI Personal Finance Agent.

I completed the following tasks:

- Created a new Jupyter Notebook (`src/week12_graph.ipynb`).
- Defined `FinanceState` using `TypedDict`.
- Created a node to calculate monthly savings.
- Created nodes to generate financial responses.
- Connected nodes using normal edges.
- Added conditional edges to select different paths based on the user's financial situation.
- Compiled and executed the LangGraph workflows.
- Tested three financial scenarios.
- Visualized the graph using Mermaid.


## Important Commits

- Commit hash: 34e58bc
- Description: Implement Week 12 LangGraph workflow.
- Link: https://github.com/Arna8285/css4007-ai-agents-final/commit/34e58bc

## Current Functionality

The AI Personal Finance Agent can now process basic financial information using LangGraph.

The user provides monthly income and expenses. The graph calculates the remaining money and selects the correct response.

The workflow supports three situations:

1. **Positive budget:** Income is higher than expenses. The agent shows possible monthly savings.
2. **Balanced budget:** Income equals expenses. The agent reports that no money remains.
3. **Negative budget:** Expenses are higher than income. The agent reports the budget deficit.

I tested the workflow with three examples:

| Monthly Income | Monthly Expenses | Result |
|---|---|---|
| 300,000 KZT | 200,000 KZT | 100,000 KZT savings |
| 250,000 KZT | 250,000 KZT | Balanced budget |
| 180,000 KZT | 220,000 KZT | 40,000 KZT deficit |

All three manual checks produced the expected results.

The workflow currently uses Python functions inside LangGraph. The LLM is not yet connected to this graph.

## Problems Encountered

I needed to understand how LangGraph manages state, nodes, and edges.

I also needed to understand the difference between normal edges and conditional edges.

At first, I created a simple workflow where nodes executed in a fixed order. I then needed to add different paths for different financial situations.

No major execution errors occurred during the implementation.

## Solutions

I started with a simple graph containing two nodes.

Next, I created a `check_budget` function to determine the user's financial situation.

I used `add_conditional_edges()` to connect the calculation node to three possible response nodes.

I tested the graph with positive, balanced, and negative budgets to check the routing logic.

Finally, I generated a graph diagram to understand the workflow visually.

## What I Learned

During Week 12, I learned:

- How to create a LangGraph `StateGraph`.
- How to define and update graph state.
- How to create nodes using Python functions.
- How to connect nodes with `add_edge()`.
- How to create conditional routing using `add_conditional_edges()`.
- How to compile and execute a graph with `invoke()`.
- How to visualize a LangGraph workflow.

I also learned that LangGraph can control the order of financial calculations and select different actions based on the current state.

## Next Week

In Week 13, I plan to:

- Connect the LLM to the LangGraph workflow.
- Create financial tools for budget analysis and savings calculations.
- Allow the LLM to select tools based on the user's request.
- Test the interaction between the LLM and financial tools.
- Continue developing the AI Personal Finance Agent toward the Level A project requirements.
