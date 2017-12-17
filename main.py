import sys
sys.path.append('./modules')

import asyncio
import mysql as datasource
import http_client
import slack
import util
from weather_type import WeatherType

# lambda hundler
def lambda_hundler(event, context):
    main()

# local functions
async def get_task(weather_list):
    taskList = []
    for data in weather_list:
        id  = data.get('id')
        lat = data.get('lat')
        lon = data.get('lon')
        if all(update_value is not None for update_value in [id, lat, lon]):
            taskList.append(asyncio.ensure_future(http_client.weather_api_request(id, lat, lon)))
    return await asyncio.gather(*taskList)


def main():
    weather_list = datasource.read_data()
    loop = asyncio.get_event_loop()
    result_list = loop.run_until_complete(get_task(weather_list))

    for id, result in result_list:
        weather = util.safe_array_get(result.get('weather'), 0, {})
        weather_main = weather.get('main')
        weather_name = WeatherType(weather_main).japanese_name()

        if weather_name is not None:
            datasource.update_data(id, weather_name)
        else:
            slack.send_error_message(slack.error_message_format.format(id, result))
        continue

main()
