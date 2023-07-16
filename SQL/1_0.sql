--Project: creat a table is filter dados in order aphabet

--creat table
CREATE TABLE People (
  Name VARCHAR(20) NOT NULL,
  Age INT NOT NULL
  );

-- add elements in table
INSERT INTO People(Name, Age) VALUES ('xxxxx', 23);
INSERT INTO People(Name, Age) VALUES ('Alice', 27);
INSERT INTO People(Name, Age) VALUES ('Bob', 35);
INSERT INTO People(Name, Age) VALUES ('Charlie', 42);
INSERT INTO People(Name, Age) VALUES ('David', 19);
INSERT INTO People(Name, Age) VALUES ('Emily', 56);
INSERT INTO People(Name, Age) VALUES ('Frank', 31);
INSERT INTO People(Name, Age) VALUES ('Grace', 23);
INSERT INTO People(Name, Age) VALUES ('Henry', 47);
INSERT INTO People(Name, Age) VALUES ('Isabella', 18);
INSERT INTO People(Name, Age) VALUES ('Jake', 29);
INSERT INTO People(Name, Age) VALUES ('Karen', 37);
INSERT INTO People(Name, Age) VALUES ('Liam', 21);
INSERT INTO People(Name, Age) VALUES ('Mia', 24);
INSERT INTO People(Name, Age) VALUES ('Nathan', 30);
INSERT INTO People(Name, Age) VALUES ('Olivia', 26);
INSERT INTO People(Name, Age) VALUES ('Peter', 39);
INSERT INTO People(Name, Age) VALUES ('Quinn', 28);
INSERT INTO People(Name, Age) VALUES ('Riley', 33);
INSERT INTO People(Name, Age) VALUES ('Sarah', 41);
INSERT INTO People(Name, Age) VALUES ('Tom', 22);

--View elements in order alphabet
SELECT * FROM People ORDER BY Name ASC;
--View elements in order numeric
SELECT * FROM People ORDER BY Age ASC;

--WHERE + ORDER BY
SELECT * FROM People WHERE Age > 30;
SELECT * FROM People WHERE Age < 30 ORDER BY Age ASC;

--DELETE
DELETE FROM People WHERE Age < 30;

--DROP TABLE
DROP TABLE People;