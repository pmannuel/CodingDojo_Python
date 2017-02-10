-- Question 1
SELECT city.city_id, CONCAT(customer.first_name, ' ', customer.last_name) AS fullnames, customer.email, address.address
FROM city
LEFT JOIN address ON city.city_id = address.city_id
LEFT JOIN customer ON address.address_id = customer.address_id
WHERE city.city_id = 312;

-- Question 2
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre
FROM category
LEFT JOIN film_category ON category.category_id = film_category.category_id
LEFT JOIN film ON film_category.film_id = film.film_id
where category.name = "Comedy";

-- Question 3
SELECT actor.first_name, film.title AS Movies
FROM actor
LEFT JOIN film_actor ON actor.actor_id = film_actor.actor_id
LEFT JOIN film ON film_actor.film_id = film.film_id
WHERE actor.actor_id = 5;

-- Question 4
SELECT store.store_id, city.city_id, CONCAT(customer.first_name, ' ', customer.last_name) AS fullnames, customer.email, address.address
FROM customer
LEFT JOIN store ON customer.store_id = store.store_id
LEFT JOIN address ON customer.address_id = address.address_id
LEFT JOIN city ON address.city_id = city.city_id
WHERE store.store_id = 1 AND city.city_id IN (1,42, 312,459);

-- Question 5
SELECT film.title, film.description, film.release_year, film_rating, film.special_feature
FROM film
LEFT JOIN film_actor ON film_actor.film_id = film.film_id
WHERE film.rating = "G" AND film.special_features LIKE '%Behind the scenes%' AND actor_id = 15;


-- Question 6
SELECT film.film_id, film.title, actor.first_name
FROM film
LEFT JOIN film_actor ON film.film_id = film_actor.film_id
LEFT JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE film.film_id = 369;

-- Question 7
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre
FROM category
LEFT JOIN film_category ON category.category_id = film_category.category_id
LEFT JOIN film ON film_category.film_id = film.film_id
WHERE film.rental_rate = 2.99
and category.name LIKE '%Drama%'

-- Question 8