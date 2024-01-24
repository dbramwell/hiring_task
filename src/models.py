from pydantic import BaseModel


class Member(BaseModel):
    name: str
    bio: str


class Job(BaseModel):
    title: str
    location: str
