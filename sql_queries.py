# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays(
songplay_id SERIAL PRIMARY KEY, 
start_time time NOT NULL, 
user_id int NOT NULL, 
level char(4), 
song_id varchar, 
artist_id varchar, 
session_id int, 
location varchar, 
user_agent varchar
);

""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users(
user_id int PRIMARY KEY, 
first_name varchar NOT NULL, 
last_name varchar NOT NULL, 
gender char(1), 
level char(4)
);
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs(
song_id varchar PRIMARY KEY, 
title varchar NOT NULL, 
artist_id varchar, 
year int, 
duration numeric
);
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists(
artist_id varchar PRIMARY KEY, 
name varchar NOT NULL, 
location varchar, 
lattitude varchar, 
longitude varchar
);
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time(
start_time time PRIMARY KEY, 
hour int NOT NULL, 
day int NOT NULL, 
week int NOT NULL, 
month int NOT NULL, 
year int NOT NULL, 
weekday int NOT NULL);
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays (start_time,user_id,level,song_id,artist_id,session_id,location,user_agent) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""")

user_table_insert = ("""INSERT INTO users VALUES (%s,%s,%s,%s,%s) ON CONFLICT (user_id) DO UPDATE SET level = EXCLUDED.level;""")

song_table_insert = ("""INSERT INTO songs VALUES (%s,%s,%s,%s,%s) ON CONFLICT (song_id) DO NOTHING""")

artist_table_insert = ("""INSERT INTO artists VALUES (%s,%s,%s,%s,%s) ON CONFLICT (artist_id) DO NOTHING""")

time_table_insert = ("""INSERT INTO time VALUES (%s,%s,%s,%s,%s,%s,%s) ON CONFLICT (start_time) DO NOTHING""")

# FIND SONGS

song_select = ("""SELECT s.song_id, a.artist_id FROM songs s JOIN artists a on s.artist_id = a.artist_id WHERE title = (%s) and name = (%s) and duration = (%s)""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]