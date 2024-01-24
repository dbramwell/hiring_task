import aiohttp
from typing import List, Any
from src.models import Member, Job


class Api:
    async def fetch(self) -> List[Any]:
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url) as response:
                json = await response.json()
                return [self.model(**data) for data in json]


class MemberApi(Api):
    model = Member
    url: str = "https://bn-hiring-challenge.fly.dev/members.json"


class JobApi(Api):
    model = Job
    url: str = "https://bn-hiring-challenge.fly.dev/jobs.json"
