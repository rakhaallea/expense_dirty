from models.expenseTracker import ExpenseTracker

tracker = ExpenseTracker()

tracker.load_csv("data/expense_dirty.csv")

tracker.show_error_data()

tracker.show_summary()

tracker.show_total_per_kategori()

print("\nTOTAL SELURUH PENGELUARAN:")
print(f"Rp {tracker.get_total():,.0f}".replace(",", "."))