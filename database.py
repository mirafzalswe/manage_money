import psycopg2

class Database:
    def __init__(self, database, user, host, password):
        self.connection = psycopg2.connect(database=database, user=user, host=host, password=password)
        self.cur = self.connection.cursor()

    def start_transaction(self):
        self.cur.execute('START TRANSACTION')

    def commit(self):
        self.connection.commit()

    def rollback(self):
        self.cur.execute('ROLLBACK')

    def get_balance(self, card_id):
        self.cur.execute('SELECT balance FROM customers WHERE card_id = %s', (card_id,))
        balance = self.cur.fetchone()
        return balance[0] if balance else None

    def update_balance(self, card_id, amount):
        self.cur.execute('UPDATE customers SET balance = balance + %s WHERE card_id = %s', (amount, card_id))

    def create_customer(self, name, card_id, balance):
        self.cur.execute('INSERT INTO customers (name, card_id, balance) VALUES (%s, %s, %s)', (name, card_id, balance))

    def get_all_customers(self):
        self.cur.execute('SELECT * FROM customers')
        return self.cur.fetchall()

    def update_customer(self, card_id, name, balance):
        self.cur.execute('UPDATE customers SET name = %s, balance = %s WHERE card_id = %s', (name, balance, card_id))

    def close(self):
        self.cur.close()
        self.connection.close()
