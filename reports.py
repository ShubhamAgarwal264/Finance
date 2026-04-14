def total_expense(expenses):
    return sum(exp.amount for exp in expenses)

def category_summary(expenses):
    summary = {}
    for exp in expenses:
        summary[exp.category] = summary.get(exp.category, 0) + exp.amount
    return summary

def monthly_report(expenses, month):
    return [exp for exp in expenses if exp.date.startswith(month)]
