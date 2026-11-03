# type hints tells us what type of data function expects and returns
def invoice_total(items: list[dict]) -> float:
    total = 0

    for item in items:
        total = total + item["price"]

    return float(total)


items = [
    {"name": "Laptop", "price": 1500},
    {"name": "Mouse", "price": 50},
    {"name": "Keyboard", "price": 100}
]

result = invoice_total(items)

print("Invoice total:", result)
