DROP TABLE IF EXISTS transactions;

CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    description TEXT,
    type TEXT CHECK(type IN ('income', 'expense')) NOT NULL
);