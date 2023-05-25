SELECT
  route_id,
  name,
  SUM(distance) AS total_distance
FROM routes
LEFT JOIN route_points ON routes.id = route_points.route_id
GROUP BY route_id, name;
