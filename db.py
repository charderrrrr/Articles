import sqlite3 as sql

## Инициализация БД
def init_db():
    connect = sql.connect('magazinse.db')
    cursor = connect.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS authors (
        author_id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        affiliation VARCHAR(100),
        email VARCHAR(100),
        UNIQUE (full_name)
        );
    """)

    cursor.execute("""
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

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS topics (
        topic_id INTEGER PRIMARY KEY AUTOINCREMENT,
        topic_name VARCHAR(100) NOT NULL UNIQUE,
        parent_topic_id INTEGER,
        description TEXT,
        FOREIGN KEY (parent_topic_id) REFERENCES topics(topic_id)
        );
    """)

    cursor.execute("""
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

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS article_authors (
        article_id INTEGER NOT NULL,
        author_id INTEGER NOT NULL,
        author_order INTEGER NOT NULL,
        PRIMARY KEY (article_id, author_id),
        FOREIGN KEY (article_id) REFERENCES articles(article_id),
        FOREIGN KEY (author_id) REFERENCES authors(author_id)
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS article_topics (
        article_id INTEGER NOT NULL,
        topic_id INTEGER NOT NULL,
        PRIMARY KEY (article_id, topic_id),
        FOREIGN KEY (article_id) REFERENCES articles(article_id),
        FOREIGN KEY (topic_id) REFERENCES topics(topic_id)
        );
    """)

    connect.commit()

    return True

## Добавление записи