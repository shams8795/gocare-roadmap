# Demand Forecasting

## 1. Feature Overview

**Demand Forecasting** aims to predict how much of each product GoCare is expected to sell in the coming period, based on historical sales data, while taking seasons and trends into account.

The feature has three main parts:

- **Sales forecasting:** predicting the expected sales quantity of each product for the coming weeks or months.
- **Seasonal and trend awareness:** adjusting forecasts for seasons, holidays, and rising or falling trends.
- **Stock planning support:** helping the team decide when and how much to restock, to reduce stockouts and overstock.

**Example:**

The system predicts that sunscreen sales will increase in summer, and that perfume sales will increase before Ramadan and Eid, so the team orders larger quantities early.

Note: unlike the recommendation features, this is a prediction and analytics feature for internal teams, mainly inventory and purchasing, rather than a feature shown to users.

## 2. Current Website Status

Based on the review in this report:

- GoCare sells products across many categories, such as skin care, hair care, makeup, perfumes, personal care, and beauty devices.
- The website runs seasonal and promotional offers, which affect sales volumes.
- It is not yet confirmed how much sales history is stored, and for how long.
- It is not yet confirmed whether stock levels and stockout periods are recorded.
- It is not yet confirmed how stock is managed today, for example by GoCare directly or by each seller or brand.

**What does this mean for the feature?**

- Forecast quality depends mainly on the amount and quality of sales history.
- Promotions and stockouts must be recorded, otherwise the model may learn wrong patterns.
- The way stock is managed decides who will use the forecasts and how.

## 3. Business Objective

The main goal is to keep the right amount of stock for each product, so customers find what they want and less money is tied up in products that do not sell.

**Expected benefits:**

- Fewer stockouts and lost sales.
- Less overstock and fewer expired or unsold products.
- Better planning for seasonal peaks, such as summer, Ramadan, Eid, and promotional events.
- More data-driven purchasing decisions.

**Example:**

Instead of ordering the same quantity of sunscreen every month, the team orders more before summer and less in winter, based on the forecast.

**Business Impact:** High, according to the client's assessment.

## 4. Client Clarification Questions

### 4.1 Questions for the Client

**1. Who will use the forecasts?**

The inventory team, the purchasing team, sellers and brands on the platform, or management?

**2. What forecast horizon is needed?**

Next week, next month, or next season?

**3. At what level should forecasts be made?**

Per product, per category, per brand, or per city or warehouse?

**4. How should forecasts be delivered?**

A dashboard, a regular report, or automatic restock suggestions?

**5. Which events affect sales the most?**

For example: summer, Ramadan, Eid, White Friday, national holidays, or brand campaigns?

**6. How is stock managed today?**

Does GoCare hold the stock, or does each seller or brand manage their own stock?

### 4.2 Questions for the Backend and Data Team

1.  How far back does sales history go, and at what level (per order, per day, per product)?
2.  Are stock levels recorded over time, including periods when products were out of stock?
3.  Are promotions and discounts recorded with their dates?
4.  Are returns and cancellations recorded?
5.  Are new products, discontinued products, and product variants (e.g. sizes and shades) clearly identified?

## 5. Functional Requirements

**FR-01: Product demand forecasting**

The system must predict the expected sales quantity of each product for a defined future period.

*Example:* product A is expected to sell 300 units next month.

**FR-02: Seasonal and event adjustments**

The system must take seasons, holidays, and known events into account in the forecasts.

*Example:* perfume forecasts increase in the weeks before Eid.

**FR-03: Trend detection**

The system must detect products whose sales are rising or falling over time.

*Example:* a new serum shows steadily rising sales over the last eight weeks.

**FR-04: Stockout and overstock alerts**

The system must highlight products expected to run out soon, or that have more stock than expected demand.

*Example:* sunscreen stock is expected to run out in two weeks based on the summer forecast.

**Proposed additional requirements (need client confirmation):**

- **FR-05:** Suggested restock quantities for each product.
- **FR-06:** Forecasts per city or warehouse.
- **FR-07:** A dashboard comparing forecasts with actual sales.
- **FR-08:** Including planned promotions in the forecasts.

## 6. Non-Functional Requirements

**1. Forecast Accuracy**

