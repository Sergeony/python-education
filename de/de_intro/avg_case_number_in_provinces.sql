SELECT province_name, avg(cases_total) AS avg_case_number
FROM ita_covid
GROUP BY province_name
ORDER BY avg(cases_total) DESC;
