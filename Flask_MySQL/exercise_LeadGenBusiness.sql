-- Question 1
SELECT DATE_FORMAT(charged_datetime, '%M') AS month_of_charge, SUM(amount)
FROM billing
WHERE MONTH(charged_datetime) = 03;
GROUP BY month_of_charge

-- Question 2
SELECT clients.client_id AS client_name, SUM(amount)
FROM billing
LEFT JOIN clients ON billing.client_id = clients.client_id
WHERE clients.client_id = 2
GROUP BY clients.client_id

-- Question 3
SELECT clients.client_id, sites.domain_name
FROM clients
LEFT JOIN sites ON clients.client_id = sites.client_id
WHERE clients.client_id = 10

-- Question 4
SELECT clients.client_id, COUNT(sites.domain_name) AS number_of_websites, DATE_FORMAT(sites.created_datetime, '%M') AS month_created, DATE_FORMAT(sites.created_datetime, '%Y') AS year_created
FROM clients
LEFT JOIN sites ON clients.client_id = sites.client_id
WHERE clients.client_id = 1
GROUP BY sites.created_datetime

-- Question 5
SELECT sites.domain_name AS website, COUNT(leads.leads_id) AS number_of_leads, DATE_FORMAT(leads.registered_datetime, '%M %d, %Y')
FROM sites
LEFT JOIN leads ON leads.site_id = sites.site_id
WHERE leads.registered_datetime BETWEEN "2011/01/01" AND "2011/02/15"
GROUP BY sites.domain_name

-- Question 6
SELECT CONCAT(clients.first_name, clients.last_name) AS client_names, COUNT(leads.leads_id) AS number_of_leads
FROM clients
LEFT JOIN sites ON clients.client_id = sites.client_id
LEFT JOIN leads ON sites.site_id = leads.site_id
WHERE sites.created_datetime BETWEEN "2011/01/01" AND "2011/12/31"
GROUP BY clients.client_id

-- Questions 7
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_names, COUNT(leads.leads_id) AS number_of_leads, DATE_FORMAT(leads.registered_datetime, '%M') AS month
FROM clients
LEFT JOIN sites ON clients.client_id = sites.client_id
LEFT JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN "2011/01/01" AND "2011/06/30"
GROUP BY leads.leads_id

-- Questions 8
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_names, sites.domain_name AS website, COUNT(leads.leads_id) AS number_of_leads, DATE_FORMAT(sites.created_datetime, '%M %d, %Y') AS date_generated
FROM sites
LEFT JOIN clients ON clients.client_id = sites.client_id
LEFT JOIN leads ON leads.site_id = sites.site_id
WHERE leads.registered_datetime >= "2011/01/01" AND leads.registered_datetime <= "2011/12/31"
GROUP BY sites.client_id, website

-- Question 9
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_names, SUM(billing.amount) AS Total_Revenue, MONTHNAME(charged_datetime) AS month_charge, YEAR(charged_datetime) AS year_charge
FROM billing
LEFT JOIN clients ON billing.client_id = clients.client_id
GROUP BY MONTH(charged_datetime), YEAR(charged_datetime), clients.client_id

-- Question 10
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, GROUP_CONCAT(' ', sites.domain_name) AS website
FROM sites
LEFT JOIN clients ON clients.client_id = sites.client_id
GROUP BY client_name