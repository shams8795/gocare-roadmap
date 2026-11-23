# Collaborative Filtering

## 1. Feature Overview

### The problem

Most simple recommendation systems recommend products that are **similar to what the user viewed or bought**, based on product attributes such as category or brand. This is called **content-based filtering**. It works, but it has a limit: it only recommends products similar to what the user already knows, and rarely helps them discover something new that they may like.

### What the feature does

**Collaborative Filtering** recommends products based on **the behavior of similar users**, not only on product attributes.

**Example:**

| User   | Bought                                                       |
|--------|--------------------------------------------------------------|
| User A | Cleanser, Toner, Moisturizer, Sunscreen, **Vitamin C Serum** |
| User B | Cleanser, Toner, Moisturizer, Sunscreen                      |

User A and User B bought the same four products, so their tastes are similar. User A also bought a Vitamin C Serum, so the system recommends it to User B, even though it is not similar to anything User B has bought.

The roadmap describes two techniques:

- **User-to-user similarity:** finding users with similar behavior and recommending what they liked.
- **Matrix factorization:** a mathematical method that analyzes a large table of all users and all products, and discovers hidden patterns in their preferences.

### What "hybrid" means

The goal is a **hybrid recommendation approach** that combines:

- **Content-based filtering:** "this product is similar to what you bought".
- **Collaborative filtering:** "users similar to you bought this".

Combining both gives more accurate and more varied recommendations than either one alone.

## 2. Current System Status

Based on the information available in this report:

- GoCare already has a product recommendation system in production.
- It is not yet confirmed which methods the current system uses.
- It is not yet confirmed how much user interaction data is recorded (views, clicks, add-to-cart, purchases, bookings).

**What does this mean for the feature?**

- The new method must be added to the existing system, not built from scratch.
- Collaborative filtering depends heavily on the amount of interaction data available.

## 3. Business Objective

The main goal is to make recommendations more accurate and more varied, so users discover more products they like and buy more.

**Expected benefits:**

- **Better recommendations:** based on real behavior, not only product attributes.
- **More discovery:** users find products they would not have searched for.
- **Higher conversion and order value:** more relevant products shown to each user.
- **Improves over time:** recommendations get better as more users interact with the website.

**Example:**

A user who only buys skin care products may receive a recommendation for a hair care product that many similar users bought, which content-based filtering alone would not suggest.

**Priority:** High, according to the roadmap.

## 4. Clarification Questions

### 4.1 Questions for the Team Lead / Client

**1. Where should the hybrid recommendations be used?**

Homepage, product pages, cart, chatbot, or all of them?

**2. How should the new recommendations be evaluated before launch?**

Offline tests on historical data, A/B testing with real users, or both?

**3. Should salons and services be included?**

Products only, or also salon services and bookings?

### 4.2 Questions for the Backend and Data Team

1.  Which recommendation methods does the current system use?
2.  Which user interactions are recorded (views, clicks, add-to-cart, purchases, bookings)?
3.  How many users and how many interactions are available?
4.  Are guest users tracked, or only logged-in users?
5.  How often is the current recommendation model retrained?

### 4.3 Shared Question

**Is there enough interaction data?**

Collaborative filtering needs many users interacting with many products. The data team confirms the amount of data, and the team lead decides whether to start now or after collecting more data.

## 5. Functional Requirements

**FR-01: User-to-user similarity**

The system must find users with similar behavior and use their interactions to recommend products.

**FR-02: Matrix factorization model**

The system must train a matrix factorization model on user-product interactions to predict which products each user may like.

**FR-03: Hybrid recommendations**

The system must combine collaborative filtering results with content-based results into one recommendation list.

*Example:* half of the recommendations come from similar products, and half from similar users, ranked together.

**FR-04: Cold-start handling**

The system must fall back to content-based or popular products for new users and new products with no interactions.

*Example:* a new user with no history sees popular products, then personalized recommendations after a few interactions.

