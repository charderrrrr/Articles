import sqlite3 as sql

class DatabaseHandler:
    def __init__(self, db_name='magazinse.db'):
        self.connect = sql.connect(db_name)
        self.cursor = self.connect.cursor()
        self.init_db()

    def close(self):
        self.connect.close()

    ## Инициализация БД
    def init_db(self):        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS authors (
            author_id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL UNIQUE,
            affiliation VARCHAR(100),
            email VARCHAR(100)
            );
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS journals (
            journal_id INTEGER PRIMARY KEY AUTOINCREMENT,
            journal_name TEXT NOT NULL UNIQUE,
            issn VARCHAR(9) UNIQUE,
            publisher TEXT,
            founding_year INTEGER,
            frequency VARCHAR(30)
            );
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS topics (
            topic_id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic_name VARCHAR(100) NOT NULL UNIQUE,
            parent_topic VARCHAR(100),
            description TEXT
            );
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS articles (
            article_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR(200) NOT NULL,
            author_id TEXT,
            journal_id TEXT,
            publication_date DATE,
            volume VARCHAR(20),
            issue VARCHAR(20),
            pages INTEGER,
            abstract TEXT,
            link TEXT
            );
        """)

        self.connect.commit()
        return True
    
    def addRecord(self, name_table, data):
        if len(data) != 0:
            if name_table == "Авторы":
                self.cursor.execute("""
                INSERT INTO authors(full_name, affiliation, email)
                VALUES (?, ?, ?);
            """, tuple(data))

            if name_table == "Журналы":
                self.cursor.execute("""
                INSERT INTO journals(journal_name, issn, publisher, founding_year, frequency)
                VALUES (?, ?, ?, ?, ?);
            """, tuple(data))

            if name_table == "Темы":
                self.cursor.execute("""
                INSERT INTO topics(topic_name, parent_topic, description)
                VALUES (?, ?, ?);
            """, tuple(data))

            if name_table == "Статьи":
                self.cursor.execute("""
                INSERT INTO articles(title, author_id, journal_id, publication_date, volume, issue, pages, abstract, link)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
            """, tuple(data))

            return self.connect.commit()
        
    def load_data(self, name_table):
        if name_table == "Авторы":
            self.cursor.execute("""
            SELECT * FROM Авторы
            """)
            return self.cursor.fetchall()

        if name_table == "Журналы":
            self.cursor.execute("""
            SELECT * FROM journals
        """)
            return self.cursor.fetchall()

        if name_table == "Темы":
            self.cursor.execute("""
            SELECT * FROM topics
        """)
            return self.cursor.fetchall()

        if name_table == "Статьи":
            self.cursor.execute("""
            SELECT * FROM articles
        """)
            return self.cursor.fetchall()
        
    def load_headers(self, name_table):   
        if name_table == "Авторы":
            self.cursor.execute("PRAGMA table_info(authors)")
            columns_dict = {idx: column[1] for idx, column in enumerate(self.cursor.fetchall())}
            return columns_dict

        if name_table == "Журналы":
            self.cursor.execute("PRAGMA table_info(journals)")
            columns_dict = {idx: column[1] for idx, column in enumerate(self.cursor.fetchall())}
            return columns_dict

        if name_table == "Темы":
            self.cursor.execute("PRAGMA table_info(topics)")
            columns_dict = {idx: column[1] for idx, column in enumerate(self.cursor.fetchall())}
            return columns_dict

        if name_table == "Статьи":
            self.cursor.execute("PRAGMA table_info(articles)")
            columns_dict = {idx: column[1] for idx, column in enumerate(self.cursor.fetchall())}
            return columns_dict
        
    def delRecord(self, name_table, id):
        if len(id) != 0:
            if name_table == "Авторы":
                self.cursor.execute("""
                DELETE FROM authors WHERE author_id=?
            """, tuple(id))

            if name_table == "Журналы":
                self.cursor.execute("""
                DELETE FROM journals WHERE journal_id=?
            """, tuple(id))

            if name_table == "Темы":
                self.cursor.execute("""
                DELETE FROM topics WHERE topic_id=?
            """, tuple(id))

            if name_table == "Статьи":
                self.cursor.execute("""
                DELETE FROM articles WHERE article_id=?
            """, tuple(id))

            return self.connect.commit()
        
    def findValue(self, name_table, text):

        if name_table == "Авторы":
            self.cursor.execute("""
            SELECT * FROM authors WHERE 
                full_name LIKE ? OR
                affiliation LIKE ? OR
                email LIKE ?
            """, (text, text, text))
            return self.cursor.fetchall()
    
        if name_table == "Журналы":
            self.cursor.execute("""
            SELECT * FROM journals WHERE 
                journal_name LIKE ? OR
                issn LIKE ? OR
                publisher LIKE ? OR
                founding_year LIKE ? OR
                frequency LIKE ?
            """, (text, text, text, text, text))
            return self.cursor.fetchall()

        if name_table == "Темы":
            self.cursor.execute("""
            SELECT * FROM topics WHERE 
                topic_name LIKE ? OR
                parent_topic LIKE ? OR
                description LIKE ?
            """, (text, text, text))
            return self.cursor.fetchall()

        if name_table == "Статьи":
            self.cursor.execute("""
            SELECT * FROM articles WHERE 
                title LIKE ? OR
                author_id LIKE ? OR
                journal_id LIKE ? OR
                publication_date LIKE ? OR
                volume LIKE ? OR
                issue LIKE ? OR
                pages LIKE ? OR
                abstract LIKE ? OR
                link LIKE ?
            """, (text, text, text, text, text, text, text, text, text))
            return self.cursor.fetchall()
    

        

    def getAuthors(self):
        self.cursor.execute(""" 
        SELECT full_name FROM authors
        """)
        return self.cursor.fetchall()
    
    def getJournals(self):
        self.cursor.execute(""" 
        SELECT journal_name FROM journals
        """)
        return self.cursor.fetchall()
    
    def getTopic(self):
        self.cursor.execute(""" 
        SELECT topic_name FROM topics
        """)
        return self.cursor.fetchall()