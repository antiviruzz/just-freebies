def category_total(expenses):
    cat_totals = {}
    for expense in expenses:
        cat = expense["category"]
        amt = expense["amount"]
        if cat in cat_totals:
            cat_totals[cat] += amt
        else:
            cat_totals[cat] = amt
    return cat_totals

def cat_total(expenses):
    catt = {}
    for expense in expenses:
        c = expense["category"]
        a = expense["amount"]
        catt[c] = catt.get(c,0) + a
    return catt

def percentage_score(correct, total):
    if total == 0:
        return 0
    return round((correct/total)*100)

def completion_rate(tasks):
    if not tasks:
        return 0
    completed = 0
    for task in tasks:
        if task["completed"]:
            completed+= 1
    return round((completed/len(tasks))*100)

def find_book(books, title):
    for book in books:
        if book["title"] == title:
            return book
    return None

def lowest_stock(products):
    if not products:
        return None

    lowest = products[0]

    for product in products:
        pq = product["quantity"]
        lq = lowest["quantity"]
        pi = product["id"]
        li = lowest["id"]

        if pq < lq or (pq == lq and pi < li):
            lowest = product

    return lowest["id"]

def count_by_author(books):
    author_counts = {}

    for book in books:
        author = book["author"]
        author_counts[author] = author_counts.get(author, 0) + 1

    return author_counts

def compound(principal, rate, periods):
    balance = principal * (1 + rate) ** periods
    return round(balance, 2)

def apply_discount(products, category, pct):
    new_products = []

    for product in products:
        new_product = product.copy()

        if product["category"] == category:
            new_price = product["price"] - (product["price"] * pct / 100)
            new_product["price"] = round(new_price, 2)

        new_products.append(new_product)

    return new_products