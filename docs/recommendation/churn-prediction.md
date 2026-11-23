# Churn Prediction

## 1. Feature Overview

**Churn Prediction** aims to identify GoCare customers who are likely to stop buying or booking, before they actually leave, so the business can act early to keep them.

The feature has three main parts:

- **Identifying at-risk customers:** a model that estimates, for each customer, the probability that they will stop using GoCare, based on their past behavior.
- **Proactive retention campaigns:** sending targeted offers or reminders to at-risk customers before they leave.
- **Customer Lifetime Value (CLV):** estimating how much each customer is expected to spend on GoCare over time, to understand the value of each customer.

**Example:**

A customer who used to buy skin care products every month has not purchased in three months. The system marks her as at-risk, and she receives a WhatsApp message with a personal discount code to encourage her to buy again.

Note: unlike the other features in this section, this is a prediction and analytics feature rather than a product recommendation feature, although it relies on the same customer data.

## 2. Current Website Status

Based on the review in this report:

- GoCare combines a beauty products store with salon booking, so customer activity includes both purchases and bookings.
- The website already offers loyalty incentives, such as 1,000 points on registration, which could be used in retention offers.
- It is not yet confirmed how much purchase and booking history is stored, and for how long.
- It is not yet confirmed whether customer activity, such as visits and logins, is recorded.
- Customers already confirm their orders on WhatsApp.

**What does this mean for the feature?**

- The prediction model depends on enough historical customer data, which must be confirmed first.
- Existing loyalty points and offers can be reused in retention campaigns.

## 3. Business Objective

The main goal is to reduce customer loss and increase revenue by keeping existing customers, which is usually cheaper than acquiring new ones.

**Expected benefits:**

- Fewer customers leaving GoCare.
- Retention efforts focused on customers who are actually at risk.
- Acting early, before customers are lost completely.
- A clearer understanding of why customers leave.

**Example:**

Instead of waiting until customers are lost, GoCare sends every customer who has not bought anything for three months a personal discount code on WhatsApp.

**Business Impact:** High, according to the client's assessment.

## 4. Client Clarification Questions

### 4.1 Questions for the Backend and Data Team

1.  How far back does purchase and booking history go?
2.  Is customer activity recorded (visits, logins, searches, cart activity)?
3.  Are order values stored, so customer spending can be calculated?
4.  Are returns, cancellations, and refunds recorded?
5.  Can prediction results be stored and shared with the WhatsApp messaging system?

## 5. Functional Requirements

**FR-01: Churn risk scoring**

The system must estimate a churn risk score for each customer.

*Example:* customer A has an 80% probability of churning, customer B has 10%.

**FR-02: At-risk customer list**

The system must produce a list of at-risk customers, updated regularly.

*Example:* a weekly list of customers with high churn risk.

**FR-03: Customer Lifetime Value calculation**

The system must estimate the expected lifetime value of each customer.

*Example:* customer A is expected to spend 3,000 SAR over the next year.

**FR-04: Retention campaign support**

The system must provide at-risk segments that can be used in retention campaigns.

*Example:* high-risk customers receive a WhatsApp message with a personal discount code, encouraging them to buy again from the website.

**Proposed additional requirements (need client confirmation):**

- **FR-05:** A dashboard showing churn risk, CLV, and retention campaign results.
- **FR-06:** Main reasons behind each customer's risk score (e.g. fewer visits, longer time since last purchase).
- **FR-07:** Tracking whether retained customers actually returned after a campaign.

## 6. Non-Functional Requirements

**1. Model Accuracy**

Predictions must be accurate enough to be useful, and measured before launch.

**2. Explainability**

The business team should be able to understand why a customer is marked as at-risk.

**3. Regular Updates**

Risk scores must be refreshed regularly as customer behavior changes.

**4. Privacy & Security**

Customer data must be protected and used in line with data protection regulations in Saudi Arabia.

**5. Reliability**

A failure in the prediction pipeline must not affect the website or other systems.

*Note: target values for model accuracy and update frequency must be defined with the technical team.*

## 7. Data Requirements

