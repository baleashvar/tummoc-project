SELECT
  station_id,
  station_name,
  slot,
  time
FROM (
  SELECT
    station_id,
    name AS station_name,
    slot,
    time
  FROM station
  INNER JOIN times ON station.id = times.station_id
) AS r
WHERE station_id = 1 AND slot IN (1, 2);
