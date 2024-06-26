# LinkedIn Job Scraper

This Python script utilizes the ScrapingDog web API to scrape job listings from LinkedIn. It extracts relevant data such as job title, employment type, job description, company name, company logo (if available), and apply URL. Additionally, it decodes the apply URL to its original format.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/linkedin-job-scraper.git
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Sign up for a free account on ScrapingDog to obtain your API key.
2. Replace `'YOUR_API_KEY'` in `config.py` with your actual API key.
3. Run the scraper script:

```bash
python scraper.py
```

## Parameters

The scraper is designed with parameter flexibility to facilitate future adjustments. You can modify the parameters in `config.py` according to your requirements.

- `SEARCH_QUERY`: Specify the search query for job listings (e.g., "Python Developer").
- `LOCATION`: Specify the location for job search (e.g., "New York").
- `MAX_RESULTS`: Specify the maximum number of job listings to scrape.
- `SCRAPE_COMPANY_LOGO`: Set to `True` to scrape company logos (if available).
- `DECODE_APPLY_URL`: Set to `True` to decode apply URLs to their original format.

## Output

The scraper outputs the extracted job data in JSON format. Each job listing is represented as a dictionary with the following fields:

- `job_title`
- `employment_type`
- `job_description`
- `company_name`
- `company_logo_url`
- `apply_url`

## Example

Here's an example of a scraped jobs overview(In my code we can add job_id in this dict as well):

