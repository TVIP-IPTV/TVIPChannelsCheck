import aiohttp
from typing import Optional, Dict


class TMS:
    def __init__(self, tms_url: str, token: str) -> None:
        self.tms_url = tms_url
        self.token = token

    async def _request(self, page: str, data: Optional[Dict] = None, type_: str = 'GET') -> dict:
        headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json',
            'X-Content-Type-Options': 'nosniff'
        }

        async with aiohttp.ClientSession() as session:
            async with session.request(method=type_, url=f'{self.tms_url}/{page}', json=data, headers=headers) as response:
                if response.status in (200, 401):
                    content_type = response.headers.get('Content-Type', '')
                    if 'application/json' in content_type:
                        return await response.json()
                    else:
                        return {"error": "Unexpected content type", "content": await response.text()}
                else:
                    return {"error": f"Unexpected status code: {response.status}", "content": await response.text()}

    async def get_channels(
        self,
        start: int = 0,
        limit: int = 1000
    ) -> dict:
        return await self._request(
            page=f'api/admin/channel/?start={start}&limit={limit}',
            data={},
            type_='GET'
        )