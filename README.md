# LinkdIn-Job-Scrapper

Collects LinkedIn job listings through the [ScrapingDog](https://www.scrapingdog.com) LinkedIn Jobs API, decodes each job's real apply link and exports everything to CSV. Built for lead/market research on job postings (title, company, seniority, pay, description, apply URL …).

## What it does

1. Calls the ScrapingDog jobs endpoint with a search field (e.g. `python`), a LinkedIn `geoid` (location) and a page number, and reads back the list of job ids.
2. For every job id, calls the same endpoint again to fetch the full posting.
3. Decodes LinkedIn's redirect-style `job_apply_link` (`…externalApply/<id>?url=<encoded>…`) into the employer's original application URL.
4. Writes all jobs to `job_data.csv`, one row per job.

## Data captured

`job_position`, `job_location`, `company_name`, `company_linkedin_id`, `job_posting_time`, `base_pay`, `job_description`, `Seniority_level`, `Employment_type`, `Job_function`, `Industries`, `job_apply_link` (decoded) and `job_id`.

Example record (shortened):

```json
{
  "job_position": "Business Analyst",
  "job_location": "Las Vegas, NV",
  "company_name": "SearchPros",
  "job_posting_time": "1 week ago",
  "Seniority_level": "Entry level",
  "Employment_type": "Contract",
  "Job_function": "Research, Analyst, and Information Technology",
  "Industries": "Staffing and Recruiting",
  "job_apply_link": "https://www2.jobdiva.com/candidates/myjobs/openjob_outside.jsp?…",
  "job_id": "3736845912"
}
```

## Repository contents

| File | Purpose |
|---|---|
| `linkdin_job_scrapper.py` | **The scraper** — ids → details → decoded apply link → `job_data.csv` |
| `linkdin_profile_scrapper.py` | Small experiment with LinkedIn's *authwall* redirect (cookie parsing, http→https, `authwall?trk=…` URL building). It only prints the URL it would redirect to; it is not a full profile scraper. |
| `lindin_prof_scrapper.html` | Saved copy of the authwall page used while studying that redirect logic |
| `job_data.csv`, `job_ids.txt` | Sample output and sample ids from a run |
| `requirements.txt` | Python dependencies (`requests`) |

## How it works

```
ScrapingDog jobs API ──(field, geoid, page)──► [ {job_id, …}, … ]
        │
        └─ for each job_id ──► full job JSON ──► decode_url(job_apply_link)
                                                      │  urllib.parse.unquote, keep text after "url="
                                                      ▼
                                              job_data.csv (DictWriter, header + rows)
```

## Setup

```bash
git clone https://github.com/SanaAkram/LinkdIn-Job-Scrapper.git
cd LinkdIn-Job-Scrapper

python -m venv .venv
# Windows:      .venv\Scripts\activate
# macOS/Linux:  source .venv/bin/activate

pip install -r requirements.txt
```

1. Create a ScrapingDog account and copy your **API key**.
2. Open `linkdin_job_scrapper.py` and fill in the placeholders at the top:

   ```python
   api_key = "YOUR_SCRAPINGDOG_API_KEY"
   job_url = "<ScrapingDog LinkedIn Jobs API endpoint from their docs>"

   job_params = {
       "api_key": api_key,
       "field": "python",        # search keyword / job title
       "geoid": "100293800",     # LinkedIn location id
       "page": "1",              # results page
   }
   ```

> Never commit your real API key — load it from an environment variable or an untracked file if you share the code.

## Run

```bash
python linkdin_job_scrapper.py
```

Progress (job ids, decoded links, failures) is printed to the console and `job_data.csv` is written when the run finishes.

## Notes

- To scrape more, loop over the `page` parameter; to change the market, change `geoid`.
- Failed detail requests are reported and skipped, so one bad job does not stop the run.
- Follow ScrapingDog's and LinkedIn's terms of service and applicable data-protection rules.