| Data                               | Purpose                                | Status                                         |
|------------------------------------|----------------------------------------|------------------------------------------------|
| Purchase History                   | Track buying patterns and spending     | Available in the product recommendation system |
| Booking History                    | Track salon customer activity          | Unconfirmed                                    |
| Order Values                       | Calculate spending and CLV             | Unconfirmed                                    |
| Customer Activity (visits, logins) | Detect declining engagement            | Unconfirmed                                    |
| Cart Activity                      | Detect abandoned purchases             | Unconfirmed                                    |
| Returns & Cancellations            | Detect dissatisfaction signals         | Unconfirmed                                    |
| Customer Profile                   | Registration date and basic attributes | Unconfirmed                                    |
| Campaign Results                   | Measure retention success              | Not collected yet                              |

**Example:**

If GoCare has only a few months of purchase history, the model will not have enough examples of customers who left, and its predictions will be unreliable.

## 8. Technical Feasibility

The first version can start simple:

- **Rule-based risk scoring:** e.g. customers with no purchase in three months are marked as at-risk.
- **RFM analysis:** scoring customers by Recency, Frequency, and Monetary value to identify valuable and at-risk customers.
- **Simple CLV estimate:** average order value multiplied by purchase frequency and expected customer lifetime.

When enough history is available, Machine Learning models can be tested, such as:

- **Classification models** (e.g. Logistic Regression, Random Forest, Gradient Boosting) to predict churn probability.
- **Probabilistic CLV models** to estimate future customer value more accurately.

**Initial assessment:** technically feasible, but the quality of predictions depends mainly on the amount and history of customer data available.

## 9. Dependencies & Constraints

### Dependencies

- Enough historical purchase, booking, and activity data.
- The agreed definition of churn: no purchase for three months.
- The WhatsApp Business API, to send win-back messages.
- Collaboration between the Data, Backend, and Recommendation teams, and the marketing team.

### Constraints & Risks

**1. Limited history**

If GoCare is relatively new, there may not be enough examples of churned customers to train a model.

**2. Unclear churn definition**

Customers buy beauty products at different frequencies, so one fixed definition may not fit all customers.

**3. Acting too late or too often**

Predictions are only useful if retention actions follow quickly, without overwhelming customers with offers.

**4. Measuring real impact**

Some at-risk customers may return on their own, so retention results must be compared with a control group.

**Example:**

If 30% of at-risk customers return after a campaign, but 25% of a similar group that received nothing also returned, the campaign's real impact is only 5%.

------------------------------------------------------------------------

## Meeting Decisions

The following points were agreed in the meeting:

**1. Orders are confirmed on WhatsApp**

Customers already confirm their orders on WhatsApp, similar to how shipping companies such as Bosta work. This existing WhatsApp channel will be reused.

**2. Handoff to human support on WhatsApp**

If a customer wants to make any change to their order, and the system cannot understand the request, the conversation is transferred to a human on a dedicated WhatsApp support number.

**3. Win-back messages on WhatsApp**

If a customer has not bought anything for three months, the system sends them a WhatsApp message with a discount code, encouraging them to buy again from the website. This replaces sending retention offers through the Personalized Marketing feature.

**4. All inactive customers receive the code**

Every customer who has not bought anything for three months receives the discount code. Customer Lifetime Value is not used to decide who receives the offer.

Requirements for this:

- Messages must use WhatsApp message templates approved by Meta.
- Messages are sent only to customers who agreed to receive marketing messages.
- Each customer receives a personal discount code, so purchases from the message can be tracked.
- Each inactive customer receives the message only once in a set period, since every WhatsApp marketing message has a cost.

<div dir="rtl" style="text-align: right;">
<p><strong>مثال:</strong></p>
<p>عميلتان في موقفين مختلفين على واتساب.</p>
<ul>
<li><strong>عميلة تريد تغيير عنوان طلبها على واتساب:</strong> لا يستطيع النظام فهم طلبها، فتُحوَّل إلى رقم الدعم على واتساب، ويساعدها أحد موظفي الدعم.</li>
<li><strong>عميلة لم تشترِ أي شيء منذ ثلاثة أشهر:</strong> تصلها رسالة على واتساب فيها كود خصم شخصي ورابط للموقع، فتستخدم الكود وتشتري مرة أخرى.</li>
</ul>
</div>

**Open question:**

- **Discount value and validity:** the discount value and how long the code stays valid are still to be agreed.

**Blocker:**

- **Is the WhatsApp Business API already connected to GoCare's system?**

  To send messages automatically, without someone sending them manually, the WhatsApp Business API is required. If it is already used to confirm orders, the same connection can be reused. If not, it must be set up first, and the win-back messages cannot be sent until then.
