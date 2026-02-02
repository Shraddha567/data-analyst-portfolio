USE startersql;
-- SELECT gender, name from users WHERE gender='Male';
-- SELECT * FROM users WHERE date_of_birth > '1992-09-02';
-- SELECT * FROM users WHERE email IS NOT NULL;
-- SELECT * FROM users LIMIT 5;
-- SELECT * FROM users LIMIT 10 OFFSET 5;
-- SELECT * FROM users LIMIT 5,10;
SELECT * FROM users ORDER BY created_at DESC LIMIT 10;