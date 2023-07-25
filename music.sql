-- from the terminal run:
-- psql < music.sql

DROP DATABASE IF EXISTS music;

CREATE DATABASE music;

\c music

CREATE TABLE songs
(
  id SERIAL PRIMARY KEY,
  title TEXT NOT NULL,
  duration_in_seconds INTEGER NOT NULL,
  release_date DATE NOT NULL,
  artists TEXT[] NOT NULL,
  album TEXT NOT NULL,
  producers TEXT[] NOT NULL
);

CREATE TABLE artists
(
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL
  birth_date DATE NOT NULL,
  last_album TEXT NOT NULL,
);

CREATE TABLE producers
(
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL
  birth_date DATE NOT NULL,
  record_label TEXT NOT NULL,
);


CREATE TABLE songs_artists
(
  id SERIAL PRIMARY KEY,
  song_id
  artist_id
);

CREATE TABLE songs_producers
(
  id SERIAL PRIMARY KEY,
  song_id
  producers_id
);


INSERT INTO songs
  (title, duration_in_seconds, release_date, album,)
VALUES
  ('MMMBop', 238, '04-15-1997', 'Middle of Nowhere'),
  ('Bohemian Rhapsody', 355, '10-31-1975', 'A Night at the Opera'),
  ('One Sweet Day', 282, '11-14-1995', 'Daydream'),
  ('Shallow', 216, '09-27-2018', 'A Star Is Born'),
  ('How You Remind Me', 223, '08-21-2001', 'Silver Side Up'),
  ('New York State of Mind', 276, '10-20-2009',  'The Blueprint 3')
  ('Dark Horse', 215, '12-17-2013', 'Prism', ),
  ('Moves Like Jagger', 201, '06-21-2011', 'Hands All Over'),
  ('Complicated', 244, '05-14-2002', 'Let Go'),
  ('Say My Name', 240, '11-07-1999',  'The Writing''s on the Wall');
