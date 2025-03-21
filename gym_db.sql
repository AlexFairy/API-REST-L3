USE gym_db;

/*
CREATE TABLE Members (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT
);


CREATE TABLE WorkoutSessions (
    session_id INT PRIMARY KEY,
    member_id INT,
    session_date DATE,
    session_time VARCHAR(50),
    activity VARCHAR(255),
    FOREIGN KEY (member_id) REFERENCES Members(id)
);
*/

/*
INSERT INTO Members
VALUES (1, "Jane Doe", 27);
*/

/*
INSERT INTO Members (id, name, age)
VALUES (2, "John Smith", 59),
	   (3, "Michelle Garcia", 36),
       (4, "Johnny Guzman", 21),
       (6, "Michael Hernandez", 18),
       (7, "Miriam Meillant", 38),
       (8, "Alexandria Meilan", 29),
       (9, "Mitch Landford", 44);
*/

/*
INSERT INTO WorkoutSessions (session_id, member_id, session_date, session_time, activity)
VALUES (50, 1, '2024-03-02', '06:35 AM', 'Cardio'),
       (51, 2, '2024-03-02', '07:11 AM', 'Cardio'),
       (53, 3, '2024-03-02', '07:55 AM', 'Yoga'),
       (54, 4, '2024-03-02', '10:00 AM', 'Cardio'),
       (55, 4, '2024-03-02', '11:00 AM', 'Yoga'),
       (56, 5, '2024-03-02', '07:05 AM', 'Cardio'),
       (57, 6, '2024-03-02', '01:00 PM', 'Weightlifting'),
       (58, 7, '2024-03-02', '06:00 AM', 'Weightlifting'),
       (59, 7, '2024-03-02', '07:00 AM', 'Cardio'),
       (60, 7, '2024-03-02', '08:00 AM', 'Treadmill'),
       (61, 8, '2024-03-02', '10:00 AM', 'Weightlifting'),
       (62, 9, '2024-03-02', '07:15 PM', 'Treadmill');
*/

/*
SELECT *
FROM Members
INNER JOIN WorkoutSessions
ON Members.id = WorkoutSessions.member_id;
*/

/*
SET SQL_SAFE_UPDATES = 0;
UPDATE WorkoutSessions
SET session_time = 'evening'
WHERE member_id = 1;
SET SQL_SAFE_UPDATES = 1;


SELECT * FROM WorkoutSessions;
*/

/*
DELETE FROM WorkoutSessions
WHERE member_id = 2;

DELETE FROM Members
WHERE id = 2;
*/
 /*
SELECT *
FROM Members
INNER JOIN WorkoutSessions
ON Members.id = WorkoutSessions.member_id;
*/

/*
GRANT ALL PRIVILEGES ON gym_db.* TO 'root'@'localhost';
FLUSH PRIVILEGES;
*/

SELECT *
FROM Members
INNER JOIN WorkoutSessions
ON Members.id = WorkoutSessions.member_id;