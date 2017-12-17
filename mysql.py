import json
import logger
import os
import pymysql
import sys

logger = logger.instantiate_logger()

def connect_mysql():
    username = os.environ['MYSQL_USERNAME']
    password = os.environ['MYSQL_PASSWORD']
    db_name  = os.environ['MYSQL_DB_NAME']
    host     = os.environ['MYSQL_HOST']

    try:
        connection = pymysql.connect(
                host,
                user=username,
                passwd=password,
                db=db_name,
                connect_timeout=5,
                charset='utf8',
                cursorclass=pymysql.cursors.DictCursor
        )
    except Exception as e:
        logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
        logger.error("reason: {}".format(e))
        sys.exit()

    return connection

def read_data():
    u"""
    データ取得用メソッド
    """

    connection = connect_mysql()

    try:
        weather_list = []
        with connection.cursor() as cursor:
            query = "SELECT id, lat, lon FROM weathers"
            cursor.execute(query)
            query_results = cursor.fetchall()

            for weather in query_results:
                id  = weather.get('id')
                lat = weather.get('lat')
                lon = weather.get('lon')
                weather_list.append({
                    'id' : id,
                    'lat': lat,
                    'lon': lon
                })
        return weather_list
    finally:
        connection.close()

def update_data(id, weather):
    u"""
    データ更新用メソッド
    """

    connection = connect_mysql()

    try:
        with connection.cursor() as cursor:
            query = '''
                UPDATE
                    weathers
                SET
                    weather = %s, updated_at = NOW()
                WHERE
                    id = %s
            '''
            cursor.execute(query, (weather, id))
        connection.commit()
    finally:
        connection.close()
