CREATE TABLE IF NOT EXISTS radio(
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    manufacturer TEXT,
    model TEXT NOT NULL,
    serial_number TEXT NOT NULL,
    status TEXT,
    purchase_price DECIMAL(10, 2) CHECK (purchase_price > 0),
    date_acquired DATE  DEFAULT CURRENT_DATE,
    selling_price DECIMAL(10, 2) CHECK (selling_price > 0),
    accessories TEXT,
    version BIGINT NOT NULL
)
