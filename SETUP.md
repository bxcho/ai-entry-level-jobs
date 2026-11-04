# Is AI eating entry-level jobs?

This project takes a weekly snapshot of job postings at about 45 companies. It measures how many openings are entry-level and how many entry-level postings ask for AI skills, by job function.

Everything runs on GitHub. You do not install anything on your computer.

## What it measures

1. The entry-level share of all open jobs, by function.
2. The share of entry-level postings that ask the candidate to have or use AI skills. The results split this into "use AI tools" (for example ChatGPT or Copilot) and "build AI" (for example PyTorch or LLM fine-tuning).
3. How both numbers change from week to week.

## What it cannot tell you

- It measures what postings ask for. It does not show that AI replaced anyone.
- It covers only companies that post jobs on Greenhouse, Lever, or Ashby, which are mostly tech companies. Big 4 firms and most banks use Workday, which has no public API. The results describe these employers, not the whole job market.
- The labels come from keyword rules. The validation step measures how often the rules agree with a person.
- The project stores the text of entry-level jobs and internships only. If you change the rules later, it cannot re-check jobs that it labeled "other" when it collected them.

## Set up (about 30 minutes, all in the browser)

1. On GitHub, create a **private** repository named `ai-entry-jobs`. A private repository keeps the companies' posting text off the public web. Free accounts get 2,000 Actions minutes per month for private repositories, and one run takes a few minutes.
2. Click **Add file → Upload files**. Drag in every file and folder from this project. The Mac Finder hides the `.github` folder, so step 3 adds that file.
3. Click **Add file → Create new file**. Type the name `.github/workflows/pipeline.yml`. Paste the contents of `pipeline.yml` and click **Commit**.
4. Open **Settings → Secrets and variables → Actions → Variables** and click **New repository variable**. Name it `CONTACT_EMAIL` and enter your email address. The script sends it with each request so the API owners can contact you.
5. Open the **Actions** tab, click **pipeline**, then **Run workflow**. Choose the task `collect` and click **Run workflow**. The run takes 3–5 minutes.
6. Open the finished run and read the **Summary**. It shows how many companies worked and lists the rows to fix.
7. Fix `companies.csv` on GitHub (click the pencil icon). For each "not found" row, open the company's careers page, click any job, and copy the token from the address:
   - `job-boards.greenhouse.io/TOKEN` or `boards.greenhouse.io/TOKEN` → `greenhouse`
   - `jobs.lever.co/TOKEN` → `lever`
   - `jobs.ashbyhq.com/TOKEN` → `ashby`

   Delete any company that uses a different system. Then run `collect` again. A second run on the same day replaces that day's data.

After setup, the workflow runs by itself every Monday. Check the Actions tab every two weeks to make sure the runs still succeed.

## Validate the rules (about 2 hours, once)

Do this after your first good snapshot.

1. Run the workflow with the task `sample`. It writes `labels/to_label.csv` with 80 postings.
2. Open that file on GitHub, click **Download raw file**, and import it into Google Sheets.
3. Fill in three columns for each row. Read `posting_text` and open `url` if you need more context. The file hides the rules' answers on purpose, so your labels stay independent.
   - `human_ai_skill`: `yes` or `no`. Does the posting ask the candidate to have or use AI skills? Company boilerplate such as "we are an AI company" counts as `no`.
   - `human_function`: one of the function names below.
   - `human_level`: `entry`, `intern`, or `other`.
4. In Google Sheets, click **File → Download → CSV**. Upload the file to the repository as `labels/labeled.csv`.
5. Run the workflow with the task `score`. Read `results/validation.md`. Its list of disagreements shows which words to add to or remove from `classify.py`.

Function names: `software_eng`, `data_ml`, `hardware_eng`, `product_design`, `sales_marketing`, `finance_accounting`, `hr_people`, `legal_policy`, `consulting_strategy_ops`, `other`.

## Get results

Run the workflow with the task `analyze`. It writes `results/summary.md` and two charts. The function breakdown works after the first snapshot. The weekly trend needs about six snapshots.

## Change the rules

All rules are word lists in `classify.py`. Edit them on GitHub, then run the workflow with the task `test` to check that nothing broke. The `analyze` and `score` tasks re-apply the current rules to the stored text.

## Files

| File | What it does |
|---|---|
| `companies.csv` | The companies to track |
| `sources.py` | Calls the Greenhouse, Lever, and Ashby APIs |
| `classify.py` | Labels level, function, and AI requirement |
| `collect.py` | Takes one snapshot and saves it to `data/` |
| `label.py` | Makes the blind labeling sheet and scores it |
| `analyze.py` | Writes `results/summary.md` and charts |
| `pipeline.yml` | Schedules the weekly run (goes in `.github/workflows/`) |
| `tests/` | Checks for the rules |

## Notes

- All three APIs are public and need no key. The script waits one second between companies.
- One job posted in several cities counts once.
- To show this project publicly when you finish, make a new public repository with the code and the `results/` folder. Leave out `data/`, because it holds the companies' posting text.
