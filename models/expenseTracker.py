import csv

from services.cleaner import clean_row


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    # READ CSV
    def read_csv(self, file_path):
        
        with open(file_path, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                # CLEANING DATA
                expense = clean_row(row)
                self.expenses.append(expense)

    # PROCESS TOTAL PER KATEGORI
    def total_per_kategori(self):
        result = {}

        for exp in self.expenses:

            if exp.is_valid():

                if exp.kategori not in result:
                    result[exp.kategori] = 0

                result[exp.kategori] += exp.amount

        return result

    # HITUNG TOTAL VALID & ERROR
    def summary_status(self):
        valid = 0
        error = 0

        for exp in self.expenses:

            if exp.is_valid():
                valid += 1

            elif exp.is_invalid():
                error += 1

        return valid, error

    # TAMPILKAN DATA ERROR
    def show_error_data(self):

        print("=" * 70)
        print("DATA ERROR".center(70))
        print("=" * 70)

        for i, exp in enumerate(self.expenses, 1):

            if exp.is_invalid():

                print(f"{i}. Tanggal  : {exp.tanggal}")
                print(f"   Kategori : {exp.kategori}")
                print(f"   Amount   : Rp {exp.amount:,.0f}".replace(",", "."))
                print(f"   Status   : {exp.status}")

                print("-" * 70)

    # TAMPILKAN TOTAL PER KATEGORI
    def show_total_per_kategori(self):

        totals = self.total_per_kategori()

        print("\n" + "=" * 70)
        print("TOTAL PENGELUARAN PER KATEGORI".center(70))
        print("=" * 70)

        for kategori, total in totals.items():
            print(f"{kategori:<20} Rp {total:>15,.0f}".replace(",", "."))

        print("=" * 70)

    # TAMPILKAN SUMMARY
    def show_summary(self):

        valid, error = self.summary_status()

        print("\n" + "=" * 70)
        print("TOTAL DATA OK DAN ERROR".center(70))
        print("=" * 70)

        print(f"Jumlah Data Error {'':>5}: {error}")
        print(f"Jumlah Data Valid {'':>5}: {valid}")
        print(f"Total Data {'':>12}: {valid + error}")

        print("=" * 70)
