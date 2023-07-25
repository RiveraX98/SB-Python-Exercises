-- from the terminal run:
-- psql < outer_space.sql

DROP DATABASE IF EXISTS outer_space;

CREATE DATABASE outer_space;

\c outer_space

CREATE TABLE planets
(
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  orbital_period_in_years FLOAT NOT NULL,
  orbits_around TEXT NOT NULL,
  galaxy TEXT NOT NULL,

);

CREATE TABLE moons(
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  galaxy TEXT NOT NULL,

);

CREATE TABLE planets_moons(
 id SERIAL PRIMARY KEY,
 planets_id INT NOT NULL,
 moons_id INT NOT NULL,
);

CREATE TABLE galaxies(
 id SERIAL PRIMARY KEY,
 name TEXT NOT NULL,
 magnitude FLOAT NOT NULL,
 constellation TEXT
);


INSERT INTO planets
  (name, orbital_period_in_years, orbits_around, galaxy_id)
VALUES
  ('Earth', 1.00, 'The Sun'),
  ('Mars', 1.88, 'The Sun'),
  ('Venus', 0.62, 'The Sun')
  ('Neptune', 164.8, 'The Sun'),
  ('Proxima Centauri b', 0.03, 'Proxima Centauri', ),
  ('Gliese 876 b', 0.23, 'Gliese 876');