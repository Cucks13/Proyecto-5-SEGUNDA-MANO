import psycopg2


def create_tables(cursor, conn):
    # Script de creación de la tabla datos_cash_converters
    create_table_cash_converters = """
    CREATE TABLE IF NOT EXISTS datos_cash_converters (
        id SERIAL PRIMARY KEY,
        titulo VARCHAR(255),
        descripcion VARCHAR(255),
        precio NUMERIC(10, 2)
    );
    """

    # Script de creación de la tabla datos_mercado_libre
    create_table_mercado_libre = """
    CREATE TABLE IF NOT EXISTS datos_mercado_libre (
        id SERIAL PRIMARY KEY,
        titulo VARCHAR(255),
        link TEXT,
        precio_eur NUMERIC(10, 2)
    );
    """

    # Script de creación de la tabla datos_wallpop_limpios
    create_table_wallpop_limpios = """
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
    """

    # Script de creación de la tabla datos_vinted_filtrados
    create_table_vinted_filtrados = """
    CREATE TABLE IF NOT EXISTS datos_vinted_filtrados (
        Unnamed_0 SERIAL PRIMARY KEY,
        id BIGINT NOT NULL,
        title VARCHAR(255),
        is_visible BOOLEAN,
        currency CHAR(3),
        brand_title VARCHAR(255),
        user JSONB,
        url TEXT,
        promoted BOOLEAN,
        photo JSONB,
        favourite_count INT,
        is_favourite BOOLEAN,
        total_item_price NUMERIC(10, 2),
        status VARCHAR(50)
    );
    """

    # Ejecutar los scripts de creación de tablas
    cursor.execute(create_table_cash_converters)
    cursor.execute(create_table_mercado_libre)
    cursor.execute(create_table_wallpop_limpios)
    cursor.execute(create_table_vinted_filtrados)
    conn.commit()

# Ejemplo de uso:
# with conn.cursor() as cursor:
#     create_tables(cursor, conn)
# conn.close()









def bulk_insert_from_csv(file_path, table_name, conn):
    with open(file_path, 'r', encoding='utf-8') as f:
        cursor = conn.cursor()
        # Definir el comando SQL COPY
        sql = f"COPY {table_name} FROM STDIN WITH CSV HEADER DELIMITER ','"
        # Usar copy_expert para ejecutar el comando COPY
        cursor.copy_expert(sql, f)
        conn.commit()