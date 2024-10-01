SHOW DATABASES;

USE omfk;

SHOW TABLES;

DESCRIBE students;



CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    grade INT,
    enrollment_date DATE
);


INSERT INTO students (first_name, last_name, age, grade, enrollment_date) VALUES
('Олександр', 'Коваленко', 18, 4, '2024-08-16'),
('Марія', 'Шевченко', 18, 4, '2024-08-22'),
('Андрій', 'Мельник', 17, 3, '2024-08-30'),
('Олена', 'Кравченко', 17, 3, '2024-09-01');


SELECT * FROM students WHERE age = 18;

SELECT first_name, last_name, age FROM students WHERE grade = 4 ORDER BY enrollment_date DESC;
