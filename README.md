# Bright Network Hiring Challenge

Enjoyed this!

## Usage
You need to have docker and docker compose installed.

To build the container:
```
docker compose build
```

To run the tests:
```
docker compose run --rm app pytest
```

By default the program outputs each member and all jobs sorted according to their relevance, with the most relevant at the top:
```
docker compose run --rm app python main.py

```

You can limit to the top n results using `-n`, for example to get the top 2 results for each member:
```
docker compose run --rm app python main.py -n 2
```

You can also exlude any jobs in a location that does not appear in a member's bio:
```
docker compose run --rm app python main.py -n 2 --filter_on_location
```

## Approach

In reality it'd be better to do this matching based on key values. Let members set a list of Job Titles that they are interested in and Locations that they would like to work. I wanted my solution to scale to bios, titles and locations that aren't included in the sample data.

### Finding jobs with relevant titles
Looking at the data it immediately becomes apparent that you can't just do `if title in bio`, otherwise members for example "looking for a design job" wouldn't be given the "UX Designer" job. Potentially there's a very clever solution out there using machine learning and natural language processing. With two hours I opted for fuzzy string matching and a library called "thefuzz" and from [this blog post](https://chairnerd.seatgeek.com/fuzzywuzzy-fuzzy-string-matching-in-python/) the `token_set_ratio` function seemed the best fit. This gave me a score as to how well a job title matched a member's bio. There are of course issues with this, someone with "I have developed a range of skills" might end up being recommended "developer" jobs because of the word "developed".

### Finding jobs in the correct location
Fuzzy matching doesn't apply here, as location names don't have various forms, people looking for jobs in Norwich don't want to be recommended jobs in Northwich. Searching `location in bio` is the approach I've used, adding a `10` weighting to the score gained from the fuzzy title match if a jobs location is in a member's bio. I haven't tackled the issue of people stating they are not open to work in a certain place, a list of regularly used phrases could be used for this, or maybe again some sort of NLP. I've added an option to specifically exclude jobs where the location does not appear in a member's bio, this has the effect of recommending Hassan for zero jobs because he doesn't have a location in his bio, would need to know business requirements in order to understand if that is a good thing or not.

## Assumptions
* The api will always work. I haven't built in any retry logic, etc.
* I will always get strings from the API. I'm using pydantic for simple validation and throwing exceptions when not receiving strings. I could call str() ony everything that I'm passing to the Member and Job classes, but that may produce incorrect results and hide other issues in whatever system this code will run in.

## Improvements
* Missing tests for the main entrypoint file due to running out of time. These could be added.
* Using a tool like factoryboy to ease creating the test data.
* Adding a further commit hook to sort and remove duplicate dependencies.
* Allow specifying custom urls for the apis via env vars or cli arguments.