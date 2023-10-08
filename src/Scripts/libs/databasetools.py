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
def write_db(data, db, filename):
    dt = pd.DataFrame(data)
    comb = pd.concat([db, dt], ignore_index=True)
    comb.to_csv(filename, index=False)
def read_db(filename):
    res = pd.read_csv(filename)
    return res
def write_new_db(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
def print_all_db(db):
    return db
def init_db(filename):
    res = pd.read_csv(filename)
    return res
def convert_to_dataframe(data):
    df = pd.DataFrame(data)
    return df
def row_string_search(query, row, db):
    res = db[db[row] == query]
    return res
def row_string_search_range(query, row, db):
    res = db[(db[row] > query) & (db[row] < query)]
    return res
def row_number_search(query, row, db):
    res = db[db[row].str.contains(query)]
    return res