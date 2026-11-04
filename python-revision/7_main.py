
from utils import calculate_total, get_high_fee_clients


clients = [
    {"name": "Ali", "country": "Pakistan", "monthly_fee": 1200},
    {"name": "Sara", "country": "USA", "monthly_fee": 1500},
    {"name": "John", "country": "UK", "monthly_fee": 800},
    {"name": "Ayesha", "country": "Pakistan", "monthly_fee": 2000},
    {"name": "David", "country": "Canada", "monthly_fee": 900}
]

total = calculate_total(clients)

high_fee_clients = get_high_fee_clients(clients)

print("Total monthly fee:", total)

print("Clients with fee above 1000:", high_fee_clients)
