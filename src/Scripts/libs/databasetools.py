import pandas as pd

def search_collumn(query, collumn, db):
    res = db[db[collumn] == query]
    return res
def search_query(query, db):
    res = db.query(query)
    return res
def search_range_collumn(query, collumn, db):
    res = db[(db[collumn] > query) & (db[collumn] < query)]
    return res
def write(data, db, filename):
    dt = pd.DataFrame(data)
    comb = pd.concat([db, dt], ignore_index=True)
    comb.to_csv(filename, index=False)
def read(filename):
    res = pd.read_csv(filename)
    return res