import sqlite3


connection = sqlite3.connect("domains.db")
cursor = connection.cursor()

data = cursor.execute(
    """
    SELECT * FROM domains;
    """
)
for project_id, domain in data.fetchall():
    domain_list = domain.split(".")
    pattern = f"^(?!\S*((.static.developer?).))({domain_list[-3]}.)?" \
              f"{domain_list[-2]}.{domain_list[-1]}$"
    cursor.execute(
        """
        INSERT INTO rules VALUES ($1, $2);
        """,
        [project_id, pattern]
    )
    connection.commit()
cursor.close()
