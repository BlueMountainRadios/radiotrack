CREATE TABLE IF NOT EXISTS radiostatus(
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    status TEXT NOT NULL,
    meaning TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS manufacturer(
    id BIGINT GENERATED ALWAYS AS INDENTITY PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS radioaccessorytype(
    id BIGINT GENERATED ALWAYS AS INDENTITY PRIMARY KEY,
    accessory_type TEXT NOT NULL,
    manufacturer_id BIGINT REFERENCES manufacturer(id) -- Foreign Key to Manufacturer
);


CREATE TABLE IF NOT EXISTS radio(
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    manufacturer_id BIGINT REFERENCES manufacturer(id), -- Foreign Key to Manufacturer,
    model TEXT NOT NULL,
    model_number TEXT NOT NULL,
    serial_number TEXT NOT NULL,
    status_id BIGINT REFERENCES radio_status(id),
    purchase_price DECIMAL(10, 2) CHECK (purchase_price > 0),
    date_acquired DATE  DEFAULT CURRENT_DATE,
    selling_price DECIMAL(10, 2) CHECK (selling_price > 0),
    accessories TEXT,
    version BIGINT NOT NULL
);
