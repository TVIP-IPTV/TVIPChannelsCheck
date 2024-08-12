import sys
import requests
import json
import asyncio

from loguru import logger
from core.tms import TMS

logger.remove()
logger.add(sys.stderr, format='<white>{time:HH:mm:ss}</white>'
                           ' | <level>{level: <8}</level>'
                           ' - <white>{message}</white>')

def check_m3u8(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200 and "#EXTM3U" in response.text:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False

def check_channels(channels):
    channel_work = 0
    channel_died = 0
    content_json = json.loads(channels['content'])

    for channel in content_json['data']:
        if channel.get('enabled', False):
            channel_name = channel.get('displayName', 'Unnamed Channel')
            channel_url = channel.get('url', None)
            
            if channel_url:
                if check_m3u8(channel_url):
                    channel_work += 1
                    logger.success(f"Рабочий канал: {channel_name}\nURL: {channel_url}\n")
                else:
                    channel_died += 1
                    logger.error(f"Ошибка в канале: {channel_name}\nURL: {channel_url}\n")
            else:
                logger.warning(f"URL отсутствует для канала: {channel_name}")

    logger.success(f'Рабочих каналов: {channel_work}. Ошибок в канале: {channel_died}')

if __name__ == "__main__":
    tms_link = input('Введите URL TMS: ')
    tms_token = input('Введите TOKEN TMS: ')

    tms = TMS(
        tms_url=tms_link,
        token=tms_token
    )
    
    channels = asyncio.run(tms.get_channels())
    
    check_channels(channels)
