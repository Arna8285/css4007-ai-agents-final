
def calculate_monthly_savings(income: float, expenses: float) -> dict:
    """
    Calculates how much money a user can save per month.
    """
    if income < 0 or expenses < 0:
        raise ValueError("Income and expenses cannot be negative.")

    savings = income - expenses

    return {
        "income": income,
        "expenses": expenses,
        "monthly_savings": savings
    }

def project_savings(monthly_savings: float, months: int) -> dict:
    """
    Calculates total savings for a given number of months.
    """
    if months <= 0:
        raise ValueError("Months must be greater than zero.")
    if monthly_savings < 0:
        raise ValueError("Monthly savings cannot be negative.")

    total_savings = monthly_savings * months

    return {
        "monthly_savings": monthly_savings,
        "months": months,
        "total_savings": total_savings
    }

def check_savings_goal(
    monthly_savings: float,
    months: int,
    savings_goal: float
) -> dict:
    """
    Checks if a savings goal is achievable.
    """
    if months <= 0:
        raise ValueError("Months must be greater than zero.")
    if monthly_savings < 0:
        raise ValueError("Monthly savings cannot be negative.")

    if savings_goal < 0:
        raise ValueError("Savings goal cannot be negative.")

    total_savings = monthly_savings * months
    achievable = total_savings >= savings_goal

    return {
        "total_savings": total_savings,
        "savings_goal": savings_goal,
        "achievable": achievable
    }
