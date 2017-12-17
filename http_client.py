import aiohttp
import asyncio
import os

async def weather_api_request(id, lat, lon):
    app_id = os.environ['OPEN_WEATHER_MAP_APP_ID']
    url = 'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}'.format(lat, lon, app_id)
    semaphore = asyncio.Semaphore(5)
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return (id, await response.json())
