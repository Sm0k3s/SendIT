[![Build Status](https://travis-ci.org/Sm0k3s/SendIT.svg?branch=ft-logout-user-v1-161869682)](https://travis-ci.org/Sm0k3s/SendIT)
[![Coverage Status](https://coveralls.io/repos/github/Sm0k3s/SendIT/badge.svg?branch=ch-update-tests-161908326)](https://coveralls.io/github/Sm0k3s/SendIT?branch=ch-update-tests-161908326)
[![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)


# SendIT
 SendIT is a courier service that helps users deliver parcels to different destinations. SendIT provides courier quotes based on weight categories.

## Required Features

1. Users can create an account and log in.
2. Users can create a parcel delivery order.
3. Users can change the destination of a parcel delivery order.
4. Users can cancel a parcel delivery order.
5. Users can see the details of a delivery order.
6. Admin can change the ​ status​​ and present​​ ​ location​​ of a parcel delivery order.

## The User Interface
* Follow the link below to access it
* [SendIT UI](https://sm0k3s.github.io/SendIT/UI/)

## Installation

* Clone this repo

```bash
$ git clone https://github.com/sm0k3s/SendIT.git
```
* Cd into it
* Make a virtual environment and activate it

```bash
$ python3 -m venv venv 	
$ source venv/bin/activate		
```
* Install the dependencies

```bash
$ pip install -r requirements.txt
```
* Run the app

```bash
$ export FLASK_APP=run.py
$ flask run
```
* Test the endpoints on Postman/Curl/Insomnia

Open postman and navigate to the localhost
```bash
http://localhost:5000/
```
Test the available endpoints

## Available endpoints
|  Endpoint  | Description  |
|  ---  | --- |
| `POST api/v1/auth/signup` | Creates a new user |
| `POST api/v1/auth/login`  | Users can log in to their accounts |
| `DELETE api/v1/users/logout` | Users can logout |
| `POST api/v1/parcels` | Creates a parcel delivery order |
| `GET api/v1/parcels` | Gets all parcel delivery orders |
| `PUT api/v1/parcels/<parcel_id>/cancel` | User can cancel a parcel order |
| `GET api/v1/parcels/<parcel_id>` | Gets a specific parcel by its id |
| `GET api/v1/users/<user_id>/parcels` | Gets parcel orders by a specific user |
| `PUT api/v1/parcels/<parcel_id>` | Edits the destination of a parcel order |

## Running tests
* Cd into the directory where the app is located at and
run :
```bash
$ pytest --cov app  #with coverage
```
