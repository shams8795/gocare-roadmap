# Review Notes

Review of the four GoCare reports (21 Nov 2026): the endpoint testing sheet, the integration status, the AI agent roadmap, and the website and product improvements.

## Scorecard

| Task | Verdict | What's missing |
|---|---|---|
| 1. Feature integration status | **Mostly done** | A summary, the environment and version tested, and evidence behind "correct result". Some rows contradict each other (now fixed on the [Integration Status](integration-status.md) page). |
| 2. Pending integration | **Partial** | Current status, remaining work, owner and estimate for each pending item. Owner and Target date columns are now in the workbook. |
| 3. AI agent roadmap | **Half done** | Consolidating and prioritising are done well. Missing: the immediate vs blocked split, and blockers with resolutions agreed with Farah. Now drafted in the [Action Plan](action-plan.md). |
| 4. Website & product improvements | **Partial** | The admin panel part ([Team Requests](team-requests.md)) is strong. There is no website review with Farah and no customer-experience proposals. |

## What's good

- **The feature pages are good requirements work.** Each one follows the same template: problem, example, functional and non-functional requirements, data needs, MVP scope, open questions, risks. The data tables say which data is confirmed and which isn't, which is what you need before committing to a feature.
- **Team Requests is the most useful page.** It has concrete numbers (65% of descriptions pass the audit), root causes (5 missing fields, no Shade or Size field, no defaults) and separates backend work from AI work.
- The sheet is written so non-technical people can follow it, and the Arabic reading guide helps the client side.

## Bugs fixed in the endpoint sheet

All of these were checked against the code on the `dev` and `test` branches. The details are on [Integration Status](integration-status.md#changes-from-the-original-sheet).

| # | Problem in the original sheet | Fix |
|---|---|---|
| 13, 14 | Image Audit marked "endpoint doesn't exist". | The routes exist in v0.5.4. Watermark detection is behind a flag that is off by default. Marked **Built, not working in tested env** and **Built, off by default**. |
| 19 | Routine Safety marked as used on the website, but it runs inside Routine Maker, which is still in testing. | Marked **In testing**. It needs a safety test set before go-live. |
| 20 | Salon Queries marked "endpoint doesn't exist". | `POST /api/salon/queries` exists in v0.5.4. Marked **Built, not working in tested env**. |
| 21 | Voice marked "No", but its notes describe endpoints and a flag. | No voice code in any branch. Marked **Not built**. |
| 26 | Product Search marked "No / Not sure", while its notes call it a production route. | It exists since v1.4.0. Marked **Built, not working in tested env**, with a retest request. |
| 8 | Unclear whether knowledge-base delete is DELETE or POST. | Both exist as two separate endpoints (`DELETE /delete` and `POST /documents/delete`). |
| 22–25 | Both v1.8.0 and v2 routes listed, without saying which to use. | Integrate against `/api/v1`. The legacy routes already return deprecation warnings. |
| — | Rows #3, #4, #5 and #9 are missing. | Flagged. Confirm whether they were dropped or merged. |
| — | No environment or version recorded. | Release status by branch added. Production must be defined first (Action Plan 1.0). |

## Gaps in the roadmap

1. **The roadmap and the status sheet weren't linked.**
   - Skincare Routine Advisor overlaps with Routine Maker, which is already built.
   - Visual Search overlaps with Vision Analysis, which is already built.
   - Advanced Product Recommendations overlaps with the recommendation service.
   - Personalization Engine, Context Awareness and User Preferences each appear under both Agents and Recommendation System.
2. **The top-rated item is blocked.** Churn Prediction is rated 100%, but most of its data is "Unconfirmed" and it depends on the WhatsApp Business API. This is exactly what the immediate-vs-blocked split was meant to show.
3. **Dynamic Pricing is marked "completed, only testing remains".** The code is an unmerged command-line prototype with no API and no margin rules (see the [Action Plan](action-plan.md#track-3-clear-the-blockers-owners-and-dates-no-dev-time)).
4. **Effort is missing.** Only 4 of 21 agent pages state an effort level. No feature has an owner, an estimate or an order of work.
5. **Out-of-date heading:** "Long-term Vision (2026+)".

## Repo changes made in this review

- **The site now has a markdown source.** The original repo held only built HTML. The markdown in `docs/` was rebuilt from that HTML and checked to give the same text and page structure on all 53 pages. Edit pages in `docs/` and the site rebuilds on push.
- **New pages:** Action Plan, Integration Status, Review Notes.
- **Data files:** `docs/data/gocare-endpoints-review.xlsx` (Summary, Reviewed, Legend, Original), plus CSV copies, which GitHub shows as tables.
- **Hosting:** the repo should live on the company GitHub account (`Adwat`), not a personal account, because it holds client business details.
