SELECT * FROM students;
SELECT * FROM heroes;
SELECT * FROM villains;

SELECT * FROM heroes LEFT JOIN students ON heroes.id = students.hero_id;