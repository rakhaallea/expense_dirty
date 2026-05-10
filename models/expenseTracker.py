from services.reader import read_csv
from services.cleaner import clean_row
from services.processor import process_total_per_kategori


class ExpenseTracker:

    # =========================
    # CONSTRUCTOR
    # =========================
    def __init__(self):

        # list object ExpenseRecord
        self.records = []

        # list error logs
        self.error_logs = []

    # =========================
    # LOAD CSV
    # =========================
    def load_csv(self, file_path):

        rows = read_csv(file_path)

        for row in rows:

            record = clean_row(row)

            self.records.append(record)

            # simpan log error
            if record.is_invalid():

                self.error_logs.append({
                    "row": row,
                    "message": "Invalid amount"
                })

    # =========================
    # GET TOTAL
    # =========================
    def get_total(self):

        total = 0

        for record in self.records:

            if record.is_valid():
                total += record.amount

        return total

    # =========================
    # GET TOTAL PER CATEGORY
    # =========================
    def get_by_category(self):

        return process_total_per_kategori(self.records)

    # =========================
    # SHOW ERROR DATA
    # =========================
    def show_error_data(self):

        print("=" * 70)
        print("DATA ERROR".center(70))
        print("=" * 70)

        for i, record in enumerate(self.records, 1):

            if record.is_invalid():

                print(f"{i}. Tanggal  : {record.tanggal}")
                print(f"   Kategori : {record.kategori}")
                print(f"   Amount   : Rp {record.amount:,.0f}".replace(",", "."))
                print(f"   Status   : {record.status}")

                print("-" * 70)

    # =========================
    # SHOW SUMMARY
    # =========================
    def show_summary(self):

        valid = 0
        error = 0

        for record in self.records:

            if record.is_valid():
                valid += 1

            elif record.is_invalid():
                error += 1

        print("\n" + "=" * 70)
        print("TOTAL DATA OK DAN ERROR".center(70))
        print("=" * 70)

        print(f"Jumlah Data Error {'':>5}: {error}")
        print(f"Jumlah Data Valid {'':>5}: {valid}")
        print(f"Total Data {'':>12}: {valid + error}")

        print("=" * 70)

    # =========================
    # SHOW CATEGORY TOTAL
    # =========================
    def show_total_per_kategori(self):

        totals = self.get_by_category()

        print("\n" + "=" * 70)
        print("TOTAL PENGELUARAN PER KATEGORI".center(70))
        print("=" * 70)

        for kategori, total in totals.items():

            print(
                f"{kategori:<20} Rp {total:>15,.0f}"
                .replace(",", ".")
            )

        print("=" * 70)