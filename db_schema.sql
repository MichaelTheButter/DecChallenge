CREATE TABLE city (
    id INTEGER PRIMARY KEY IDENTITY(1,1),
    city_name VARCHAR UNIQUE,
    longitude DECIMAL(18,5),
    latitude DECIMAL(18,5)
);

CREATE TABLE forecast (
    id INTEGER PRIMARY KEY IDENTITY(1,1),
    city VARCHAR,
    forecast_date DATETIME,
    temperature DECIMAL(18,5),
    created_at TIMESTAMP,
    UNIQUE (city, forecast_date),
    FOREIGN KEY (city) REFERENCES city(city_name)
);

CREATE TABLE stats (
    id INTEGER PRIMARY KEY IDENTITY(1,1),
    city VARCHAR,
    max_temp DECIMAL(18,5),
    avg_temp DECIMAL(18,5),
    min_temp DECIMAL(18,5),
    st_month DECIMAL(18,5),
    st_year INTEGER,
    last_update TIMESTAMP,
    FOREIGN KEY (city) REFERENCES city(city_name)
);