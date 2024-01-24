import asyncio
import sys
from src.api import MemberApi, JobApi


def format_output(member, sorted_jobs):
    jobs_string = "\n  ".join([str(j) for j in sorted_jobs])
    return f"{member}:\n  {jobs_string}"


async def main(number_of_results: int | None = None):
    members, jobs = await asyncio.gather(MemberApi().fetch(), JobApi().fetch())
    for member in members:
        relevant_jobs = member.sort_jobs_by_relevance(jobs)[:number_of_results]
        output = format_output(member, relevant_jobs)
        print(output)


try:
    number_of_results = int(sys.argv[1])
    asyncio.run(main(number_of_results))
except Exception:
    asyncio.run(main())
