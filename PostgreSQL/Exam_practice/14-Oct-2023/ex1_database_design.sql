CREATE TABLE towns(
	id SERIAL PRIMARY KEY,
	name VARCHAR(45) NOT NULL
);

CREATE TABLE stadiums(
	id SERIAL PRIMARY KEY,
	name VARCHAR(45) NOT NULL,
	capacity INT CHECK (capacity > 0) NOT NULL,
	town_id INT REFERENCES towns ON DELETE CASCADE ON UPDATE CASCADE NOT NULL
);

CREATE TABLE teams(
	id SERIAL PRIMARY KEY,
	name VARCHAR(45) NOT NULL,
	established DATE NOT NULL,
	fan_base INT CHECK (fan_base >= 0) DEFAULT 0 NOT NULL,
	stadium_id INT REFERENCES stadiums ON DELETE CASCADE ON UPDATE CASCADE NOT NULL
);

CREATE TABLE coaches(
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(10) NOT NULL,
	last_name VARCHAR(20) NOT NULL,
	salary NUMERIC(10, 2) CHECK (salary >= 0) DEFAULT 0 NOT NULL,
	coach_level INT CHECK (coach_level >= 0) DEFAULT 0 NOT NULL
);

CREATE TABLE skills_data(
	id SERIAL PRIMARY KEY,
	dribbling INT CHECK (dribbling >= 0) DEFAULT 0,
	pace INT CHECK (pace >= 0) DEFAULT 0,
	passing INT CHECK (passing >= 0) DEFAULT 0,
	shooting INT CHECK (shooting >= 0) DEFAULT 0,
	speed INT CHECK (speed >= 0) DEFAULT 0,
	strength INT CHECK (strength >= 0) DEFAULT 0
);

CREATE TABLE players(
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(10) NOT NULL,
	last_name VARCHAR(20) NOT NULL,
	age INT CHECK (age >= 0) DEFAULT 0 NOT NULL,
	position CHAR(1) NOT NULL,
	salary NUMERIC(10, 2) CHECK (salary >= 0) DEFAULT 0 NOT NULL,
	hire_date TIMESTAMP,
	skills_data_id INT REFERENCES skills_data ON DELETE CASCADE ON UPDATE CASCADE NOT NULL,
	team_id INT REFERENCES teams ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE players_coaches(
	player_id INT REFERENCES players ON DELETE CASCADE ON UPDATE CASCADE,
	coach_id INT REFERENCES coaches ON DELETE CASCADE ON UPDATE CASCADE
);