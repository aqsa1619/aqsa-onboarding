clients = [
    {"name": "Alice Corp", "country": "USA", "monthly_fee": 1200.0},
    {"name": "Beta Ltd", "country": "UK", "monthly_fee": 850.0},
    {"name": "Gamma SA", "country": "France", "monthly_fee": 1500.0},
    {"name": "Delta Inc", "country": "Canada", "monthly_fee": 950.0},
    {"name": "Epsilon Co", "country": "Germany", "monthly_fee": 2000.0},
]

high_tier_clients = [c["name"] for c in clients if c["monthly_fee"] > 1000]
print("Clients paying > $1000:", high_tier_clients)