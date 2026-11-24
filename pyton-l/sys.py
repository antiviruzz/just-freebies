def category_total(expenses):
    cat_tot = {}
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        if category in cat_tot:
            cat_tot[category] += amount
        else:
            cat_tot[category] = amount
    return cat_tot

def pecentage_score(correct, total):
    if total == 0:
        return 0
    return round(correct/total) * 100

def completion_rate(tasks):
    if not tasks:
        return 0
    complete = 0
    for task in tasks:
        if task["completed"]:
            complete += 1
    return round(complete / len(tasks) * 100)

def find_book(books, title):
    for book in books:
        if book["title"] == title:
            return book
    return None