```json
[
    {
        "job_position": "Business Analyst",
        "job_location": "Las Vegas, NV",
        "company_name": "SearchPros",
        "company_linkedin_id": "https://www.linkedin.com/company/searchpros?trk=public_jobs_topcard-org-name",
        "job_posting_time": "1 week ago",
        "job_description": "Job Description:  Hybrid Role Oversee, develop, coordinate and administer internal training programs for Vacation Ownership Services division employees.Translate business requirements into system definitions and solutions.Resolve system problems to ensure customer processes run smoothly.Document business processes, training procedures, standard operation procedures and project status, among others.Identify training needs, standardize training initiatives, and track and report on training success.Sets a positive example to others relative to professionalism and the respect of others in order to contribute to a positive tone in the workplace. Gathers information and data on business process and procedures. Receives/identifies problem or process issues and inefficiencies, researches alternatives, contributes to presentations, tests to confirm, and participates in implementing solutions for defined business processes. Works with business partners to create documentation of business processes, training procedures, and standard operating procedures. Generates/monitors standard reports.Reviews and audits information. Assists in coordinating, conducting or facilitating general and specific training programs for organization employees. Assists in preparing training plans relevant to the material. Keeps records and gathers information from course evaluations. May suggest improvements. Delivers established training courses. Provides orientation and onboarding training to new division employees. May travel to other locations to assess needs, deliver trainings and/or perform other business needs. Performs after-hours/weekend testing of system enhancements and fixes. This could be within the division or in conjunction with other First American groups (both onshore and offshore). Monitors the shared email inbox to assist system users with inquiries, requests and/or issues. Gathers information on business objectives from management, determines training needs, and recommends solutions. Actively participates in the design of training/instructional materials including web publications, policy and procedure manuals and client-specific guidelines.Preferred Skills/Qualities Ability to interview, formulate questions Data management skills Has basic knowledge of general business environment/operation and has general cost benefit awareness. Good written and verbal communication skills in order to define parameters to meet business requirements. Standard MS skill set. 1-3 years of directly related experience.Education Must have high school diploma or equivalent Bachelor's degree is highly desirableAbility to pass Background and Drug Screen if Required by Client",
        "Seniority_level": "Entry level",
        "Employment_type": "Contract",
        "Job_function": "Research, Analyst, and Information Technology",
        "Industries": "Staffing and Recruiting",
        "job_apply_link": "https://www.linkedin.com/jobs/view/externalApply/3736845912?url=https%3A%2F%2Fwww2%2Ejobdiva%2Ecom%2Fcandidates%2Fmyjobs%2Fopenjob_outside%2Ejsp%3Fa%3D04jdnwosaaffea78rl6drxhhqb3k080140drna677bz98tp2yi32t4r6x5eeggv3%26SearchString%3D%26StatesString%3D%26source%3Dlinkedin%2Ecom%26id%3D20663268%26compid%3D-1&urlHash=u4lS&trk=public_jobs_apply-link-offsite_sign-up-modal-sign-up-later",
        "recruiter_details": [
            {
                "recruiter_name": "",
                "recruiter_title": ""
            }
        ],
        "similar_jobs": [
            {
                "job_position": "Analyst, Business Strategy & Analytics",
                "job_company": "Chicago Bulls",
                "job_location": "Chicago, IL",
                "job_posting_time": "3 weeks ago",
                "job_link": "https://www.linkedin.com/jobs/view/analyst-business-strategy-analytics-at-chicago-bulls-3728824359?refId=rZgaPZkt%2FOI9cCPgc0Ku1A%3D%3D&trackingId=j5XENyJrK2iAF6jt3v82bQ%3D%3D&trk=public_jobs_similar-jobs"
            },
            {
                "job_position": "Business Operations Analyst",
                "job_company": "Madison Ave Consulting",
                "job_location": "United States",
                "job_posting_time": "1 month ago",
                "job_link": "https://www.linkedin.com/jobs/view/business-operations-analyst-at-madison-ave-consulting-3727448286?refId=rZgaPZkt%2FOI9cCPgc0Ku1A%3D%3D&trackingId=fP914iA3EH8HVQKZT3cz9A%3D%3D&trk=public_jobs_similar-jobs"
            },
            {
                "job_position": "Business Strategy Analyst",
                "job_company": "ESG Consulting",
                "job_location": "Atlanta Metropolitan Area",
                "job_posting_time": "1 week ago",
                "job_link": "https://www.linkedin.com/jobs/view/business-strategy-analyst-at-esg-consulting-3708948901?refId=rZgaPZkt%2FOI9cCPgc0Ku1A%3D%3D&trackingId=lCwk29%2FoGqGh6UR4E8iLcw%3D%3D&trk=public_jobs_similar-jobs"
            },
            {
                "job_position": "Business Operations & Strategy Analyst (Remote)",
                "job_company": "Kepro",
                "job_location": "Harrisburg, PA",
                "job_posting_time": "2 weeks ago",
                "job_link": "https://www.linkedin.com/jobs/view/business-operations-strategy-analyst-remote-at-kepro-3736466130?refId=rZgaPZkt%2FOI9cCPgc0Ku1A%3D%3D&trackingId=GKxYfYleW%2FOcaVslFSJS6g%3D%3D&trk=public_jobs_similar-jobs"
            },
            {
                "job_position": "Business Analyst -local",
                "job_company": "Steneral Consulting",
                "job_location": "Richmond, VA",
                "job_posting_time": "2 months ago",
                "job_link": "https://www.linkedin.com/jobs/view/business-analyst%C2%A0-local-at-steneral-consulting-3677422856?refId=rZgaPZkt%2FOI9cCPgc0Ku1A%3D%3D&trackingId=7K6FP8IrkNFtFYmXD49aAA%3D%3D&trk=public_jobs_similar-jobs"
            },
            {
                "job_position": "Sr Business Analyst",
                "job_company": "HN Consulting LLC",
                "job_location": "Arlington, VA",
                "job_posting_time": "2 hours ago",
                "job_link": "https://www.linkedin.com/jobs/view/sr-business-analyst-at-hn-consulting-llc-3747602004?refId=rZgaPZkt%2FOI9cCPgc0Ku1A%3D%3D&trackingId=f8yrE3RFFNQgOXWTx0uolw%3D%3D&trk=public_jobs_similar-jobs"
            },
            {
                "job_position": "Hybrid Work - Need  Sr. Business Analyst in Deerfield Beach FL",
                "job_company": "Steneral Consulting",
                "job_location": "Deerfield Beach, FL",
                "job_posting_time": "3 months ago",
                "job_link": "https://www.linkedin.com/jobs/view/hybrid-work-need-sr-business-analyst-in-deerfield-beach-fl-at-steneral-consulting-3665625679?refId=rZgaPZkt%2FOI9cCPgc0Ku1A%3D%3D&trackingId=gaDca%2BCUsS7M79%2BjkUUOAw%3D%3D&trk=public_jobs_similar-jobs"
            },
            {
                "job_position": "Sr Business Analyst",
                "job_company": "HN Consulting LLC",
                "job_location": "Arlington, VA",
                "job_posting_time": "3 weeks ago",
                "job_link": "https://www.linkedin.com/jobs/view/sr-business-analyst-at-hn-consulting-llc-3732134759?refId=rZgaPZkt%2FOI9cCPgc0Ku1A%3D%3D&trackingId=jZie3n0eV%2F4wrXwJBHSMDA%3D%3D&trk=public_jobs_similar-jobs"
            },
            {
                "job_position": "Business Analyst Rotation Program - Atlanta, GA",
                "job_company": "CarMax",
                "job_location": "Kennesaw, GA",
                "job_posting_time": "1 month ago",
                "job_link": "https://www.linkedin.com/jobs/view/business-analyst-rotation-program-atlanta-ga-at-carmax-3714790898?refId=rZgaPZkt%2FOI9cCPgc0Ku1A%3D%3D&trackingId=11L53LeBmyFJehQbXw1bUw%3D%3D&trk=public_jobs_similar-jobs"
            },
            {
                "job_position": ": Sr. Business Analyst",
                "job_company": "Steneral Consulting",
                "job_location": "Deerfield Beach, FL",
                "job_posting_time": "3 months ago",
                "job_link": "https://www.linkedin.com/jobs/view/sr-business-analyst-at-steneral-consulting-3660525355?refId=rZgaPZkt%2FOI9cCPgc0Ku1A%3D%3D&trackingId=2yq09JSLiLdG31HCjv6CTg%3D%3D&trk=public_jobs_similar-jobs"
            },
            {
                "job_position": "Business Analyst",
                "job_company": "TekIntegral",
                "job_location": "Richmond, VA",
                "job_posting_time": "3 months ago",
                "job_link": "https://www.linkedin.com/jobs/view/business-analyst-at-tekintegral-3644948083?refId=rZgaPZkt%2FOI9cCPgc0Ku1A%3D%3D&trackingId=ApB9IlcdnmJ31vIYLPl81w%3D%3D&trk=public_jobs_similar-jobs"
            },
            {
                "job_position": "Senior Business Analyst",
                "job_company": "Photon",
                "job_location": "Irving, TX",
                "job_posting_time": "5 months ago",
                "job_link": "https://www.linkedin.com/jobs/view/senior-business-analyst-at-photon-3597851384?refId=rZgaPZkt%2FOI9cCPgc0Ku1A%3D%3D&trackingId=lf1rL7OaiCNYU9kjk%2FiXGg%3D%3D&trk=public_jobs_similar-jobs"
            },
            {
                "job_position": "Specialist, Business Capability Product Analyst (AWD Technologies))",
                "job_company": "Nationwide",
                "job_location": "Ohio, United States",
                "job_posting_time": "4 days ago",
                "job_link": "https://www.linkedin.com/jobs/view/specialist-business-capability-product-analyst-awd-technologies-at-nationwide-3744443945?refId=rZgaPZkt%2FOI9cCPgc0Ku1A%3D%3D&trackingId=sLGcB%2F%2BVaLF00P%2Fz%2FGV4qQ%3D%3D&trk=public_jobs_similar-jobs"
            },
            {
                "job_position": "Business Process Analyst",
                "job_company": "The Rockridge Group",
                "job_location": "Fairfield, NJ",
                "job_posting_time": "9 hours ago",
                "job_link": "https://www.linkedin.com/jobs/view/business-process-analyst-at-the-rockridge-group-3745185962?refId=rZgaPZkt%2FOI9cCPgc0Ku1A%3D%3D&trackingId=KsmtJ7YJtWUEKR1su4ojhg%3D%3D&trk=public_jobs_similar-jobs"
            },
            {
                "job_position": "Amazon - Strategy Analyst",
                "job_company": "O Positiv",
                "job_location": "Santa Monica, CA",
                "job_posting_time": "3 weeks ago",
                "job_link": "https://www.linkedin.com/jobs/view/amazon-strategy-analyst-at-o-positiv-3707563342?refId=rZgaPZkt%2FOI9cCPgc0Ku1A%3D%3D&trackingId=OL4AROsaMMMbRHn%2F9Gl%2Fww%3D%3D&trk=public_jobs_similar-jobs"
            },
            {
                "job_position": "Analyst, Business Process",
                "job_company": "Ocean Network Express",
                "job_location": "Richmond, VA",
                "job_posting_time": "2 weeks ago",
                "job_link": "https://www.linkedin.com/jobs/view/analyst-business-process-at-ocean-network-express-3734163618?refId=rZgaPZkt%2FOI9cCPgc0Ku1A%3D%3D&trackingId=TVMpGjsvZsUXkUJgKaNW%2Bg%3D%3D&trk=public_jobs_similar-jobs"
            },
            {
                "job_position": "Business Analyst Sr",
                "job_company": "NextRow Digital",
                "job_location": "Hartford, CT",
                "job_posting_time": "3 months ago",
                "job_link": "https://www.linkedin.com/jobs/view/business-analyst-sr-at-nextrow-digital-3651380316?refId=rZgaPZkt%2FOI9cCPgc0Ku1A%3D%3D&trackingId=ZhtO5vpnTZzSS2hFIk8nUg%3D%3D&trk=public_jobs_similar-jobs"
            },
            {
                "job_position": "Business Analyst",
                "job_company": "Artius Solutions",
                "job_location": "Minneapolis, MN",
                "job_posting_time": "6 months ago",
                "job_link": "https://www.linkedin.com/jobs/view/business-analyst-at-artius-solutions-3584717957?refId=rZgaPZkt%2FOI9cCPgc0Ku1A%3D%3D&trackingId=KofJHUgN1xzfTcVl9VTlIw%3D%3D&trk=public_jobs_similar-jobs"
            },
            {
                "job_position": "Data Business Analyst, Senior",
                "job_company": "Varis",
                "job_location": "Boca Raton, FL",
                "job_posting_time": "1 week ago",
                "job_link": "https://www.linkedin.com/jobs/view/data-business-analyst-senior-at-varis-3735387363?refId=rZgaPZkt%2FOI9cCPgc0Ku1A%3D%3D&trackingId=8Ienf8%2F494VnRHi8%2FP15xg%3D%3D&trk=public_jobs_similar-jobs"
            },
            {
                "job_position": "Job Opening for Business Analyst - Richmond, VA",
                "job_company": "Steneral Consulting",
                "job_location": "Richmond, VA",
                "job_posting_time": "3 months ago",
                "job_link": "https://www.linkedin.com/jobs/view/job-opening-for-business-analyst-richmond-va-at-steneral-consulting-3666778539?refId=rZgaPZkt%2FOI9cCPgc0Ku1A%3D%3D&trackingId=eGwe6pYi90M2HFtm3h4uwA%3D%3D&trk=public_jobs_similar-jobs"
            },
            {
                "job_position": "Strategy Analyst",
                "job_company": "Shutterfly",
                "job_location": "Eden Prairie, MN",
                "job_posting_time": "1 month ago",
                "job_link": "https://www.linkedin.com/jobs/view/strategy-analyst-at-shutterfly-3725134591?refId=rZgaPZkt%2FOI9cCPgc0Ku1A%3D%3D&trackingId=43xwgans%2BtWnxs8ThJPK%2FQ%3D%3D&trk=public_jobs_similar-jobs"
            },
            {
                "job_position": "Client Strategy Analyst",
                "job_company": "Convergence Media",
                "job_location": "Alexandria, VA",
                "job_posting_time": "1 month ago",
                "job_link": "https://www.linkedin.com/jobs/view/client-strategy-analyst-at-convergence-media-3700056328?refId=rZgaPZkt%2FOI9cCPgc0Ku1A%3D%3D&trackingId=2LJR8nirq3PNwQhJwzwxwQ%3D%3D&trk=public_jobs_similar-jobs"
            },
            {
                "job_position": "Business Analyst - Full-Time (January & 2024 Start)",
                "job_company": "Wayfair",
                "job_location": "Boston, MA",
                "job_posting_time": "1 month ago",
                "job_link": "https://www.linkedin.com/jobs/view/business-analyst-full-time-january-2024-start-at-wayfair-3705960532?refId=rZgaPZkt%2FOI9cCPgc0Ku1A%3D%3D&trackingId=Smh4oL0xJMK08Zl5kjj46g%3D%3D&trk=public_jobs_similar-jobs"
            },
            {
                "job_position": "Sr Business Analyst with \"data Analysis\" (10 Years + only )",
                "job_company": "Extend Information Systems Inc.",
                "job_location": "Erie, PA",
                "job_posting_time": "1 week ago",
                "job_link": "https://www.linkedin.com/jobs/view/sr-business-analyst-with-data-analysis-10-years-%2B-only-at-extend-information-systems-inc-3740263858?refId=rZgaPZkt%2FOI9cCPgc0Ku1A%3D%3D&trackingId=yuzZJ3MRkPmC%2BUXR%2BsRYGQ%3D%3D&trk=public_jobs_similar-jobs"
            },
            {
                "job_position": "Lead Business Strategy Analyst",
                "job_company": "Millennium Group",
                "job_location": "San Antonio, TX",
                "job_posting_time": "3 weeks ago",
                "job_link": "https://www.linkedin.com/jobs/view/lead-business-strategy-analyst-at-millennium-group-3726776379?refId=rZgaPZkt%2FOI9cCPgc0Ku1A%3D%3D&trackingId=jH0HcDJ2nfLPWPIN71W7Eg%3D%3D&trk=public_jobs_similar-jobs"
            },
            {
                "job_position": "Hybrid Work - Need Business Data Analyst in Durant OK",
                "job_company": "Steneral Consulting",
                "job_location": "Durant, OK",
                "job_posting_time": "2 weeks ago",
                "job_link": "https://www.linkedin.com/jobs/view/hybrid-work-need-business-data-analyst-in-durant-ok-at-steneral-consulting-3734703522?refId=rZgaPZkt%2FOI9cCPgc0Ku1A%3D%3D&trackingId=z8wofUO0dOZmSftuqapcww%3D%3D&trk=public_jobs_similar-jobs"
            },
            {
                "job_position": "urgent requirement :: Business Data Analyst :: Contract :: Charlotte, NC (Hybrid).",
                "job_company": "Apptad Inc.",
                "job_location": "Charlotte, NC",
                "job_posting_time": "6 days ago",
                "job_link": "https://www.linkedin.com/jobs/view/urgent-requirement-business-data-analyst-contract-charlotte-nc-hybrid-at-apptad-inc-3741164608?refId=rZgaPZkt%2FOI9cCPgc0Ku1A%3D%3D&trackingId=5jRbhoCa4pHfnTrYmBwKCg%3D%3D&trk=public_jobs_similar-jobs"
            }
        ],
        "people_also_viewed": [
            {
                "job_position": "Business Strategy Analyst",
                "job_company": "Pace Center for Girls",
                "job_location": "Jacksonville, FL",
                "job_posting_time": "1 week ago",
                "job_link": "https://www.linkedin.com/jobs/view/business-strategy-analyst-at-pace-center-for-girls-3737814929?refId=rZgaPZkt%2FOI9cCPgc0Ku1A%3D%3D&trackingId=vwRqIUOsEaBC5hMUy6ULKw%3D%3D&trk=public_jobs_people-also-viewed"
            },
            {
                "job_position": "Business Analysis/Reengineering Senior",
                "job_company": "KYYBA Inc",
                "job_location": "Dearborn, MI",
                "job_posting_time": "1 month ago",
                "job_link": "https://www.linkedin.com/jobs/view/business-analysis-reengineering-senior-at-kyyba-inc-3711689178?refId=rZgaPZkt%2FOI9cCPgc0Ku1A%3D%3D&trackingId=xMSXZFAq%2FGa0juJjLpYRgw%3D%3D&trk=public_jobs_people-also-viewed"
            },
            {
                "job_position": "Business Analyst",
                "job_company": "Cynet Systems",
                "job_location": "Richmond, VA",
                "job_posting_time": "2 months ago",
                "job_link": "https://www.linkedin.com/jobs/view/business-analyst-at-cynet-systems-3673309704?refId=rZgaPZkt%2FOI9cCPgc0Ku1A%3D%3D&trackingId=fBAHzI8Qytcc5NjcU7aoNg%3D%3D&trk=public_jobs_people-also-viewed"
            },
            {
                "job_position": "Corporate Strategy Analyst",
                "job_company": "NinjaTrader",
                "job_location": "Chicago, IL",
                "job_posting_time": "2 months ago",
                "job_link": "https://www.linkedin.com/jobs/view/corporate-strategy-analyst-at-ninjatrader-3717902475?refId=rZgaPZkt%2FOI9cCPgc0Ku1A%3D%3D&trackingId=l21zry3JMsxoL0L6zSbM1w%3D%3D&trk=public_jobs_people-also-viewed"
            },
            {
                "job_position": "Business Analyst",
                "job_company": "Bristol Myers Squibb",
                "job_location": "Princeton, NJ",
                "job_posting_time": "2 months ago",
                "job_link": "https://www.linkedin.com/jobs/view/business-analyst-at-bristol-myers-squibb-3689293562?refId=rZgaPZkt%2FOI9cCPgc0Ku1A%3D%3D&trackingId=pCCkAcC88G0LlpvP0x9bjQ%3D%3D&trk=public_jobs_people-also-viewed"
            },
            {
                "job_position": "Senior Business and Strategy Analyst - Remote US",
                "job_company": "Holland America Line",
                "job_location": "Seattle, WA",
                "job_posting_time": "1 week ago",
                "job_link": "https://www.linkedin.com/jobs/view/senior-business-and-strategy-analyst-remote-us-at-holland-america-line-3743424799?refId=rZgaPZkt%2FOI9cCPgc0Ku1A%3D%3D&trackingId=z7mPuAtgfjGkIh40Of7KkQ%3D%3D&trk=public_jobs_people-also-viewed"
            },
            {
                "job_position": "Senior Business Analyst",
                "job_company": "KYYBA Inc",
                "job_location": "Albany, NY",
                "job_posting_time": "5 months ago",
                "job_link": "https://www.linkedin.com/jobs/view/senior-business-analyst-at-kyyba-inc-3622570449?refId=rZgaPZkt%2FOI9cCPgc0Ku1A%3D%3D&trackingId=qjYK0CHlTgvzqBDiuilckQ%3D%3D&trk=public_jobs_people-also-viewed"
            },
            {
                "job_position": "ODGA - Business Analyst 4",
                "job_company": "NextRow Digital",
                "job_location": "Richmond, VA",
                "job_posting_time": "3 months ago",
                "job_link": "https://www.linkedin.com/jobs/view/odga-business-analyst-4-at-nextrow-digital-3644952386?refId=rZgaPZkt%2FOI9cCPgc0Ku1A%3D%3D&trackingId=aZdJM5WMGtKDVkzz%2FPtmbQ%3D%3D&trk=public_jobs_people-also-viewed"
            },
            {
                "job_position": "Business Analyst",
                "job_company": "HonorVet Technologies",
                "job_location": "Lawrenceville, NJ",
                "job_posting_time": "3 weeks ago",
                "job_link": "https://www.linkedin.com/jobs/view/business-analyst-at-honorvet-technologies-3726775416?refId=rZgaPZkt%2FOI9cCPgc0Ku1A%3D%3D&trackingId=Q5iKTdvDI81Jcqu%2BiNE50Q%3D%3D&trk=public_jobs_people-also-viewed"
            },
            {
                "job_position": "DBHDS - Business Analyst 4 - Enterprise Data Warehouse Project",
                "job_company": "NextRow Digital",
                "job_location": "Richmond, VA",
                "job_posting_time": "3 months ago",
                "job_link": "https://www.linkedin.com/jobs/view/dbhds-business-analyst-4-enterprise-data-warehouse-project-at-nextrow-digital-3651370823?refId=rZgaPZkt%2FOI9cCPgc0Ku1A%3D%3D&trackingId=%2B%2FRB%2Bi9rzacqqcYyWVXucQ%3D%3D&trk=public_jobs_people-also-viewed"
            }
        ]
    }
]
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to customize the README according to your project's specifics and add any additional sections or information as needed!
