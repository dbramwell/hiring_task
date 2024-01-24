from pydantic import BaseModel
from thefuzz import fuzz
from typing import List


class Job(BaseModel):
    title: str
    location: str


class Member(BaseModel):
    name: str
    bio: str

    def sort_jobs_by_relevance(self, jobs: List[Job]) -> List[Job]:
        def key(job: Job) -> int:
            title_score = fuzz.token_sort_ratio(self.bio, job.title)
            location_score = 10 if job.location in self.bio else 0
            return title_score + location_score

        return sorted(jobs, key=key, reverse=True)
