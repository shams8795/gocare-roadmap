# Personalized Marketing

## 1. Feature Overview

**Personalized Marketing** aims to automatically create marketing campaigns for different customer segments on GoCare, instead of sending the same offer to all customers.

The feature has three main parts:

- **Customer segmentation:** grouping customers based on their behavior and preferences (e.g. what they buy, how often, how much they spend, and whether they book salons).
- **Automated campaign creation:** preparing a suitable message or offer for each segment automatically.
- **A/B testing:** sending two versions of the same campaign to small groups, measuring which one performs better, then sending the better version to the rest of the segment.

**Example:**

Customers who often buy hair care products receive a notification about new hair care products, while customers who often book salons receive an offer on salon services.

## 2. Current Website Status

Based on the review in this report:

- GoCare combines a beauty products store with salon booking, so customer behavior can include both purchases and bookings.
- The website already runs general offers, such as free shipping on the first order in Riyadh, installment payments with Tabby and Tamara, and 1,000 points on registration.
- It is not yet confirmed which customer behavior data is recorded (e.g. page views, clicks, searches, abandoned carts).
- Campaigns will be sent as notifications.

**What does this mean for the feature?**

- GoCare already runs promotions, so the feature can build on existing offers rather than start from scratch.
- The feature depends heavily on behavior data, which must be confirmed first.

## 3. Business Objective

The main goal is to increase sales and customer engagement by sending each customer group offers that match their interests, instead of general offers.

**Expected benefits:**

- Higher response rates to campaigns.
- Increased repeat purchases and bookings.
- Less wasted marketing effort on offers that do not interest customers.
- Data-driven decisions on which messages and offers work best, through A/B testing.

**Example:**

Instead of sending the same discount to all customers, GoCare sends a hair care offer only to customers interested in hair care, which is more likely to lead to a purchase.

**Business Impact:** High, according to the client's assessment.

## 4. Client Clarification Questions

### 4.1 Questions for the Backend and Data Team

1.  Which customer behavior data is recorded (page views, clicks, searches, cart activity, purchases, bookings)?
2.  Is customer purchase and booking history stored and accessible?
3.  Are customers' marketing consent and contact preferences stored?
4.  Is there an existing integration with a notification service?
5.  Can campaign results (opens, clicks, purchases) be tracked back to each campaign?

### 4.2 Shared Question for the Client and Data Team

**What data can be used to segment customers?**

The client decides which customer attributes and behaviors should define segments, and the data team confirms which of them are actually recorded and can be used legally.

## 5. Functional Requirements

**FR-01: Customer segmentation**

The system must group customers into segments based on their behavior and preferences.

*Example:* a segment of customers who bought hair care products in the last 60 days.

**FR-02: Automated campaign creation**

The system must prepare a suitable campaign for each segment, including the message and the offer.

*Example:* customers who often buy skin care products receive a notification about a new serum, with a related offer.

**FR-03: A/B testing**

The system must support sending two versions of a campaign to small test groups and comparing their results.

*Example:* version A offers 10% off, version B offers free shipping; the version with more purchases is sent to the rest of the segment.

**FR-04: Campaign performance tracking**

The system must track the results of each campaign, such as opens, clicks, and purchases.

**FR-05: Campaign frequency limit**

Each customer must receive a maximum of one campaign notification about every two weeks.

**FR-06: Marketing team review**

Every campaign must be reviewed and approved by the marketing team before it is sent.

**Proposed additional requirements (need client confirmation):**

- **FR-07:** Product recommendations inside campaigns, based on the recommendation system.
- **FR-08:** Unsubscribe option in every campaign.

## 6. Non-Functional Requirements

**1. Scalability**

The system must handle growth in the number of customers and campaigns without significant delays.

**2. Reliability**

Campaigns must not be sent twice to the same customer, and failures must be logged and retried safely.

**3. Privacy & Security**

Customer data must be used only with marketing consent, and every campaign must allow customers to unsubscribe, in line with data protection and marketing regulations in Saudi Arabia.

**4. Measurability**

Every campaign must be trackable so its results can be measured and compared.

**5. Statistical Reliability**

A/B test results must be based on enough data to make the difference between versions meaningful, not random.

*Note: target values for sending speed, delivery rates, and test sample sizes must be defined with the technical team.*

