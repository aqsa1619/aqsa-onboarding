
def calculate_total(clients):
    total = 0

    for client in clients:
        total += client["monthly_fee"]

    return total


def get_high_fee_clients(clients):
    names = []

    for client in clients:
        if client["monthly_fee"] > 1000:
            names.append(client["name"])

    return names