Forecasts must be accurate enough to support purchasing decisions, and their error must be measured regularly against actual sales.

**2. Regular Updates**

Forecasts must be refreshed regularly, for example weekly, as new sales data arrives.

**3. Explainability**

The team should understand the main reasons behind a forecast, such as a seasonal peak or a recent trend.

**4. Scalability**

The system must handle a growing number of products and categories.

**5. Reliability**

A failure in the forecasting pipeline must not affect the website or other systems.

*Note: target values for forecast accuracy and update frequency must be defined with the technical team.*

## 7. Data Requirements

| Data                                   | Purpose                                     | Status                                                                        |
|----------------------------------------|---------------------------------------------|-------------------------------------------------------------------------------|
| Sales History                          | Train the forecasting model                 | Available in the product recommendation system; length of history unconfirmed |
| Stock Levels Over Time                 | Separate real demand from stockout periods  | Unconfirmed                                                                   |
| Promotions & Discounts                 | Explain sales peaks caused by offers        | Unconfirmed                                                                   |
| Product Catalog & Categories           | Group products and forecast new products    | Exists on the website                                                         |
| Returns & Cancellations                | Calculate real net demand                   | Unconfirmed                                                                   |
| Event Calendar                         | Account for Ramadan, Eid, and other seasons | Not available; needs to be prepared                                           |
| Product Lifecycle (new / discontinued) | Avoid forecasting discontinued products     | Unconfirmed                                                                   |

**Example:**

If a product was out of stock for two weeks, its sales during that time were zero, not because nobody wanted it, but because it was not available. If stock levels are not recorded, the model may wrongly learn that demand dropped.

## 8. Technical Feasibility

The first version can start with simple and well-known forecasting methods:

- **Baseline methods:** moving averages and same-period-last-year comparisons.
- **Statistical time series models:** such as Exponential Smoothing or ARIMA, which handle trends and seasonality.
- **Event adjustments:** adding known events, such as Ramadan and Eid, which move each year in the Gregorian calendar.

Later, more advanced approaches can be tested, such as:

- **Machine Learning models** (e.g. Gradient Boosting) that use features like price, promotions, category, and events.
- **Forecasting libraries** designed for business time series with holidays and seasonality.

**Initial assessment:** technically feasible. Forecast quality depends mainly on having enough sales history, recorded promotions, and recorded stock levels.

## 9. Dependencies & Constraints

### Dependencies

- Enough historical sales data, preferably more than one year.
- Recorded stock levels and promotions.
- An agreed list of important seasons and events.
- Collaboration with the inventory and purchasing teams.
- Collaboration between the Data, Backend, and Recommendation teams.
- Coordination with the Analytics Dashboard feature, which can display forecasts.

### Constraints & Risks

**1. Short sales history**

If GoCare does not have at least one full year of data, the model cannot learn yearly seasons reliably.

**2. Moving events**

Ramadan and Eid move about 11 days earlier each year in the Gregorian calendar, so simple yearly comparisons can be misleading.

**3. New products**

New products have no sales history, so their forecasts must rely on similar products in the same category.

**4. Hidden demand**

Stockouts and promotions can hide the real demand if they are not recorded.

**Example:**

If last year's Eid was in April and this year's Eid is in March, a model that only compares the same month of last year will predict the Eid peak in the wrong month.

------------------------------------------------------------------------

## Meeting Decisions

The following points were agreed in the meeting:

**1. Not a priority for now**

Demand Forecasting is not considered very important at the moment.

**2. Not enough data**

There is not enough customer and sales data yet to build reliable forecasts. As explained in this page, learning seasons such as summer, Ramadan, and Eid needs at least one full year of sales history.

<div dir="rtl" style="text-align: right;">
<p><strong>مثال:</strong></p>
<p>يريد النظام أن يتوقع زيادة مبيعات واقي الشمس في الصيف.</p>
<ul>
<li><strong>ما يحتاجه النظام:</strong> أن يرى أولًا بيانات المبيعات من صيف سابق واحد على الأقل.</li>
<li><strong>الوضع الحالي:</strong> هذه البيانات غير متوفرة بعد، لذلك لن تكون التوقعات موثوقة، وتم تأجيل الميزة حتى تُجمع بيانات كافية.</li>
</ul>
</div>
