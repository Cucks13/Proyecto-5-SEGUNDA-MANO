-- Creación de la tabla datos_cash_converters
CREATE TABLE IF NOT EXISTS datos_cash_converters (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(255),
    descripcion VARCHAR(255),
    precio NUMERIC(10, 2)
);

-- Creación de la tabla datos_mercado_libre
CREATE TABLE IF NOT EXISTS datos_mercado_libre (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(255),
    link TEXT,
    precio_eur NUMERIC(10, 2)
);

-- Creación de la tabla datos_wallpop_limpios
CREATE TABLE IF NOT EXISTS datos_wallpop_limpios (
    id SERIAL PRIMARY KEY,
    wallpop_id VARCHAR(20),
    user_id VARCHAR(20),
    titulo VARCHAR(255),
    descripcion TEXT,
    categoria_id INTEGER,
    precio NUMERIC(10, 2),
    imagenes JSON,
    reservado BOOLEAN,
    localizacion VARCHAR(255),
    golpe VARCHAR(20),
    reacondicionado BOOLEAN,
    url_producto TEXT,
    posibilidad_envio BOOLEAN
);

-- Creación de la tabla datos_vinted_filtrados
CREATE TABLE IF NOT EXISTS datos_vinted_filtrados (
    Unnamed_0 SERIAL PRIMARY KEY,
    id BIGINT NOT NULL,
    title VARCHAR(255),
    is_visible BOOLEAN,
    currency CHAR(3),
    brand_title VARCHAR(255),
    url_ TEXT,
    promoted BOOLEAN,
    favourite_count INT,
    is_favourite BOOLEAN,
    total_item_price NUMERIC(10, 2),
    status_ VARCHAR(50)
);
