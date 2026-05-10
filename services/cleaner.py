from models.expenseRecord import ExpenseRecord


def clean_row(row):

    tanggal = row['tanggal']
    kategori = row['kategori']
    amount_raw = row['amount']

    try:

        if amount_raw == "" or amount_raw is None:
            raise ValueError("Empty")

        amount = float(
            amount_raw
            .replace("Rp", "")
            .replace(",", "")
            .strip()
        )

        return ExpenseRecord(
            tanggal,
            amount,
            kategori,
            "OK"
        )

    except Exception as e:

        return ExpenseRecord(
            tanggal,
            0,
            kategori,
            "ERROR"
        )