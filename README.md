# weather-batch
Batch processing for japanese prefectures current weather using OpenWeatherMap API

# Environment
## Language
Python 3.6.3

## Machine(confirmed)
* macOS Sierra 10.12.5
* Ubuntu 16.04

## Database
MySQL 5.7

### Schema
```
# Create db
create database if not exists sample_db character set utf8;

# Create table
create table if not exists weathers (
    id int auto_increment,
    prefecture varchar(10) not null,
    lat double(9, 6) not null,
    lon double(9, 6) not null,
    weather varchar(20) not null,
    created_at datetime,
    updated_at datetime,
    primary_key(id)
) engine = innodb default charset = utf8;
```

# Usage example
```
$ cd path/to/weather-batch
$ vim export_env.sh

# Change values into yours
export MYSQL_USERNAME=<username>
export MYSQL_PASSWORD=<password>
export MYSQL_DB_NAME=<dbname>
export MYSQL_HOST=<host>
export MYSQL_PORT=<port>

export OPEN_WEATHER_MAP_APP_ID=XXXXXXXXXXXXXXXXXXXXXX

export SLACK_TOKEN=YYYYYYYYYYYYYYYYYYYYY

$ source export_env.sh
$ python main.py
```