## 7. Data Requirements

| Data                                        | Purpose                                           | Status                                         |
|---------------------------------------------|---------------------------------------------------|------------------------------------------------|
| Purchase History                            | Segment customers by what they buy                | Available in the product recommendation system |
| Booking History                             | Segment salon customers                           | Unconfirmed                                    |
| Browsing Behavior (views, clicks, searches) | Understand customer interests                     | Unconfirmed                                    |
| Cart Activity                               | Identify abandoned carts                          | Unconfirmed                                    |
| Customer Profile                            | Basic segmentation (e.g. city, registration date) | Unconfirmed                                    |
| Marketing Consent                           | Send campaigns legally                            | Unconfirmed                                    |
| Contact Channels                            | Deliver campaigns                                 | Notifications (agreed in the meeting)          |
| Campaign Results                            | Measure performance and run A/B tests             | Not collected yet                              |

**Example:**

If only purchase history is available, the system can segment customers by what they bought, but cannot target customers who showed interest in a product without buying it.

## 8. Technical Feasibility

The first version can be built with simple, rule-based segments:

- Segments defined by clear rules (e.g. last purchase date, number of orders, total spending, product categories).
- Campaign templates prepared for each segment.
- A simple A/B testing setup that randomly splits a segment into test groups.

Later, more advanced approaches can be tested, such as:

- **Clustering:** discovering customer segments automatically from behavior data.
- **RFM analysis:** segmenting customers by Recency, Frequency, and Monetary value.
- **AI-generated content:** generating campaign messages for each segment, reviewed before sending.

**Initial assessment:** technically feasible, provided that customer behavior data, marketing consent, and a sending channel are available.

## 9. Dependencies & Constraints

### Dependencies

- Customer behavior and purchase data.
- A notification service and integration with it.
- Marketing consent data.
- Collaboration with the marketing team on offers and approvals.
- Collaboration between the Backend, Data, and Recommendation teams.
- Coordination with the Churn Prediction feature, which handles discount codes for inactive customers, so the same customer does not receive duplicate messages.

### Constraints & Risks

**1. Missing behavior data**

If browsing and cart activity are not recorded, segmentation will be limited to purchases only.

**2. Customer fatigue**

Sending too many campaigns may lead customers to unsubscribe or ignore messages.

**3. Legal and consent requirements**

Sending campaigns without proper consent can create legal and reputation risks.

**4. Small test groups**

If segments are small, A/B test results may not be reliable.

**Example:**

If a segment has only 50 customers, splitting it into two groups of 25 may not show a meaningful difference between the two versions.

------------------------------------------------------------------------

## Meeting Decisions

The following points were agreed in the meeting:

**1. Campaigns are sent as notifications only**

Personalized campaigns will be delivered to customers as notifications only. Other channels, such as email, SMS, and WhatsApp, are not part of this feature for now.

**2. Limited frequency**

Each customer receives a maximum of one campaign notification about every two weeks, to avoid customer fatigue.

**3. Discount codes for inactive customers move to Churn Prediction**

Win-back offers, such as discount codes for customers who stopped buying, will be handled by the Churn Prediction feature instead of this feature. Personalized Marketing focuses on sending relevant offers and products to active customer segments.

**4. Campaigns are reviewed by the marketing team**

Campaigns are not sent automatically. The marketing team reviews and approves every campaign before it is sent.

**5. All customer segments are included**

The feature covers all customer segments, such as new customers, frequent buyers, and salon customers.

<div dir="rtl" style="text-align: right;">
<p><strong>مثال:</strong></p>
<p>عميلتان لكل منهما سلوك شراء مختلف.</p>
<ul>
<li><strong>عميلة تشتري منتجات العناية بالشعر كثيرًا:</strong> يصلها إشعار واحد عن منتجات العناية بالشعر الجديدة، ولا يصلها أي إشعار حملة آخر خلال الأسبوعين التاليين.</li>
<li><strong>عميلة لم تشترِ أي شيء منذ ثلاثة أشهر:</strong> لا تحصل على كود خصم من هذه الميزة، وبدلًا من ذلك تتولى ميزة <bdi>Churn Prediction</bdi> التعامل معها.</li>
</ul>
</div>
