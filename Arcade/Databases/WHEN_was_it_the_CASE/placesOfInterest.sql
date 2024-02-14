CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT
  country,
  COALESCE(SUM(CASE WHEN leisure_activity_type = 'Adventure park' THEN number_of_places ELSE 0 END), 0) AS adventure_park,
  COALESCE(SUM(CASE WHEN leisure_activity_type = 'Golf' THEN number_of_places ELSE 0 END), 0) AS golf,
  COALESCE(SUM(CASE WHEN leisure_activity_type = 'River cruise' THEN number_of_places ELSE 0 END), 0) AS river_cruise,
  COALESCE(SUM(CASE WHEN leisure_activity_type = 'Kart racing' THEN number_of_places ELSE 0 END), 0) AS kart_racing
FROM countryActivities
GROUP BY country
ORDER BY country;

END