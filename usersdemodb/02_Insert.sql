INSERT INTO users VALUES
(1, 'Alice', 'alice@example.com', 'Female', '1995-05-14', DEFAULT);
-- This method requires you to provide values for all columns in order, except
-- columns with default values or AUTO_INCREMENT .
-- Not recommended if your table structure might change (e.g., new columns added later).

-- Insert by Specifying Column Names (Best Practice)
-- This method is safer and more readable. You only insert into specific columns.
-- or for multiple rows:
-- Single Row
INSERT INTO users (name, email, gender, date_of_birth) VALUES
('Bob', 'bob@example.com', 'Male', '1990-11-23');
-- Multiple rows
INSERT INTO users (name, email, gender, date_of_birth) VALUES
('Bob', 'bob@example.com', 'Male', '1990-11-23'),
('Charlie', 'charlie@example.com', 'Other', '1988-02-17');
-- The remaining columns like id (which is AUTO_INCREMENT ) and created_at (which has a default) are automatically handled by MySQL.
-- Insert Without Specifying Column Names (Full Row Insert)