**Proposed additional requirements (need confirmation):**

- **FR-05:** Regular retraining of the model with new interaction data.
- **FR-06:** A/B testing of hybrid recommendations against the current system.
- **FR-07:** Including salon services in the recommendations.

## 6. Non-Functional Requirements

**1. Performance**

Recommendations must be returned quickly, without slowing down the website.

**2. Scalability**

The model must handle growth in users, products, and interactions.

**3. Recommendation Quality**

The hybrid approach must perform better than the current system on agreed metrics, such as click-through and conversion rates.

**4. Privacy**

User interaction data must be used in line with data protection regulations in Saudi Arabia.

**5. Reliability**

If the new model fails, the system must fall back to the current recommendations.

*Note: target values for response time and quality improvement must be defined with the technical team.*

## 7. Data Requirements

| Data                            | Purpose                                | Status                                         |
|---------------------------------|----------------------------------------|------------------------------------------------|
| Purchase History                | Main signal of user preferences        | Available in the product recommendation system |
| Views, Clicks, Add-to-Cart      | Extra signals of interest              | Unconfirmed                                    |
| Booking History                 | Include salon services                 | Unconfirmed                                    |
| Ratings                         | Explicit user preferences              | Feature exists; amount unconfirmed             |
| Product Attributes              | Content-based part of the hybrid model | Exists; completeness needs review              |
| User IDs (logged in and guests) | Link interactions to users             | Unconfirmed                                    |

**Example:**

If most users bought only one product, there is not enough overlap between users to find similar ones, and collaborative filtering will not work well.

## 8. Technical Feasibility

Collaborative filtering is a well-known and widely used approach:

- **Matrix factorization** methods, such as ALS, are available in standard libraries and work well with purchase and click data.
- **User-to-user similarity** can be calculated with simple similarity measures, such as cosine similarity.
- **Hybrid ranking** can combine the scores of content-based and collaborative models.

**Initial assessment:** technically feasible, and it builds on the existing recommendation system. The main condition is having enough interaction data.

## 9. Dependencies & Constraints

### Dependencies

- Enough user interaction data.
- Access to the current recommendation system and its data.
- Good product attributes for the content-based part, supported by Automated Content Tagging.
- The Analytics Dashboard, to measure the impact of the new recommendations.

### Constraints & Risks

**1. Cold start**

New users and new products have no interactions, so collaborative filtering cannot recommend them.

**2. Sparse data**

If users interact with very few products, it is hard to find similar users.

**3. Popularity bias**

The model may keep recommending the same popular products to everyone.

**4. Compute cost**

Training on large interaction data may need more computing resources.

**Example:**

A new product added today has no purchases, so collaborative filtering will never recommend it. This is why the content-based part of the hybrid approach is still needed.

------------------------------------------------------------------------

## Meeting Decisions

The following points were agreed in the meeting:

**1. The feature is important**

Collaborative Filtering is considered an important feature for GoCare, since it helps users discover new products based on what similar users bought.

**2. Not for now**

The feature will not be built at the moment. It can start later, when the number of users becomes very large, since this method needs many users interacting with many products to work well.

<div dir="rtl" style="text-align: right;">
<p><strong>مثال:</strong></p>
<p>لكي يقترح النظام سيروم فيتامين سي على عميلة، يجب أن يجد أولًا عملاء آخرين لديهم ذوق مشابه لذوقها واشتروا هذا السيروم.</p>
<ul>
<li><strong>عندما يكون عدد المستخدمين قليلًا:</strong> يصعب العثور على عملاء متشابهين، لذلك لن تكون الاقتراحات دقيقة.</li>
<li><strong>عندما يصبح عدد المستخدمين كبيرًا جدًا:</strong> يستطيع النظام العثور على عملاء متشابهين بسهولة، وعندها تكون الميزة مفيدة.</li>
</ul>
</div>
