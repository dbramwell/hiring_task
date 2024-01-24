import asyncio
import getopt
import sys
from src.api import MemberApi, JobApi


def format_output(member, sorted_jobs):
    jobs_string = "\n  ".join([str(j) for j in sorted_jobs])
    return f"{member}:\n  {jobs_string}"


async def main(
    limit_number_of_results: int | None = None, filter_on_location: bool = False
):
    members, jobs = await asyncio.gather(MemberApi().fetch(), JobApi().fetch())
    for member in members:
        relevant_jobs = member.sort_jobs_by_relevance(jobs, filter_on_location)[
            :limit_number_of_results
        ]
        output = format_output(member, relevant_jobs)
        print(output)


limit_number_of_results = None
filter_on_location = False

opts, args = getopt.getopt(sys.argv[1:], "n:", ["filter_on_location"])

for opt, arg in opts:
    if opt == "-n":
        try:
            limit_number_of_results = int(arg)
        except Exception:
            pass
    if opt == "--filter_on_location":
        filter_on_location = True

asyncio.run(main(limit_number_of_results, filter_on_location))
