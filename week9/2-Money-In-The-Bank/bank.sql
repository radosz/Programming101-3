PRAGMA foreign_keys=OFF;
CREATE TABLE clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT unique,
password TEXT,
balance REAL DEFAULT 0,
message TEXT);