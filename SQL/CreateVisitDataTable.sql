CREATE TABLE visitsData
AS
SELECT
	date,
	CONCAT(stationcode.stationCode, ' ',   visitsData_raw.station_out)::VARCHAR(30) AS station,
	stationCode.metrolinecode AS line,
	SUM(visit_hour_5)::int AS visit_hour_5,
	SUM(visit_hour_6)::int AS visit_hour_6,
	SUM(visit_hour_7)::int AS visit_hour_7,
	SUM(visit_hour_8)::int AS visit_hour_8,
	SUM(visit_hour_9)::int AS visit_hour_9,
	SUM(visit_hour_10)::int AS visit_hour_10,
	SUM(visit_hour_11)::int AS visit_hour_11,
	SUM(visit_hour_12)::int AS visit_hour_12,
	SUM(visit_hour_13)::int AS visit_hour_13,
	SUM(visit_hour_14)::int AS visit_hour_14,
	SUM(visit_hour_15)::int AS visit_hour_15,
	SUM(visit_hour_16)::int AS visit_hour_16,
	SUM(visit_hour_17)::int AS visit_hour_17,
	SUM(visit_hour_18)::int AS visit_hour_18,
	SUM(visit_hour_19)::int AS visit_hour_19,
	SUM(visit_hour_20)::int AS visit_hour_20,
	SUM(visit_hour_21)::int AS visit_hour_21,
	SUM(visit_hour_22)::int AS visit_hour_22,
	SUM(visit_hour_23)::int AS visit_hour_23,
	SUM(visit_hour_0)::int AS visit_hour_0,
	SUM(visit_hour_1)::int AS visit_hour_1,
	SUM(visitallday)::int AS visitallday
FROM
	visitsData_raw
JOIN
	stationcode
		ON visitsData_raw.station_out = stationcode.stationName
WHERE
	date > startDate
GROUP BY
	date, station, metrolinecode
LIMIT
	150
;