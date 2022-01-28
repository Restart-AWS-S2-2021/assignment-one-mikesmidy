import sqlite3
from sqlite3 import Connection

connection = sqlite3.connect("sakila.db")
# Use created functions for your 20 queries below.

cursor = connection.cursor()


def one_query_order_by():
    output = cursor.execute("SELECT first_name, last_name "
                            "FROM actor "
                            "ORDER BY last_update;").fetchall()
    print(output)

def two_query_order_by():
    output = cursor.execute("SELECT * "
                            "FROM film "
                            "ORDER BY title;").fetchall()
    print(output)

def three_query_order_by():
    output = cursor.execute("SELECT rental_rate, title,release_year "
                            "FROM film "
                            "ORDER BY rental_rate desc;").fetchall()
    print(output)

def four_query_where():
    output = cursor.execute("SELECT district "
                            "FROM address "
                            "WHERE postal_code "
                            "BETWEEN 16500 AND 19000;").fetchall()
    print(output)

def five_query_where():
    output = cursor.execute("SELECT first_name "
                            "FROM staff "
                            "WHERE active = true;").fetchall()
    print(output)

def six_query_where():
    output = cursor.execute("SELECT first_name, last_name "
                            "FROM customer "
                            "WHERE last_name='RODRIQUEZ';").fetchall()
    print(output)

def seven_query_delete():
    output = cursor.execute("DELETE FROM payment "
                            "WHERE amount=1.99;").fetchall()
    print(output)

def eight_query_update():
    output = cursor.execute("UPDATE country SET country = ' Mike Country' "
                            "WHERE country_id = 68;").fetchall()
    print(output)

def nine_query_update():
    output = cursor.execute("UPDATE actor SET first_name = ' Jeff' "
                            "WHERE last_name = 'Probst';").fetchall()
    print(output)

def ten_query_update():
    output = cursor.execute("UPDATE customer "
                            "SET first_name = ' Deb', last_name='Smith', email='debsmith@gmail.com'  "
                            "WHERE customer_id = 25;").fetchall()
    print(output)

def eleven_query_insert_into():
    output = cursor.execute("INSERT INTO category (name,last_update) "
                            "VALUES ('Fantasy Drama', CURRENT_TIMESTAMP);").fetchall()
    print(output)

def twelft_query_insert_into():
    output = cursor.execute("INSERT INTO city (city,country_id, last_update) "
                            "VALUES ('Ghost Town', 8, CURRENT_TIMESTAMP);").fetchall()
    print(output)

def thirteen_query_insert_into():
    output = cursor.execute(
        "INSERT INTO film (title,language_id, rental_duration, rental_rate, replacement_cost, last_update) "
        "VALUES ('Fast & Furious 100 - Reanimation of Torreto', 1, 2, 18.99, 299.99, CURRENT_TIMESTAMP);").fetchall()
    print(output)

def fourteen_query_insert_into():
    output = cursor.execute("INSERT INTO language (name, last_update) "
                            "VALUES ('Elastic AWS Marketing Language', CURRENT_TIMESTAMP);").fetchall()
    print(output)

def fifthteen_query_insert_into():
    output = cursor.execute("INSERT INTO address (address, district, city_id, phone, last_update) "
                            "VALUES ('Ducktales Road 2', 'Gotham' , 5, '8052', CURRENT_TIMESTAMP);").fetchall()
    print(output)

def sixteen_query_inner_join():
    output = cursor.execute("SELECT city.city, country.country "
                            "FROM city "
                            "INNER JOIN country ON city.country_id=country.country_id;").fetchall()
    print(output)

def seventeen_query_inner_join():
    output = cursor.execute("SELECT staff.first_name, staff.last_name, address.address "
                            "FROM staff "
                            "INNER JOIN address ON staff.address_id=address.address_id").fetchall()
    print(output)

def eighteen_query_self_join():
    output = cursor.execute("SELECT A.title AS FilmeName1, B.title AS FilmName2, A.release_year "
                            "FROM film A, film B "
                            "WHERE A.film_id <> B.film_id "
                            "AND A.release_year = B.release_year  "
                            "ORDER BY A.release_year desc;").fetchall()
    print(output)

def nineteen_query_left_join():
    output = cursor.execute("SELECT customer.first_name, payment.payment_id, payment.amount "
                            "FROM customer "
                            "LEFT JOIN payment ON customer.customer_id = payment.customer_id "
                            "WHERE payment.amount=0.99 "
                            "ORDER BY customer.first_name;").fetchall()
    print(output)

def twenty_query_self_join():
    output = cursor.execute("SELECT A.first_name AS Actor1, B.first_name AS Actor2, A.last_name "
                            "FROM actor A, actor B "
                            "WHERE A.actor_id <> B.actor_id "
                            "AND A.last_name = B.last_name "
                            "ORDER BY A.last_name;").fetchall()

    print(output)