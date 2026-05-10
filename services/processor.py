def process_total_per_kategori(expenses):
    total_per_kategori = {}

    for exp in expenses:
        if exp.is_valid():

            if exp.kategori not in total_per_kategori:
                total_per_kategori[exp.kategori] = 0

            total_per_kategori[exp.kategori] += exp.amount

    return total_per_kategori