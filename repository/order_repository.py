from db_config import get_db_connection


# ✅ 1. Order History (JOIN)
def get_order_history():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT o.id AS order_id, 
           c.name AS customer_name, 
           p.name AS product_name,
           o.quantity, 
           p.price,
           (o.quantity * p.price) AS total_amount
    FROM orders o
    JOIN customers c ON o.customer_id = c.id
    JOIN products p ON o.product_id = p.id
    ORDER BY total_amount DESC;
    """

    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result


# ✅ 2. Highest Value Order
def get_highest_value_order():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT o.id AS order_id, 
           c.name AS customer_name,
           SUM(o.quantity * p.price) AS total_amount
    FROM orders o
    JOIN customers c ON o.customer_id = c.id
    JOIN products p ON o.product_id = p.id
    GROUP BY o.id
    ORDER BY total_amount DESC
    LIMIT 1;
    """

    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    return result


# ✅ 3. Most Active Customer
def get_most_active_customer():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT c.name AS customer_name,
           COUNT(o.id) AS order_count
    FROM orders o
    JOIN customers c ON o.customer_id = c.id
    GROUP BY c.id
    ORDER BY order_count DESC
    LIMIT 1;
    """

    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    return result
