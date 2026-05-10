class ExpenseRecord:
    def __init__(self, tanggal, amount, kategori, status="OK"):
        self.tanggal = tanggal
        self.amount = amount
        self.kategori = kategori
        self.status = status

    def is_valid(self):
        return self.status == "OK"

    def is_invalid(self):
        return self.status == "ERROR"