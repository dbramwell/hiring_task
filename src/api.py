import aiohttp
from typing import List
from src.models import Member


class MemberApi:
    async def fetch(self) -> List[Member]:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://bn-hiring-challenge.fly.dev/members.json"
            ) as response:
                json = await response.json()
                return [Member(**data) for data in json]
