CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT a.actor, aa.age
FROM starring_actors a
JOIN movies m ON a.movie_name = m.movie
JOIN actor_ages aa ON a.actor = aa.actor
WHERE m.genre = (
    SELECT genre
    FROM movies
    GROUP BY genre
    ORDER BY COUNT(*) DESC
    LIMIT 1
)
ORDER BY aa.age DESC, a.actor;

END