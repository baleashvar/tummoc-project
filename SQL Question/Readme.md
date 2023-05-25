1. Create query for result

Table - routes
id |name | number
1 | 200-D |SBV-BHJ
2 | 300-A |ASD-WER

Table - route_points
id | route_id | order | distance
1 | 1 | 1 | 0
2 | 1 | 2 | 100
3 | 2 | 1 | 0
4 | 2 | 2 | 50
5 | 2 | 3 | 100

Expected Result
route_id |name |total_distance
2 | 300-D |150
1 | 200-A | 100



2.Make a query for get result for same route by stop id for source and destination

Table - routes
id | name | number 
1 | 200-D | SBV-BHJ
2 | 300-A | ASD-WER

table-route_points
id | route_id | order | stop_id
1 | 1 | 1 | 1
2 | 1 |2 | 2
3 | 2 | 1 | 1
4 | 2 | 2 | 2
5 | 2 | 3 | 3

Expected Result
route_id | source_stop_id | dest_stop_id
1 | 1 | 2
2 | 2 | 3

3.
