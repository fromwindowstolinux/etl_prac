import psycopg2
import json

def connect():
    conn = psycopg2.connect(
        dbname = "dbstore", 
        user = "store",
        password = "store",
        host = "127.0.0.1",
        port = "5055"
    )
    return conn

def create_table():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute('''
                CREATE TABLE IF NOT EXISTS store_details (
                    id SERIAL PRIMARY KEY,
                    name TEXT NOT NULL,
                    address TEXT NOT NULL
                )
            ''')

            with open ('store/store/spiders/details.json','r') as store_details:
                store_data = json.loads(store_details.read())
                # print(store_data)
                for store in store_data:
                    if len(store['store_address']) > 30:
                        print(store)
                        cur.execute('''
                        INSERT INTO store_details (name, address)
                        VALUES (%s, %s);
                        ''',(store['store_name'],store['store_address']))

        conn.commit()

if __name__=="__main__":
    create_table()