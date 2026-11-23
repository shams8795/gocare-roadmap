# Integration Status

Status of every GoCare AI endpoint, based on the endpoint testing sheet and checked against the code in `Adwat/GoCare-Agents` and `Adwat/Gocare-Product-Recommendation-System` (branches `dev` and `test`) on 21 Nov 2026.

**Downloads:** [Excel workbook](data/gocare-endpoints-review.xlsx) · [Reviewed sheet (CSV)](data/endpoints-reviewed.csv) · [Original testing sheet (CSV)](data/endpoints-original.csv)

## Summary

**6 of 22** endpoints are live, and all of them are internal catalog tools (audit, enhancement, duplicate detection). **No customer-facing AI is live yet:** the chat and everything inside it is in testing, and the recommendation endpoints are not called by the website.

| Status | Count | Meaning |
|---|---|---|
| Live | 6 | Used on the website today. |
| In testing | 7 | Works, but not released to customers yet. |
| Needs frontend | 4 | Backend works; the website does not call it yet. |
| Built, not working in tested env | 3 | Code exists, but it failed or was missing on the environment that was tested. |
| Built, off by default | 1 | Code exists behind a feature flag that is off. |
| Not built | 1 | No code found. |
| **Total** | **22** | |

## Release status by branch

Before anything is called "in production", agree which branch and environment production is:

| Repo | `main` | `test` | `dev` |
|---|---|---|---|
| GoCare-Agents | v0.1 (16 Nov 2025) | v0.5.4 (23 Sep 2026) | v0.5.4+ (29 Oct 2026) |
| Recommendation System | v1.4.0 (31 Dec 2025) | v1.8.0 (21 Aug 2026) | v1.8.0+ (29 Oct 2026) |

In both repos, the production deploy workflow (`deploy-prod.yml`, on `test` and `dev`) runs on pushes to `main`. But it has never been merged into `main`, which is still v0.1 and v1.4.0. So production is deployed some other way, and the repos can't tell you which version it runs. The testing sheet doesn't say which environment was tested either, which is the likely reason some built endpoints showed as missing.

## Changes from the original sheet

| # | Feature | Sheet said (exists / correct / on website) | Reviewed status | Why |
|---|---|---|---|---|
| 13 | Image Audit | No / No / No | **Built, not working in tested env** | GoCare-Agents test & dev (v0.5.4): POST /api/images/audit and /api/images/audit/batch are registered (src/api/routes/image_audit.py). |
| 14 | Image Audit (watermark detection) | No / No / No | **Built, off by default** | GoCare-Agents: needs IMAGE_AUDIT_SEMANTIC_ENABLED=true (default false) and deep=true. |
| 19 | Routine Safety Assessment | Yes / Yes / Yes | **In testing** | GoCare-Agents: src/agents/routine_maker/nodes/audit_safety.py. It runs inside Routine Maker, which is still in testing, so it cannot be live on its own (the sheet said Yes). |
| 20 | Salon Queries | No / No / No | **Built, not working in tested env** | GoCare-Agents test & dev (v0.5.4): POST /api/salon/queries is registered (src/api/routes/salon.py). |
| 26 | Product Search | No / Not sure / No | **Built, not working in tested env** | Recommendation-System: POST /api/search/products exists since v1.4.0 and /api/v1/search/products in v1.8.0. It uses the same 'similarity' model as Similar Products (which works), plus a text-embedding step the other endpoints don't have. |

Rows #3, #4, #5 and #9 are missing from the original sheet. Confirm whether they were dropped or merged.

## Live (6)

Used on the website today.

| # | Feature | Endpoint | Code check | Next action | Owner |
|---|---|---|---|---|---|
| 10 | Audit Agent | `POST /api/audit/product` | GoCare-Agents: POST /api/audit/product and /api/audit/products registered. | Record which environment URL and version were tested. | — |
| 11 | Web search in audit | `POST /api/audit/product` | GoCare-Agents: web search only runs when SERPER_API_KEY is set. | Confirm SERPER_API_KEY is set on production. | — |
| 12 | Duplicate Detection | `POST /api/audit/products` | GoCare-Agents: duplicate detection plus /api/embeddings/products/sync and DELETE /api/embeddings/products/{product_ref}. | Record environment and version. | — |
| 15 | Title Enhancement | `POST /api/enhance/title` | GoCare-Agents: POST /api/enhance/title and /api/enhance/title/batch registered. | Record environment and version. | — |
| 16 | Description Enhancement | `POST /api/enhance/description` | GoCare-Agents: POST /api/enhance/description and /batch registered. | Record environment and version. Apply the 5-section template (Action Plan, Track 2). | — |
| 17 | Web research for enhancement | `POST /api/enhance/title?search=true` | GoCare-Agents: ?search=true is off by default and needs SERPER_API_KEY. | Confirm the key on production. | — |

## In testing (7)

Works, but not released to customers yet.

