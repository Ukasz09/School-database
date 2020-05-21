-- Giving a raise for every teachers who were hired before specific date --
UPDATE
    teachers
SET
    hourly_rate = hourly_rate + hourly_rate * 0.2
WHERE
    employment_date <= '1985-12-31'
