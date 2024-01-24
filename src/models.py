from pydantic import BaseModel
from thefuzz import fuzz
from typing import List


class Job(BaseModel):
    title: str
    location: str

    def __str__(self) -> str:
        return f"{self.title} - {self.location}"


class Member(BaseModel):
    name: str
    bio: str

    def __str__(self) -> str:
        return self.name

    def sort_jobs_by_relevance(
        self, jobs: List[Job], filter_on_location: bool = False
    ) -> List[Job]:
        def key(job: Job) -> int:
            title_score = fuzz.token_sort_ratio(self.bio, job.title)
            location_score = 10 if job.location in self.bio else 0
            return title_score + location_score

        if filter_on_location:
            jobs = filter(lambda j: j.location in self.bio, jobs)

        return sorted(jobs, key=key, reverse=True)
