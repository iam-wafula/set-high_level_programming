# Python - Object Relational Mapping

## Description

This project introduces Object-Relational Mapping (ORM) in Python.

The project covers two main approaches to interacting with MySQL databases:

- Using `MySQLdb` to execute SQL queries directly.
- Using `SQLAlchemy` to interact with databases through Python classes and objects.

The project demonstrates how to connect Python applications to MySQL databases, retrieve and manipulate data, protect against SQL injection, and create relationships between database tables using SQLAlchemy.

## Learning Objectives

At the end of this project, I am able to:

- Connect to a MySQL database from Python.
- Use `MySQLdb` to execute SQL queries.
- Retrieve data from MySQL tables.
- Filter database results.
- Protect SQL queries against SQL injection.
- Use SQLAlchemy for Object-Relational Mapping.
- Define database models using Python classes.
- Create and use relationships between models.
- Perform CRUD operations using SQLAlchemy.
- Use SQLAlchemy relationships to access related objects.
- Use eager loading to retrieve related objects efficiently.

## Technologies

- Python 3
- MySQL
- MySQLdb
- SQLAlchemy
- Ubuntu/Linux
- Git and GitHub

## Project Structure

| Task | File | Description |
| --- | --- | --- |
| 0 | `0-select_states.py` | Lists all states using MySQLdb |
| 1 | `1-filter_states.py` | Lists states starting with N |
| 2 | `2-my_filter_states.py` | Filters states using user input |
| 3 | `3-my_safe_filter_states.py` | Filters states safely from SQL injection |
| 4 | `4-cities_by_state.py` | Lists all cities with their states |
| 5 | `5-filter_cities.py` | Lists cities belonging to a specified state |
| 6 | `model_state.py` | Defines the State SQLAlchemy model |
| 6 | `6-model_state.py` | Creates the states table |
| 7 | `7-model_state_fetch_all.py` | Lists all State objects |
| 8 | `8-model_state_fetch_first.py` | Retrieves the first State object |
| 9 | `9-model_state_filter_a.py` | Lists states containing the letter a |
| 10 | `10-model_state_my_get.py` | Retrieves a state by name |
| 11 | `11-model_state_insert.py` | Adds Louisiana to the database |
| 12 | `12-model_state_update_id_2.py` | Changes state ID 2 to New Mexico |
| 13 | `13-model_state_delete_a.py` | Deletes states containing a |
| 14 | `model_city.py` | Defines the City SQLAlchemy model |
| 14 | `14-model_city_fetch_by_state.py` | Lists cities with their states |
| 15 | `relationship_state.py` | Defines State-City relationships |
| 15 | `relationship_city.py` | Defines the City model for relationships |
| 15 | `100-relationship_states_cities.py` | Creates a State and City using relationships |
| 16 | `101-relationship_states_cities_list.py` | Lists states and their cities |
| 17 | `102-relationship_cities_states_list.py` | Lists cities with their states |

## Databases

The project uses several MySQL databases for different tasks, including:

- `hbtn_0e_0_usa`
- `hbtn_0e_4_usa`
- `hbtn_0e_6_usa`
- `hbtn_0e_14_usa`
- `hbtn_0e_100_usa`
- `hbtn_0e_101_usa`

## SQLAlchemy Relationships

The final tasks introduce a relationship between the `State` and `City` classes.

A State can have multiple cities, while each City belongs to one State.

The relationship allows access such as:

```python
state.cities
