import psycopg2
from os import environ


class DatabaseLoader:
    # main function
    def __init__(self):
        self.server = environ.get("SERVER")
        self.user = environ.get("USER")
        self.password = environ.get("PASSWORD")
        self.dbname = environ.get("DBNAME")

    # takes the csv and inserts it into the db
    def setup_db(self):
        conn = psycopg2.connect(host=self.server,
                                port=5432,
                                dbname=self.dbname,
                                user=self.user,
                                password=self.password)

        cur = conn.cursor()

        # does table exist
        tb_exists = "select exists(" \
                    "select relname from pg_class where relname='"\
                    + "images" + "')"
        cur.execute(tb_exists)
        if cur.fetchone()[0] is False:
            # make table
            cur.execute(
                'create table images('
                'id serial primary key, '
                'name text not null, '
                'title text not null, '
                'data bytea not null);')
            conn.commit()
        # copy csv
        rootdir = 'images'
	
	for subdir, files in environ.walk(rootdir):
		for file in files:
			query =  "INSERT INTO images (name, title, data) VALUES (%s, %s, %s);"
    			name = environ.path.split(rootdir)[1]
			title = file
			in_file = open(file, "rb") # opening for [r]eading as [b]inary
			data = in_file.read() # if you only wanted to read 512 bytes, do .read(512)
			in_file.close()

			row = (name, title, data)
			
			conn.execute(query, row)

if __name__ == '__main__':
    dbl = DatabaseLoader()
    dbl.setup_db()
