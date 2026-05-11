USE ecom;
-- Create StudentMarks Table
-- CREATE TABLE StudentMarks (
--     student_id INT PRIMARY KEY,
--     student_name VARCHAR(50),
--     subject VARCHAR(50),
--     marks INT
-- );

-- Insert Data
-- INSERT INTO StudentMarks (student_id, student_name, subject, marks) VALUES
-- (101, 'Alice', 'Math', 78),
-- (102, 'Bob', 'Math', 65),
-- (103, 'Charlie', 'Math', 90),
-- (104, 'David', 'Science', 72),
-- (105, 'Emma', 'Science', 85),
-- (106, 'Frank', 'Science', 60),
-- (107, 'Grace', 'English', 55),
-- (108, 'Helen', 'English', 70),
-- (109, 'Ian', 'English', 88);

-- SELECT student_name, subject, marks FROM StudentMarks
-- WHERE marks > (
-- 	SELECT AVG(marks)AS Subject_Avg FROM StudentMarks 
-- );


SELECT student_name, subject, marks FROM StudentMarks
WHERE marks > (
	SELECT AVG(marks)AS Subject_Avg FROM StudentMarks 
    WHERE subject = StudentMarks.subject
);
