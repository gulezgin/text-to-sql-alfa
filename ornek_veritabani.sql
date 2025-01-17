CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    ad VARCHAR(100),
    soyad VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE orders (
    siparis_id INTEGER PRIMARY KEY,
    musteri_id INTEGER,
    tarih DATE,
    tutar DECIMAL(10,2),
    FOREIGN KEY (musteri_id) REFERENCES customers(id)
);

CREATE TABLE products (
    urun_id INTEGER PRIMARY KEY,
    ad VARCHAR(100),
    fiyat DECIMAL(10,2),
    stok_miktari INTEGER
);