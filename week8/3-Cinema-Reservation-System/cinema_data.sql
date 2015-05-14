CREATE TABLE IF NOT EXISTS Movies
(movie_id INTEGER PRIMARY KEY,
    name TEXT,
    rating FLOAT
);

CREATE TABLE IF NOT EXISTS Reservations
(reservation_id INTEGER PRIMARY KEY,
    username TEXT,
    projection_id INTEGER,
    row INTEGER,
    col INTEGER,
    FOREIGN KEY(projection_id) REFERENCES Projections(projection_id)
);

CREATE TABLE IF NOT EXISTS Projections
(projection_id INTEGER PRIMARY KEY,
    movie_id INTEGER,
    type TEXT,
    date DATE,
    time TIME,
    FOREIGN KEY(movie_id) REFERENCES Movies(movie_id)
);