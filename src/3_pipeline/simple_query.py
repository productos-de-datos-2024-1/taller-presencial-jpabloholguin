import json
import os.path
import sqlite3
import pkg_resources

CONGIG_FILE = "config.json"

if not pkg_resources.resource_exists(__name__, CONGIG_FILE):
    raise FileNotFoundError(f"File {CONGIG_FILE} not found")

with pkg_resources.resource_stream(__name__, CONGIG_FILE) as f:
    config = json.load(f)
    
def simple_query():
    query = "SELECT * FROM house_prices LIMIT 5"
    database = os.path.join(config["database_dir"], config["database_name"],)
    
    conn = sqlite3.connect(database)
    result = conn.execute(query).fetchall()
    conn.close()
    for t in result:
        print(t)
        
if __name__ == "__main__":
    simple_query()