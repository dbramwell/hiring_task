import pytest
from src.api import MemberApi, JobApi
from typing import List, TypedDict


class MemberJson(TypedDict):
    name: str
    bio: str


class MockResponse:
    def __init__(self, response_data):
        self.response_data = response_data

    async def json(self) -> List[MemberJson]:
        return self.response_data

    async def __aexit__(self, exc_type, exc, tb):
        pass

    async def __aenter__(self):
        return self


class TestMemberApi:
    @pytest.mark.asyncio
    async def test_fetch(self, mocker):
        api = MemberApi()
        data = [
            {
                "name": "David",
                "bio": "I am an engineer",
            },
            {
                "name": "Fred",
                "bio": "I am a designer",
            },
        ]
        resp = MockResponse(data)
        mocker.patch("aiohttp.ClientSession.get", return_value=resp)
        members = await api.fetch()
        assert len(members) == 2
        assert members[0].name == "David"
        assert members[0].bio == "I am an engineer"
        assert members[1].name == "Fred"
        assert members[1].bio == "I am a designer"


class TestJobApi:
    @pytest.mark.asyncio
    async def test_fetch(self, mocker):
        api = JobApi()
        data = [
            {
                "title": "Software Developer",
                "location": "Bristol",
            },
            {
                "title": "Visual Designer",
                "location": "Glasgow",
            },
        ]
        resp = MockResponse(data)
        mocker.patch("aiohttp.ClientSession.get", return_value=resp)
        jobs = await api.fetch()
        assert len(jobs) == 2
        assert jobs[0].title == "Software Developer"
        assert jobs[0].location == "Bristol"
        assert jobs[1].title == "Visual Designer"
        assert jobs[1].location == "Glasgow"
