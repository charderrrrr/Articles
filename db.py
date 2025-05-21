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
            full_name TEXT NOT NULL,
            affiliation VARCHAR(100),
            email VARCHAR(100),
            UNIQUE (full_name)
            );
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS journals (
            journal_id INTEGER PRIMARY KEY AUTOINCREMENT,
            journal_name TEXT NOT NULL,
            issn VARCHAR(9),
            publisher TEXT,
            founding_year INTEGER,
            frequency VARCHAR(30),
            UNIQUE (journal_name, issn)
            );
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS topics (
            topic_id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic_name VARCHAR(100) NOT NULL UNIQUE,
            parent_topic_id INTEGER,
            description TEXT,
            FOREIGN KEY (parent_topic_id) REFERENCES topics(topic_id)
            );
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS articles (
            article_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR(200) NOT NULL,
            journal_id INTEGER NOT NULL,
            publication_date DATE,
            volume VARCHAR(20),
            issue VARCHAR(20),
            pages VARCHAR(20),
            abstract TEXT,
            FOREIGN KEY (journal_id) REFERENCES journals(journal_id)
            );
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS article_authors (
            article_id INTEGER NOT NULL,
            author_id INTEGER NOT NULL,
            author_order INTEGER NOT NULL,
            PRIMARY KEY (article_id, author_id),
            FOREIGN KEY (article_id) REFERENCES articles(article_id),
            FOREIGN KEY (author_id) REFERENCES authors(author_id)
            );
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS article_topics (
            article_id INTEGER NOT NULL,
            topic_id INTEGER NOT NULL,
            PRIMARY KEY (article_id, topic_id),
            FOREIGN KEY (article_id) REFERENCES articles(article_id),
            FOREIGN KEY (topic_id) REFERENCES topics(topic_id)
            );
        """)

        self.connect.commit()
        return True
    
    def addRecord(self, name_table, data):
        if len(data) != 0:
            if name_table == "authors":
                self.cursor.execute("""
                INSERT INTO authors(full_name, affiliation, email)
                VALUES (?, ?, ?);
            """, tuple(data))

            if name_table == "journals":
                self.cursor.execute("""
                INSERT INTO journals(journal_name, issn, publisher, founding_year, frequency)
                VALUES (?, ?, ?, ?, ?);
            """, tuple(data))

            if name_table == "topics":
                self.cursor.execute("""
                INSERT INTO topics(topic_name, parent_topic_id, description)
                VALUES (?, ?, ?);
            """, tuple(data))

            if name_table == "articles":
                self.cursor.execute("""
                INSERT INTO articles(title, journal_id, publication_date, volume, issue, pages, abstract, link)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?);
            """, tuple(data))

            return self.connect.commit()
        
    def load_data(self, name_table):
        if name_table == "authors":
            self.cursor.execute("""
            SELECT full_name, affiliation, email FROM authors
            """)
            return self.cursor.fetchall()

        if name_table == "journals":
            self.cursor.execute("""
            SELECT journal_name, issn, publisher, founding_year, frequency FROM journals
        """)
            return self.cursor.fetchall()

        if name_table == "topics":
            self.cursor.execute("""
            SELECT topic_name, parent_topic_id, description FROM topics
        """)
            return self.cursor.fetchall()

        if name_table == "articles":
            self.cursor.execute("""
            SELECT title, journal_id, publication_date, volume, issue, pages, abstract FROM articles
        """)
            return self.cursor.fetchall()
        
    def load_headers(self, name_table):   
        if name_table == "authors":
            self.cursor.execute("PRAGMA table_info(authors)")
            columns_dict = {idx: column[1] for idx, column in enumerate(self.cursor.fetchall())}
            return columns_dict

        if name_table == "journals":
            self.cursor.execute("PRAGMA table_info(journals)")
            columns_dict = {idx: column[1] for idx, column in enumerate(self.cursor.fetchall())}
            return columns_dict

        if name_table == "topics":
            self.cursor.execute("PRAGMA table_info(journals)")
            columns_dict = {idx: column[1] for idx, column in enumerate(self.cursor.fetchall())}
            return columns_dict

        if name_table == "articles":
            self.cursor.execute("PRAGMA table_info(journals)")
            columns_dict = {idx: column[1] for idx, column in enumerate(self.cursor.fetchall())}
            return columns_dict
        
    def delRecord(self, name_table, data):
        if len(data) != 0:
            if name_table == "authors":
                self.cursor.execute("""
                INSERT INTO authors(full_name, affiliation, email)
                VALUES (?, ?, ?);
            """, tuple(data))

            if name_table == "journals":
                self.cursor.execute("""
                INSERT INTO journals(journal_name, issn, publisher, founding_year, frequency)
                VALUES (?, ?, ?, ?, ?);
            """, tuple(data))

            if name_table == "topics":
                self.cursor.execute("""
                INSERT INTO topics(topic_name, parent_topic_id, description)
                VALUES (?, ?, ?);
            """, tuple(data))

            if name_table == "articles":
                self.cursor.execute("""
                INSERT INTO articles(title, journal_id, publication_date, volume, issue, pages, abstract, link)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?);
            """, tuple(data))

            return self.connect.commit()