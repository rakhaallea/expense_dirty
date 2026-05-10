from models.expenseTracker import ExpenseTracker


tracker = ExpenseTracker()

tracker.read_csv("data/expense_dirty.csv")

tracker.show_error_data()

tracker.show_summary()

tracker.show_total_per_kategori()