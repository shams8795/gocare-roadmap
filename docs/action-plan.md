# Action Plan

What to work on next, based on the [roadmap](final-decisions.md), the [Integration Status](integration-status.md) review and the [Team Requests](team-requests.md). Prepared 21 Nov 2026.

## How items were picked

The importance % in the roadmap measures **business impact only**. Each item here was also judged on two more questions:

- **Effort.** How much work it is, and whether it builds on code that already exists. These are estimates from the feature pages and the code, so check them with the team.
- **Readiness.** Whether anything blocks it: missing data, a decision, access to a third-party API.

**The rule:** start dev work on high-impact items that aren't blocked. For high-impact items that are blocked, give the blocker an owner and a date now, and don't spend dev hours on them yet.

## Track 1: Release what is already built (weeks 1–3)

Only internal catalog tools are live today. Releasing the chat and the recommendations is worth more than any new feature.

| # | Action | Why | Roadmap link |
|---|---|---|---|
| 1.0 | **Define what "production" is.** Agree which branch and environment production runs on, and set up the `dev` → `test` → `main` promotion. `main` is still v0.1 (agents) and v1.4.0 (recommendations). | Without this, "production release status" can't be measured. | — |
| 1.1 | **Take the chat live**: chat, cart, knowledge base, vision, dialects, Routine Maker. Write an acceptance test set first, including the Routine Safety cases (pregnancy, allergies, medication). | 7 endpoints are in testing. Routine Safety must not go live without signed-off tests. | — |
| 1.2 | **Check the frontend sends the full message history.** The server keeps the last 10 messages it receives and stores nothing itself. | If the frontend sends only the latest message, follow-up questions break. | Context Awareness (85%) |
| 1.3 | **Add thumbs up/down on chat replies.** | This is cheap, and it's the only way to know whether the chat works for real users. | Feedback Collection (80%) |
| 1.4 | **Connect the 4 recommendation endpoints to the frontend**, using the `/api/v1/...` routes. Add click and purchase tracking at the same time. | The backend works but the website doesn't call it. The meeting said recommendation conversions are the key numbers. | Analytics Dashboard (30%) needs this data later |
| 1.5 | **Retest the 3 "built, not working" endpoints** (image audit, salon queries, product search) on a known environment and version. | The code exists on `test` and `dev`, so this is likely a deployment gap, not missing work. | Visual Search (80%), Smart Salon (60%) depend on these |

## Track 2: Fix the catalog (runs alongside Track 1)

**Content Creation (100%)** and **Automated Content Tagging (90%)** are one workstream with the [Team Requests](team-requests.md). Better product data improves search, filters, recommendations, routines and visual search.

**AI team (`GoCare-Agents`: audit and enhance agents)**

- Make generated descriptions editable, and save the edits (Content Creation meeting decision).
- Apply the 5-section template in Description Enhancement: Key Benefits, Ingredients/Materials, How to Use, Specifications, Best Suited For.
- When supplier data is missing, the audit fills a default ("Not specified") and marks the product **needs info** instead of **failed**.
- Extend tagging to pull out shade, size, skin/hair type, vegan, cruelty-free, perfume notes and category, using the web search that already exists (`?search=true`).

**Backend and frontend team (admin panel)**

- Add Shade and Size fields.
- Group sizes of the same product as variants on one product page.
- Alert on duplicate product codes.
- Add bulk select and bulk edit.
- Fix the bug that turns Arabic words in titles into English. Make titles bold, with space under them.

!!! warning "Decide this first"
    The Content Creation meeting says fields like country of origin and expiry are **forced and unwanted**. Team Requests says the same missing fields are why **35% of products fail the audit**.
    **Proposal:** make them optional with a default value, and stop the audit from failing products on them. This one decision settles both requests.

## Track 3: Clear the blockers (owners and dates, no dev time)

