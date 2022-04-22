CREATE
	MATERIALIZED VIEW visits1
	AS
SELECT
	station,
	stationCode.metroLineCode AS Line,
	stationCode.startDate AS startDate,
    ARRAY_AGG(visitallday order by date) AS visitDay,
	SUM(visitallday) AS visits,
    CONCAT('{',SUM(visit_hour_5),',',
        SUM(visit_hour_6),',',
        SUM(visit_hour_7),',',
        SUM(visit_hour_8),',',
        SUM(visit_hour_9),',',
        SUM(visit_hour_10),',',
        SUM(visit_hour_11),',',
        SUM(visit_hour_12),',',
        SUM(visit_hour_13),',',
        SUM(visit_hour_14),',',
        SUM(visit_hour_15),',',
        SUM(visit_hour_16),',',
        SUM(visit_hour_17),',',
        SUM(visit_hour_18),',',
        SUM(visit_hour_19),',',
        SUM(visit_hour_20),',',
        SUM(visit_hour_21),',',
        SUM(visit_hour_22),',',
        SUM(visit_hour_23),',',
        SUM(visit_hour_0),',',
        SUM(visit_hour_1),'}'
        )::int[] AS hour_sum
FROM
	visitsdata
JOIN
	stationCode
		ON station = stationCode.stationCode
GROUP BY
	station,
	Line,
	startDate
ORDER BY
	station
;

CREATE UNIQUE INDEX station_index ON visits1 (station);

CREATE TABLE visit_table1 AS
SELECT * FROM visits1;