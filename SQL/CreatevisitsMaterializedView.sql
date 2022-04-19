CREATE
	MATERIALIZED VIEW visits
	AS
SELECT
	station,
	stationCode.metroLineCode AS Line,
	stationCode.startDate AS startDate,
	ARRAY_AGG(visitallday) AS visitDay,
	SUM(visitallday) AS visits
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

CREATE UNIQUE INDEX station_index ON visits (station);