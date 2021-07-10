-- email: jeffreywei@berkeley.edu


-- You are a bike rental shop owner.

-- To run your shop smoothly, you created some tables
-- related to your shop.
--      `bike` table to keep track of basic information about the bikes
--      `inventory` table to keep track of the inventory in the shop.
--          NOTE: the total can be greater than the sum of available and rented,
--          meaning that there can be some missing copies.
--      `march_rental` table to keep track of rental history of the month of march
--
-- This question is in 2 parts.
--
-- NOTE: The tests for this question are NOT comprehensive, as they only
-- refer to the data tables as shown below. We will be grading this question
-- manually.
--
-- NOTE: In all scheme/sql questions you can put a multi-line answer
-- in a blank


CREATE TABLE bike AS
    SELECT "bike a" AS name, "*****" AS ratings, 2017 AS year UNION
    SELECT "bike b" , "*" , 1988 UNION
    SELECT "bike c" , "***" , 2010 UNION
    SELECT "bike d" , "***" , 2018 UNION
    SELECT "bike e" , "***" , 2020 UNION
    SELECT "bike f" , "*****" , 2019;

CREATE TABLE inventory AS
    SELECT "bike a" AS name, 1 AS available, 2 AS rented, 3 AS total UNION
    SELECT "bike b" , 2 , 3 , 10 UNION
    SELECT "bike c" , 4 , 1 , 9 UNION
    SELECT "bike d" , 7 , 2 , 11 UNION
    SELECT "bike f" , 0 , 12, 20;

CREATE TABLE march_rental AS
    SELECT "bike c" AS name, 1 AS rented_date, 5 AS return_date UNION
    SELECT "bike f" , 4 , 10 UNION
    SELECT "bike a" , 5 , 8 UNION
    SELECT "bike b" , 5 , 9 UNION
    SELECT "bike d" , 9 , 13 UNION
    SELECT "bike f" , 10 , 15 UNION
    SELECT "bike a" , 18, 26;

-- Part a : Complete the SQL statement below to select a one-column table
-- of bike names whose release year is 2010 or later and have at least 1 copy
-- missing. Order your results by the number of missing copies, biggest to
-- smallest.
--
-- To run tests just for this part run
--      python3 ok -q a

CREATE TABLE parta AS
    SELECT b.name AS name
    FROM bike as b, inventory as i
    WHERE b.year >= 2010 AND b.name == i.name AND i.available + i.rented <= i.total - 1 ORDER BY i.available + i.rented - i.total;

-- Part b : We are interested in seeing how renting behavior correlates with
--      rating.
--
-- Complete the SQL statement below to create a two-column table that shows
-- how many bikes per star rating have been rented out for a period of more
-- than 3 days.
--
-- For example, if a bike was rented out on march 3 and returned on march 6,
-- that would not count as being rented out for more than 3 days, but if it
-- was returned on march 7 that would count as more than 3 days.
--
-- Each row should contain the star rating and number of bikes. Only include rating
-- categories that have at least 2 bikes satisfying the condition.
--
-- To run tests just for this part run
--      python3 ok -q b

CREATE TABLE partb AS
    WITH totalDays(bikeName, totals) AS (
        SELECT b.name, SUM(m.return_date - m.rented_date)
        FROM bike as b, march_rental as m
        WHERE b.name = m.name
    )
    SELECT b.ratings as stars, COUNT(t.totals > 3)
    FROM bike as b, totalDays as t
    WHERE b.name = t.bikeName;


-- ORIGINAL SKELETON FOLLOWS


-- -- You are a bike rental shop owner.

-- -- To run your shop smoothly, you created some tables
-- -- related to your shop.
-- --      `bike` table to keep track of basic information about the bikes
-- --      `inventory` table to keep track of the inventory in the shop.
-- --          NOTE: the total can be greater than the sum of available and rented,
-- --          meaning that there can be some missing copies.
-- --      `march_rental` table to keep track of rental history of the month of march
-- --
-- -- This question is in 2 parts.
-- --
-- -- NOTE: The tests for this question are NOT comprehensive, as they only
-- -- refer to the data tables as shown below. We will be grading this question
-- -- manually.
-- --
-- -- NOTE: In all scheme/sql questions you can put a multi-line answer
-- -- in a blank


-- CREATE TABLE bike AS
--     SELECT "bike a" AS name, "*****" AS ratings, 2017 AS year UNION
--     SELECT "bike b" , "*" , 1988 UNION
--     SELECT "bike c" , "***" , 2010 UNION
--     SELECT "bike d" , "***" , 2018 UNION
--     SELECT "bike e" , "***" , 2020 UNION
--     SELECT "bike f" , "*****" , 2019;

-- CREATE TABLE inventory AS
--     SELECT "bike a" AS name, 1 AS available, 2 AS rented, 3 AS total UNION
--     SELECT "bike b" , 2 , 3 , 10 UNION
--     SELECT "bike c" , 4 , 1 , 9 UNION
--     SELECT "bike d" , 7 , 2 , 11 UNION
--     SELECT "bike f" , 0 , 12, 20;

-- CREATE TABLE march_rental AS
--     SELECT "bike c" AS name, 1 AS rented_date, 5 AS return_date UNION
--     SELECT "bike f" , 4 , 10 UNION
--     SELECT "bike a" , 5 , 8 UNION
--     SELECT "bike b" , 5 , 9 UNION
--     SELECT "bike d" , 9 , 13 UNION
--     SELECT "bike f" , 10 , 15 UNION
--     SELECT "bike a" , 18, 26;

-- -- Part a : Complete the SQL statement below to select a one-column table
-- -- of bike names whose release year is 2010 or later and have at least 1 copy
-- -- missing. Order your results by the number of missing copies, biggest to
-- -- smallest.
-- --
-- -- To run tests just for this part run
-- --      python3 ok -q a

-- CREATE TABLE parta AS
--     SELECT "replace this;";

-- -- Part b : We are interested in seeing how renting behavior correlates with
-- --      rating.
-- --
-- -- Complete the SQL statement below to create a two-column table that shows
-- -- how many bikes per star rating have been rented out for a period of more
-- -- than 3 days.
-- --
-- -- For example, if a bike was rented out on march 3 and returned on march 6,
-- -- that would not count as being rented out for more than 3 days, but if it
-- -- was returned on march 7 that would count as more than 3 days.
-- --
-- -- Each row should contain the star rating and number of bikes. Only include rating
-- -- categories that have at least 2 bikes satisfying the condition.
-- --
-- -- To run tests just for this part run
-- --      python3 ok -q b

-- CREATE TABLE partb AS
--     SELECT "replace this;";

