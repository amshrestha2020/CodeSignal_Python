CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT f.flight_id, p.number_of_seats - COUNT(pr.seat_no) AS free_seats
    FROM flights f
    JOIN planes p ON f.plane_id = p.plane_id
    LEFT JOIN purchases pr ON f.flight_id = pr.flight_id
    GROUP BY f.flight_id
    ORDER BY f.flight_id;
END