| Blocker | What it unlocks | Owner | How to resolve it |
|---|---|---|---|
| Is the WhatsApp Business API connected? Are there Meta-approved templates, marketing consent, and a way to generate a personal discount code per customer? | **Churn Prediction (100%)**, Multi-Channel Support (70%), handoff to human support | Farah / GoCare | Once confirmed, churn v1 is small: a rule for "no purchase in 90 days" plus a scheduled WhatsApp send. The meeting already dropped the ML and CLV parts. |
| How far back does purchase and booking history go? Are order values and customer activity recorded? | Churn, Personalized Marketing (80%), Smart Salon (60%) | GoCare backend | One working session. Fill in the "Unconfirmed" rows in each feature's data table. |
| Does a notification system exist, and where does the marketing team approve campaigns? | Personalized Marketing | Farah | Confirm the channel and the approval step. |
| Are product images good enough for matching? | Visual Search (80%) | AI team | Run Image Audit (Track 1.5) on the catalog and report pass rates. |
| Product cost and price history. | Dynamic Pricing (70%) | GoCare | Without cost data, the system can't keep a minimum margin. |
| Database for chat memory (Postgres or Redis). | Conversation Memory (90%) | AI team | Internal decision this week. |

!!! note "Dynamic Pricing is not 'done, only testing left'"
    The meeting notes say it is complete. In the code, it is a command-line competitor-price finder (Serper web search) on the unmerged `pricing-agent` branch (last commit 13 Jul 2026). It has no API endpoint and no cost or margin rules. It needs the cost data above, then an API and pricing rules.

## Track 4: Build next (month 2, after Tracks 1–3 move)

| Order | Feature | Builds on | Starts when |
|---|---|---|---|
| 1 | **Skincare Routine Advisor (50%)**: add body care and the order-of-use rules in chat. Add the checkout card only if it's cheap. | Routine Maker (built) | Chat is live |
| 2 | **Conversation Memory (90%) + Session Management (80%), MVP scope**: save conversations on the server (LangGraph checkpointer), one thread per conversation. | Chat agent | Database decided |
| 3 | **Churn Prediction v1 (100%)**: the 90-day rule plus a WhatsApp win-back code. | Existing WhatsApp order channel | WhatsApp blocker cleared |
| 4 | **Personalized Marketing (80%)**: segments plus campaigns the marketing team approves, at most one every two weeks. | Recommendation data | Data and notification blockers cleared |
| 5 | **Visual Search (80%)**: image embeddings plus search-bar upload. | Vision (built), Image Audit | Images pass audit, Shade field exists |
| 6 | **Interactive Elements (70%)**: product carousels and quick replies in chat. | Recommendations in the frontend | Track 1.4 done |
| 7 | **Admin Dashboard (70%)**: start with knowledge-base editing only. | Knowledge Base endpoints | Chat is live |

## Parked

- **Deferred by the meeting:** Collaborative Filtering, Sentiment Analysis, Demand Forecasting (not enough data yet), Deep Learning Models, Context-Aware Recommendations.
- **Became a manual task:** Social Recommendations (the marketing team picks viral products each month).
- **Only if server cost becomes a problem:** Model Compression. It has no customer value.
- **Not built at all:** Voice Interface. No code exists in any branch.
- **Low-priority agent features:** Multi-Agent Workflows, Advanced Tool Management, Testing & QA, Loyalty Program, Content Management, User Profiles, User Engagement, Customer Profile Integration.

## This week

1. Decide the production branch and environment (1.0), the `/api/v1` integration target (1.4), and the memory database.
2. Check whether the frontend sends the chat history (1.2), and write the chat and safety acceptance test set (1.1).
3. Settle the required-fields conflict with Farah, and send her the WhatsApp, customer-data and notification questions (Track 3).
4. Retest image audit, salon queries and product search on a known version (1.5).
5. Give the backend team the admin-panel list from Track 2.

Capacity: at a base of 44 h per person per month, Tracks 1–3 will fill most of a month. Commit to Track 4 only after you see how far Track 1 gets.
