import sqlite3

name = 'n5.db'
db = sqlite3.connect(name)

cur = db.cursor()

query = ('''
CREATE TABLE "gruppi" (
id INTEGER PRIMARY KEY,
grou TEXT NOT NULL,
rank INTEGER NOT NULL
);''')

query1 = ('''
CREATE TABLE "news" (
id INTEGER PRIMARY KEY,
news_rank INTEGER,
text TEXT,
title TEXT,
FOREIGN KEY("news_rank") REFERENCES gruppi(rank)
)''')

cur.execute(query)
cur.execute(query1)

add1 = ('''
INSERT INTO 'gruppi' ('grou','rank') VALUES
('ucheniki_11g', 1),
('pedagogi_mat', 2),
('administracia_2korp', 3),
('roditeli_11g', 4);
''')

cur.execute(add1)

add2 = ('''
INSERT INTO 'news' ('news_rank', 'text', 'title') VALUES
(1, 'Vlad poshel kushat', 'pozhiranie'),
(2, 'zachety ne byli sdany nikem, vsem 2))', 'merry christmas'),
(3, 'uchitelyam categorichesky zapreschaetsa stavit zachet!!!!!', 'rasporyazhenie'),
(4, 'Byl vveden zachet po bilogii nesmotrya na to chto vse klassy - him-him', 'Himii konec((((');
''')

cur.execute(add2)

query = ('''
        SELECT *
        FROM 'news'
        INNER JOIN 'gruppi' ON rank = news_rank
        ''')
cur.execute(query)

result = cur.fetchall()
print(result)

db.commit()

# ---------------------------------------------------------------------------------------


import unittest
import sqlite3


class TestTable(unittest.TestCase):
    def setUp(self):
        self.rus = "qwertyuiopasdfghjklzxcvbnm_-@$!?1234567890** "
        self.login = "qwertyuiopasdfghjklzxcvbnm_-@$!?1234567890 "
        self.name = 'n5.db'
        self.db = sqlite3.connect(self.name)
        self.cur = self.db.cursor()

    def test_connection(self):
        query = ('''
        SELECT *
        FROM 'news'
        INNER JOIN 'gruppi' ON rank = news_rank
        ''')
        self.cur.execute(query)
        result = self.cur.fetchall()
        for res in result:
            self.assertEqual(res[1], res[6])

    def test_unique_ids(self):
        query = ('''
        SELECT id
        FROM 'news'
        ''')
        self.cur.execute(query)
        result = self.cur.fetchall()
        self.assertEqual(len(result), len(set(result)))

        query = ('''
                SELECT id
                FROM 'gruppi'
                ''')
        self.cur.execute(query)
        result = self.cur.fetchall()
        self.assertEqual(len(result), len(set(result)))

    def test_name_and_login(self):
        query = ('''
        SELECT grou
        FROM 'gruppi'
        ''')
        self.cur.execute(query)
        result = self.cur.fetchall()
        for name in result:
            name = str(name[0])
            for letter in name:
                self.assertIn(letter.lower(), self.rus)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
