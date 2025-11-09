# Mini-Database-Project

A small bus reservation system built with HTML forms, PHP and MySQL. The project connects front-end forms to a MySQL backend so users can register, book seats, view reservations, and admins can manage schedules and buses.

Repository description: "I set up a mini database for a bus reservation company using data from a HTML Forms. I connected everything with PHP and built it on MySQL, making it easy to handle reservations smoothly."

---

## Table of contents
- About
- Included files
- Features
- Tech stack
- Prerequisites
- Quick install
- Database: import & schema
- Configuration (example)
- How to use
- Troubleshooting
- Contact

---

## About
This repo is a minimal working example of a bus reservation workflow implemented with plain PHP, HTML forms and a MySQL database. It is intended for local testing / learning and can be deployed on any PHP + MySQL hosting or local stacks like XAMPP, WAMP, MAMP, LAMP.

---

## Included files 
- booking.html — booking form (frontend)
- booking.php — booking handler or booking page (backend)
- register.html — user registration form
- register.php — registration handler
- buscompanydb.sql (or buscompanydb.sql) — SQL dump/schema for creating the database and tables
- register.avif — image used in pages
- reserve.webp — image used in pages
- (Additional PHP/HTML files may exist in the repo; adjust paths below if different)

Note: You mentioned images in your message; image set shown in Image 1 includes register.avif and reserve.webp (these are referenced above).

---

## Features
- Register new customers via HTML form
- Book seats for a schedule using a booking form
- Store customers, buses, schedules and reservations in MySQL
- Example SQL file included to create required tables

---

## Tech stack
- HTML, CSS (optional)
- PHP (procedural scripts)
- MySQL / MariaDB
- Run locally with XAMPP, WAMP, MAMP, LAMP or any PHP-enabled web server

---

## Prerequisites
- PHP 7.x or later
- MySQL 5.7+ or MariaDB
- A running web server (Apache/Nginx) configured for PHP
- Access to phpMyAdmin or mysql CLI for importing SQL

---

## Quick install (local)
1. Clone the repository:
   git clone https://github.com/Ginidu2003/Mini-Database-Project.git

2. Copy the project files into your web server directory (for XAMPP: C:\xampp\htdocs\Mini-Database-Project).

3. Start Apache and MySQL through your local environment (XAMPP/MAMP/etc).

4. Create and import the database:
   - Using phpMyAdmin: import the `buscompanydb.sql` file.
   - Or from command line:
     mysql -u root -p < buscompanydb.sql
     (or `mysql -u root -p bus_reservation < buscompanydb.sql` if the dump creates `bus_reservation` and you want a specific name)

5. Change configuration in .php files for DB connection (example below) 

6. Open a browser and navigate to:
   http://localhost/Mini-Database-Project/register.html
   http://localhost/Mini-Database-Project/booking.html

---

## Database: import & schema
Use the provided SQL file `buscompanydb.sql` in the repo to create tables and seed data (if the file includes seed data). If you need a quick reference schema, here is a compact example of the typical tables used.

```sql
-- Example schema (reference only; use buscompanydb.sql from repo)
CREATE DATABASE IF NOT EXISTS bus_reservation;
USE bus_reservation;

CREATE TABLE IF NOT EXISTS buses (
  id INT AUTO_INCREMENT PRIMARY KEY,
  bus_number VARCHAR(50),
  capacity INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS routes (
  id INT AUTO_INCREMENT PRIMARY KEY,
  origin VARCHAR(100),
  destination VARCHAR(100),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS schedules (
  id INT AUTO_INCREMENT PRIMARY KEY,
  bus_id INT,
  route_id INT,
  departure_datetime DATETIME,
  arrival_datetime DATETIME,
  fare DECIMAL(10,2),
  FOREIGN KEY (bus_id) REFERENCES buses(id) ON DELETE CASCADE,
  FOREIGN KEY (route_id) REFERENCES routes(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS customers (
  id INT AUTO_INCREMENT PRIMARY KEY,
  full_name VARCHAR(150),
  email VARCHAR(150),
  phone VARCHAR(50),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS reservations (
  id INT AUTO_INCREMENT PRIMARY KEY,
  schedule_id INT,
  customer_id INT,
  seat_number VARCHAR(10),
  status ENUM('booked','cancelled','completed') DEFAULT 'booked',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (schedule_id) REFERENCES schedules(id) ON DELETE CASCADE,
  FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE
);
```

---

## Configuration (example)
chnage your configurations in .php files 

```php
<?php
// config.php - example
$db_host = 'your server';
$db_user = 'your user name';
$db_pass = 'your password';
$db_name = 'data base name'; // or use the DB name created by buscompanydb.sql


```


---

## How to use
- register.html -> submits to register.php to create a customer record.
- booking.html -> submit to booking.php to create reservation records.

- To view or manage data directly, open phpMyAdmin or use SQL queries against the imported database.



---




---

## Troubleshooting
- "Cannot connect to DB": check MySQL is running and credentials in `config.php` match.
- Forms not submitting: ensure `<form method="post" action="...">` uses correct `name` attributes and the action path exists.
- SQL errors: import `buscompanydb.sql` and check table/column names used by PHP scripts match the schema.



---





## Contact
Owner: @Ginidu2003
ginidusampath1@gmail.com

---
