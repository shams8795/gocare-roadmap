# Analytics Dashboard

## 1. Feature Overview

**Analytics Dashboard** is an internal dashboard that shows how well GoCare's recommendation system is performing, and how users interact with the website.

The dashboard covers four main areas:

- **Recommendation CTR:** how often users click on recommendations compared to how often they are shown.
- **Popular products tracking:** the most viewed, added to cart, and purchased products.
- **User engagement metrics:** visits, active users, session duration, and pages viewed.
- **Conversion rates:** how many recommendation clicks lead to actual purchases or bookings.

**Example:**

The team opens the dashboard and sees that recommendations on product pages have a 12% CTR, while recommendations on the homepage have only 4%, which helps them decide where to improve.

## 2. Current Website Status

Based on the review in this report:

- GoCare shows recommendations to users, but it is not yet confirmed whether recommendation views and clicks are tracked.
- It is not yet confirmed which analytics tools are used today (e.g. Google Analytics or an internal tool).
- The other features in this roadmap all define success metrics, but there is no central place to view them yet.
- GoCare already has an Admin Dashboard that shows information about customers, and it is used by more than one admin.

**What does this mean for the feature?**

- Tracking must be confirmed or added before the dashboard can show reliable numbers.
- The dashboard can become the place where all features' success metrics are measured.
- The new analytics can be added to the existing Admin Dashboard, instead of building a separate dashboard.

## 3. Business Objective

The main goal is to measure the real impact of the recommendation system and support data-driven decisions.

**Expected benefits:**

- Clear visibility of whether recommendations increase sales.
- Faster detection of problems, such as a sudden drop in clicks.
- Better decisions on which features and placements to invest in.
- One shared view of performance for management and the technical team.

**Example:**

After launching Smart Salon Services, management can see in the dashboard how many bookings came from recommendations, instead of guessing.

**Priority:** High, according to the roadmap.

## 4. Clarification Questions

### 4.1 Questions for the Backend and Data Team

1.  Are recommendation impressions and clicks currently tracked?
2.  Can purchases and bookings be linked back to the recommendation that led to them?
3.  Which analytics tools or databases are already in use?
4.  What tool or framework is the existing Admin Dashboard built with, and can new charts be added to it?
5.  How long is event data stored?

## 5. Functional Requirements

**FR-01: Recommendation CTR**

The dashboard must show recommendation clicks divided by impressions, by placement (e.g. homepage, product page, cart).

**FR-02: Popular products tracking**

The dashboard must show the most viewed, added to cart, and purchased products.

**FR-03: User engagement metrics**

The dashboard must show visits, active users, session duration, and pages per session.

**FR-04: Conversion rates**

The dashboard must show how many recommendation clicks lead to purchases or bookings.

**FR-05: Filtering**

Users must be able to filter metrics by date range, placement, and product category.

**Proposed additional requirements (need client confirmation):**

- **FR-06:** Scheduled reports by email.
- **FR-07:** Alerts when a key metric drops suddenly.
- **FR-08:** A/B test results for features such as Personalized Marketing.

## 6. Non-Functional Requirements

**1. Accuracy**

The numbers must be correct and consistent with other company reports.

**2. Performance**

The dashboard must load quickly, even for long date ranges.

**3. Access Control**

Only authorized admins can access the analytics. Since more than one admin uses the Admin Dashboard, access can be controlled by role, so each admin sees only the metrics relevant to their work.

**4. Privacy & Security**

The dashboard must show aggregated numbers, not personal customer data, in line with data protection regulations in Saudi Arabia.

**5. Reliability**

Tracking must not slow down the website for users.

*Note: target values for data freshness and loading time must be defined with the technical team.*

## 7. Data Requirements

| Data                       | Purpose                           | Status                                                                 |
|----------------------------|-----------------------------------|------------------------------------------------------------------------|
| Recommendation Impressions | Calculate CTR                     | Unconfirmed                                                            |
| Recommendation Clicks      | Calculate CTR and conversion      | Unconfirmed                                                            |
| Product Views              | Track popular products            | Unconfirmed                                                            |
| Add-to-Cart Events         | Track popular products and funnel | Unconfirmed                                                            |
| Purchases & Bookings       | Calculate conversion rates        | Purchases available in the recommendation system; bookings unconfirmed |
| Sessions & Visits          | Measure user engagement           | Unconfirmed                                                            |

**Example:**

If recommendation impressions are not tracked, CTR cannot be calculated, even if clicks are recorded.

## 8. Technical Feasibility

The first version starts with:

- **Tracking:** record recommendation impressions, clicks, and conversions as events.

Later, improvements can be added, such as automatic alerts and A/B test reporting.

**Initial assessment:** technically feasible. The main effort is in adding reliable tracking; building the dashboard itself is relatively simple once the data exists.

## 9. Dependencies & Constraints

### Dependencies

- Event tracking on the website for recommendations, views, carts, and purchases.
- A database or analytics store for the events.
- Collaboration between the Frontend, Backend, Data, and Recommendation teams.

### Constraints & Risks

**1. Missing tracking**

If events are not tracked today, there will be no historical data at launch.

**2. Inconsistent definitions**

Different teams may calculate metrics such as conversion differently.

**3. Data volume**

Tracking every impression can create large amounts of data.

**Example:**

If tracking is added today, the dashboard will only show data from today onwards, so it cannot compare with previous months.

------------------------------------------------------------------------

## Meeting Decisions

The following points were agreed in the meeting:

**1. The feature is important**

The Analytics Dashboard is considered useful and important, since it helps the team measure the impact of the other features.

**2. Not a top priority right now**

The feature is not a top priority at the moment. It stays in the plan, and work on it will start after the more urgent features.

**3. Built inside the existing Admin Dashboard**

The analytics will be added to GoCare's existing Admin Dashboard, which is used by more than one admin, instead of building a separate dashboard.

**4. Used by the Admin Dashboard admins**

The analytics are used by the admins who already use the Admin Dashboard.

**5. Recommendation metrics are the most important**

The most important numbers are the recommendation metrics, such as how often recommendations are clicked and how many lead to purchases.

**6. How a conversion from a recommendation is counted**

A purchase is counted as a conversion from a recommendation when the customer buys the product through the recommendation.

<div dir="rtl" style="text-align: right;">
<p><strong>مثال:</strong></p>
<p>سيعمل الفريق أولًا على الميزات الأكثر إلحاحًا.</p>
<ul>
<li><strong>بعد ذلك:</strong> تُضاف الأرقام الجديدة إلى لوحة التحكم التي يستخدمها المسؤولون حاليًا.</li>
<li><strong>النتيجة:</strong> يرى المسؤولون في مكان واحد كم زادت المبيعات والحجوزات بفضل كل ميزة.</li>
</ul>
</div>
