import sqlite3
from pydantic import BaseModel
import pandas as pd
from sqlalchemy import create_engine

class User(BaseModel):
    user_id : int
    username : str
    hashed_password : str
    name : str
    dob : str
    email : str
    bio : str
    profession : str

    
def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS app_users (
        user_id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        hashed_password TEXT NOT NULL,
        name TEXT NOT NULL,
        dob TEXT NOT NULL,
        email TEXT NOT NULL,
        bio TEXT,
        profession TEXT
    )
    ''')
    conn.commit()
    conn.close()

# Call the function to initialize the database
init_db()




if __name__ == '__main__':
    print("-------- upload the csv file -------")
    csvPath = input("input the path of csv file: ")
    
    df = pd.read_csv(csvPath)
    
    engine = create_engine('sqlite:///users.db')
    df.to_sql("app_users", con=engine, if_exists="replace", index=False)

    #engine.close()



    


