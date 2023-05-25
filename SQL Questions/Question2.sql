SELECT
  route_id,
  source_stop_id,
  dest_stop_id
FROM (
  SELECT
    route_id,
    stop_id AS source_stop_id,
    NULL AS dest_stop_id
  FROM route_points
  WHERE order = 1
  UNION ALL
  SELECT
    route_id,
    NULL AS source_stop_id,
    stop_id AS dest_stop_id
  FROM route_points
  WHERE order = 2
) AS r
WHERE source_stop_id < dest_stop_id;