| # | Feature | Endpoint | Code check | Next action | Owner |
|---|---|---|---|---|---|
| 1 | Chat Assistant | `POST /api/chat/completion` | GoCare-Agents test & dev (v0.5.4): POST /api/chat/completion. The request carries the message list from the client; the server keeps the last 10 messages and stores nothing between sessions. | Write the acceptance test set. Confirm the frontend sends the full message history. Decide go-live. | — |
| 2 | Cart Management + Checkout | `POST /api/chat/completion` | GoCare-Agents: runs inside /api/chat/completion (cart_context in the body). | Add cart add/remove/update and checkout cases to the chat acceptance tests. | — |
| 6 | Vision Analysis | `POST /api/chat/completion` | GoCare-Agents: vision needs GEMINI_API_KEY and VISION_MODEL (default gemini-2.5-flash) in the environment. | Confirm the Gemini key is set on the production environment, then test. | — |
| 7 | Arabic dialect mirroring | `POST /api/chat/completion` | GoCare-Agents: dialect handling in the chat prompts. | Add Saudi, Egyptian and MSA samples to the acceptance tests. | — |
| 8 | Knowledge Base | `POST /api/chat/knowledge-base/search` | GoCare-Agents: both DELETE /api/chat/knowledge-base/delete and POST /api/chat/knowledge-base/documents/delete exist. They are two separate endpoints, not one endpoint with two methods. | Question answered. Document which delete the admin panel should call. | — |
| 18 | Routine Maker | `POST /api/chat/completion` | GoCare-Agents: routine_maker agent inside /api/chat/completion (routine_state in the body). | Include in chat acceptance tests. | — |
| 19 | Routine Safety Assessment | `POST /api/chat/completion` | GoCare-Agents: src/agents/routine_maker/nodes/audit_safety.py. It runs inside Routine Maker, which is still in testing, so it cannot be live on its own (the sheet said Yes). | Build a safety test set (pregnancy, allergies, medication) and get it signed off before go-live. | — |

## Needs frontend (4)

Backend works; the website does not call it yet.

| # | Feature | Endpoint | Code check | Next action | Owner |
|---|---|---|---|---|---|
| 22 | Cross-Selling | `POST /api/recommend/product/{product_id}` | Recommendation-System test & dev (v1.8.0): both /api/recommend/product/{id} (legacy) and /api/v1/recommend/product/{id} exist. Legacy routes already return a 'lang' deprecation warning. | Integrate against /api/v1 so the frontend does not need a second migration. | — |
| 23 | Upselling | `POST /api/recommend/upsell/{product_id}` | Recommendation-System v1.8.0: /api/recommend/upsell/{id} and /api/v1/recommend/upsell/{id}. | Integrate against /api/v1. | — |
| 24 | Similar Products | `POST /api/recommend/similar/{product_id}` | Recommendation-System v1.8.0: /api/recommend/similar/{id} and /api/v1/... (uses the 'similarity' model). | Integrate against /api/v1. | — |
| 25 | Bundles | `POST /api/recommend/bundle/product/{product_id}` | Recommendation-System v1.8.0: bundle/product, bundle/similar, bundle/cart on both route versions. | Integrate against /api/v1. | — |

## Built, not working in tested env (3)

Code exists, but it failed or was missing on the environment that was tested.

| # | Feature | Endpoint | Code check | Next action | Owner |
|---|---|---|---|---|---|
| 13 | Image Audit | `POST /api/images/audit` | GoCare-Agents test & dev (v0.5.4): POST /api/images/audit and /api/images/audit/batch are registered (src/api/routes/image_audit.py). | Check which version is deployed on the environment that was tested, redeploy if older, then retest. | — |
| 20 | Salon Queries | `POST /api/salon/queries` | GoCare-Agents test & dev (v0.5.4): POST /api/salon/queries is registered (src/api/routes/salon.py). | Check the deployed version, redeploy, then retest. | — |
| 26 | Product Search | `POST /api/search/products` | Recommendation-System: POST /api/search/products exists since v1.4.0 and /api/v1/search/products in v1.8.0. It uses the same 'similarity' model as Similar Products (which works), plus a text-embedding step the other endpoints don't have. | Retest with {"query": "dry skin", "top_k": 10} and save the error response. Check the text encoder is configured on that environment. | — |

## Built, off by default (1)

Code exists behind a feature flag that is off.

| # | Feature | Endpoint | Code check | Next action | Owner |
|---|---|---|---|---|---|
| 14 | Image Audit (watermark detection) | `POST /api/images/audit` | GoCare-Agents: needs IMAGE_AUDIT_SEMANTIC_ENABLED=true (default false) and deep=true. | Decide whether to enable it. If yes, set the flag and retest. | — |

## Not built (1)

No code found.

| # | Feature | Endpoint | Code check | Next action | Owner |
|---|---|---|---|---|---|
| 21 | Voice | `GET /api/voice/config` | No voice code in any GoCare-Agents branch (main, dev, test, Front, pricing-agent, feat/jev-classification). HUMAIN_VOICE_ENABLED does not appear in the code. | Treat as not started. Find out where the endpoint notes came from. | — |

## How to update this page

Edit `docs/data/endpoints-reviewed.csv`, then run `python scripts/build_status.py`. The script rebuilds this page and the Excel workbook.
