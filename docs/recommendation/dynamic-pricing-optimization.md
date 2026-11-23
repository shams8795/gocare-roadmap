# Dynamic Pricing Optimization

## 1. Feature Overview

### The problem

Product prices on GoCare are usually set once and changed manually. Meanwhile, competitors change their prices, and demand for products rises and falls. As a result:

- Some products are priced higher than competitors and sell slowly.
- Some products are discounted even when demand is already high.
- The team cannot manually track competitor prices for thousands of products.

### What the feature does

**Dynamic Pricing Optimization** suggests a suitable price for each product, based on two main inputs:

- **Competitor price monitoring:** tracking the prices of the same products in other stores.
- **Demand-based adjustments:** adjusting the suggested price based on demand, such as high demand before Eid, low demand, or low stock.

These are **price recommendations**, reviewed and approved by the team before they are applied.

**Example:**

| Product          | GoCare price | Competitor price | Demand               | Suggested action                   |
|------------------|--------------|------------------|----------------------|------------------------------------|
| Sunscreen SPF 50 | 85 SAR       | 70 SAR           | Low                  | Lower the price to around 75 SAR   |
| Perfume X        | 300 SAR      | 310 SAR          | High (before Eid)    | Keep the price, no discount needed |
| Serum Y          | 120 SAR      | 120 SAR          | Very low, high stock | Suggest a limited-time discount    |

In short:

- **Input:** GoCare prices, competitor prices, sales and demand data, and stock levels.
- **Output:** a suggested price, or price action, for each product.
- **Result:** more competitive prices and better sales, without unnecessary discounts.

## 2. Current Website Status

Based on the review in this report:

- GoCare runs offers such as free shipping on the first order in Riyadh, installment payments with Tabby and Tamara, and loyalty points.
- Products come from different brands and sellers.
- It is not yet confirmed who sets product prices today: GoCare, the sellers, or the brands.
- It is not yet confirmed whether competitor prices are tracked in any way today.

**What does this mean for the feature?**

- Who controls prices decides who will use the price recommendations.
- Competitor price data must be collected before the feature can work.

## 3. Business Objective

The main goal is to set competitive prices that increase sales and protect profit margins, based on data instead of manual guessing.

**Expected benefits:**

- **More competitive prices:** fewer products priced far above competitors.
- **Better margins:** avoiding unnecessary discounts on products with high demand.
- **Faster stock movement:** suggesting discounts for slow-moving products with high stock.
- **Less manual work:** the team does not need to check competitor prices by hand.

**Example:**

Instead of giving the same 20% discount on all perfumes before Eid, GoCare discounts only perfumes with low demand, and keeps the price of best-sellers.

**Business Impact:** High, according to the client's assessment.

## 4. Client Clarification Questions

### 4.1 Questions for the Client

**1. Who sets and approves prices?**

GoCare, the sellers, or the brands? Who will approve the suggested prices?

**2. Which competitors should be monitored?**

Which stores or websites, and for which product categories?

**3. Are there pricing limits?**

For example: minimum profit margin, maximum discount, or prices fixed by brand agreements?

**4. How often can prices change?**

Daily, weekly, or only during campaigns?

**5. Should prices be applied automatically or manually?**

Should the team approve every suggestion, or can small changes be applied automatically?

### 4.2 Questions for the Backend and Data Team

1.  Is price history stored for each product?
2.  Is product cost stored, so profit margin can be calculated?
3.  Are sales, stock levels, and promotions recorded over time?
4.  Is there any existing source of competitor prices?
5.  Can product prices be updated through an API?

### 4.3 Shared Question for the Client and Data Team

**How will competitor prices be collected?**

The client confirms which competitors and products matter, and whether collecting their prices is allowed. The data team confirms the method, such as a pricing data provider or an approved data feed.

## 5. Functional Requirements

**FR-01: Competitor price monitoring**

The system must collect and store competitor prices for matching products.

*Example:* the system records that the same sunscreen is sold at 70 SAR in another store.

**FR-02: Product matching**

The system must match GoCare products with the same products in competitor stores.

*Example:* "Sunscreen SPF 50, 50 ml" on GoCare is matched with the same product, brand, and size on another site.

**FR-03: Price recommendations**

The system must suggest a price, or a price action, for each product based on competitor prices, demand, and stock.

*Example:* lower the price, keep the price, or suggest a limited-time discount.

**FR-04: Pricing rules**

The system must respect pricing limits, such as minimum margin and maximum discount.

*Example:* the system never suggests a price below cost.

**Proposed additional requirements (need client confirmation):**

- **FR-05:** A review screen to approve or reject price suggestions.
- **FR-06:** Alerts when a competitor price changes significantly.
- **FR-07:** Automatic application of small, approved price changes.
- **FR-08:** Reports comparing sales before and after price changes.

## 6. Non-Functional Requirements

**1. Accuracy**

Product matching and price suggestions must be accurate, since wrong prices directly affect revenue.

**2. Data Freshness**

Competitor prices must be updated often enough to be useful.

**3. Control & Traceability**

Every price change must be recorded, with who approved it and why.

**4. Legal Compliance**

Competitor price collection and pricing practices must follow applicable laws and the terms of the data sources.

**5. Reliability**

A failure in the pricing system must not change or break the prices shown on the website.

*Note: target values for update frequency and matching accuracy must be defined with the technical team.*

## 7. Data Requirements

| Data              | Purpose                                       | Status                                         |
|-------------------|-----------------------------------------------|------------------------------------------------|
| Current Prices    | Compare with competitors                      | Exists on the website                          |
| Price History     | Learn how price affects sales                 | Unconfirmed                                    |
| Product Cost      | Calculate margins and minimum price           | Unconfirmed                                    |
| Sales History     | Measure demand                                | Available in the product recommendation system |
| Stock Levels      | Adjust prices for low or high stock           | Unconfirmed                                    |
| Promotions        | Separate promotion effects from normal demand | Unconfirmed                                    |
| Competitor Prices | Main input for comparison                     | Not available; source needs to be agreed       |

**Example:**

If product cost is not available, the system may suggest a lower price that is actually below cost, which would cause a loss.

## 8. Technical Feasibility

The first version can be rule-based:

- Collect competitor prices for a limited set of key products.
- Match products by brand, name, and size.
- Apply clear pricing rules, such as "stay within 5% of the lowest competitor price, without going below the minimum margin".
- Use demand and stock data to decide between lowering, keeping, or discounting the price.

Later, more advanced approaches can be tested, such as:

- **Price elasticity models:** estimating how much sales change when the price changes.
- **Machine Learning models** that combine demand forecasting, competitor prices, and seasonality.

**Initial assessment:** technically feasible, but it depends mainly on a reliable and allowed source of competitor prices, and on having product cost data.

## 9. Dependencies & Constraints

### Dependencies

- A reliable and allowed source of competitor prices.
- Product cost and pricing rules.
- Sales, stock, and price history.
- The Demand Forecasting feature, which provides demand signals.
- Collaboration with the pricing or commercial team, and with sellers if they control prices.

### Constraints & Risks

**1. Competitor data access**

Collecting competitor prices may be limited by website terms, technical blocks, or cost.

**2. Product matching errors**

Comparing different products, sizes, or versions leads to wrong suggestions.

**3. Price wars**

Automatically following competitor prices can lead to repeated price drops and lower margins.

**4. Customer trust**

Frequent price changes may reduce customer trust.

**Example:**

If a 50 ml product is matched with a 100 ml version on another site, the competitor price will look higher than it really is, and the suggestion will be wrong.

------------------------------------------------------------------------

## Meeting Decisions

The feature has already been completed, and only testing remains.
