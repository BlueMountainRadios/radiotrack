CREATE TABLE IF NOT EXISTS radio_status(
    id BIGINT NOT NULL GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    status TEXT NOT NULL,
    meaning TEXT NOT NULL
    UNIQUE(status)
);

CREATE TABLE IF NOT EXISTS manufacturer(
    id BIGINT NOT NULL GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT NOT NULL
    UNIQUE(name)
);

CREATE TABLE IF NOT EXISTS radio_accessory_type(
    id BIGINT NOT NULL GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    type TEXT NOT NULL,
    description TEXT NOT NULL,
    UNIQUE(type)
);

CREATE TABLE IF NOT EXISTS radio_accessory(
    id BIGINT NOT NULL GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT NOT NULL,
    model TEXT NOT NULL,
    accessory_type_id BIGINT REFERENCES radioaccessorytype(id), -- Foreign Key to Radio Accessory accessory_type
    manufacturer_id BIGINT REFERENCES manufacturer(id), -- Foreign Key to Manufacturer
    purchase_price DECIMAL(10, 2) NOT NULL CHECK (purchase_price >= 0),
    selling_price DECIMAL(10, 2) NOT NULL CHECK (selling_price >= 0)
);


CREATE TABLE IF NOT EXISTS radio(
    id BIGINT NOT NULL GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    manufacturer_id BIGINT NOT NULL REFERENCES manufacturer(id), -- Foreign Key to Manufacturer,
    model TEXT NOT NULL,
    model_number TEXT NOT NULL,
    serial_number TEXT NOT NULL,
    status_id BIGINT NOT NULL REFERENCES radio_status(id),
    purchase_price DECIMAL(10, 2) NOT NULL CHECK (purchase_price >= 0),
    date_acquired DATE  DEFAULT CURRENT_DATE,
    selling_price DECIMAL(10, 2) NOT NULL CHECK (selling_price >= 0),
    accessories TEXT,
    version BIGINT NOT NULL DEFAULT 0,
    UNIQUE(manufacturer_id, model_number, serial_number)
);
