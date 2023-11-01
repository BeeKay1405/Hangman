import sqlite3

# Connect to the database (or create a new one if it doesn't exist)
conn = sqlite3.connect('hangman.db')
cursor = conn.cursor()

"""
# Create the WORDS table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS WORDS (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT,
        word TEXT,
        difficulty TEXT
    )
''')

# Create the LEADERBOARD table
cursor.execute('''
    CREATE TABLE LEADERBOARD (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        word TEXT,
        score INTEGER
    )    
''')
"""


# Insert words in table
def insertWords(conn, filePath, category):
    try:
        with open(filePath, "r") as file:
            words = file.read().splitlines()

        cursor = conn.cursor()

        for index, word in enumerate(words, start=11):
            cursor.execute("INSERT INTO WORDS (category, word) VALUES (?, ?)", (category, word))

        conn.commit()
        print(f"Words from {filePath} inserted successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()


# Call the function to insert words from a text file into the database
"""insertWords(conn, "animals.txt", "animals")
insertWords(conn, "cars.txt", "cars")
insertWords(conn, "colours.txt", "colours")
insertWords(conn, "countries.txt", "countries")
insertWords(conn, "fruits.txt", "fruits")
insertWords(conn, "movies.txt", "movies")
insertWords(conn, "professions.txt", "professions")
insertWords(conn, "sports.txt", "sports")"""


# Update difficulty based on word length
def updateDifficulty(conn):
    try:
        cursor = conn.cursor()

        cursor.execute('''
            UPDATE Words 
            SET difficulty = 
                CASE 
                    WHEN LENGTH(word) <= 5 THEN 'easy' 
                    WHEN LENGTH(word) > 5 AND LENGTH(word) <= 10 THEN 'medium' 
                    ELSE 'hard' 
                END
        ''')

        conn.commit()
        print("Difficulty updated successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()


"""updateDifficulty(conn)"""


# Insert data into Leaderboard
def insertLeaderboard(name, word, score):
    conn = sqlite3.connect('hangman.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO LEADERBOARD (name, word, score) VALUES (?, ?, ?)",
                   (name, word, score))
    conn.commit()


# Commit the changes and close the connection
conn.commit()
conn.close()

print("Table created successfully!")
