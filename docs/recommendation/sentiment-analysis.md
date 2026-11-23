# Sentiment Analysis

## 1. Feature Overview

### The problem

Customers leave reviews and comments on GoCare products and services, in Arabic and English. For example:

> "The cream is very good and the texture is light."
>
> "Caused redness on my skin after two days."
>
> "الكريم حلو بس العبوة وصلت مكسورة"

When there are only a few reviews, the team can read them one by one. When there are thousands, it becomes impossible to read them all, and real problems with a product can be missed until they become serious.

### What the feature does

**Sentiment Analysis** reads customer reviews and feedback automatically and:

- **Detects the sentiment** of each review: positive, negative, or neutral.
- **Detects the topic** of the review, such as quality, side effects, packaging, delivery, price, or scent.
- **Highlights product issues** by grouping negative reviews about the same problem and alerting the team.

For the reviews above, the system produces:

| Review                                           | Sentiment | Topic                                            |
|--------------------------------------------------|-----------|--------------------------------------------------|
| The cream is very good and the texture is light. | Positive  | Product quality                                  |
| Caused redness on my skin after two days.        | Negative  | Side effects                                     |
| الكريم حلو بس العبوة وصلت مكسورة                 | Mixed     | Product quality (positive), packaging (negative) |

In short:

- **Input:** customer reviews and feedback (free text).
- **Output:** sentiment and topic for each review, plus alerts for repeated problems.
- **Result:** the team finds product issues early, before they affect many customers.

### Why Arabic and English

GoCare customers write in Arabic, English, or a mix of both, and Arabic reviews are often written in dialect (e.g. Saudi or Egyptian) rather than formal Arabic. The system must understand all of these.

## 2. Current Website Status

Based on the review in this report:

- GoCare has a ratings feature, shown on salons and products.
- Almost all salons had no ratings at the time of review.
- It is not yet confirmed how many product reviews and comments exist.
- It is not yet confirmed whether other feedback sources exist, such as customer service messages, chatbot conversations, or return reasons.

**What does this mean for the feature?**

- The feature depends on having enough reviews and feedback to analyze.
- If product reviews are few, other feedback sources, such as chatbot conversations and return reasons, may be more useful at the start.

## 3. Business Objective

The main goal is to discover product and service problems early, and understand what customers like and dislike, without reading every review manually.

**Expected benefits:**

- **Early problem detection:** spotting issues, such as a batch of damaged products or a product causing irritation, before they spread.
- **Better product decisions:** knowing which products customers love and which ones they complain about.
- **Better customer service:** responding quickly to negative feedback.
- **Better recommendations:** avoiding recommending products with many recent complaints.

**Example:**

If many reviews of the same moisturizer mention "redness" or "irritation" in one week, the system alerts the team, who can check the product or contact the supplier quickly.

**Business Impact:** Moderate, according to the client's assessment.

## 4. Client Clarification Questions

### 4.1 Questions for the Backend and Data Team

1.  How many product reviews and comments are stored, and in which languages?
2.  Are reviews linked to the product, the seller, and the order date?
3.  Are other feedback sources stored, such as chatbot conversations or return reasons?
4.  Are star ratings stored together with the review text?
5.  Can results be stored and shown in the Analytics Dashboard?

## 5. Functional Requirements

**FR-01: Sentiment detection**

The system must classify each review as positive, negative, neutral, or mixed.

*Example:* "Caused redness on my skin" is classified as negative.

**FR-02: Topic detection**

The system must identify what each review is about.

*Example:* "The bottle arrived broken" is about packaging.

**FR-03: Arabic and English support**

The system must understand reviews in Arabic, English, or a mix of both, including common dialect words.

*Example:* "حلو جدًا" and "very nice" are both classified as positive.

**FR-04: Product issue alerts**

The system must alert the team when negative reviews about the same problem increase for a product.

*Example:* five reviews mentioning irritation for the same product within one week trigger an alert.

**FR-05: Results in the Analytics Dashboard**

The analysis results must be shown in the Analytics Dashboard, inside the existing Admin Dashboard.

**Proposed additional requirements (need client confirmation):**

- **FR-06:** A summary per product showing its main strengths and complaints.
- **FR-07:** Analysis of chatbot conversations and return reasons.
- **FR-08:** Sharing product feedback summaries with sellers and brands.

## 6. Non-Functional Requirements

**1. Accuracy**

Sentiment and topic results must be accurate enough to trust, and accuracy must be measured on a set of manually labeled reviews.

**2. Dialect Support**

The system must handle Arabic dialects and mixed Arabic and English, not only formal Arabic.

**3. Timeliness**

New reviews must be analyzed quickly enough for alerts to be useful, for example daily.

**4. Privacy & Security**

Customer names and personal information in reviews must be protected, in line with data protection regulations in Saudi Arabia.

**5. Reliability**

If the analysis service fails, reviews must still be saved and shown on the website normally.

*Note: target values for accuracy and analysis frequency must be defined with the technical team.*

## 7. Data Requirements

| Data                                   | Purpose                          | Status                              |
|----------------------------------------|----------------------------------|-------------------------------------|
| Product Reviews & Comments             | Main input for analysis          | Unconfirmed (amount unknown)        |
| Star Ratings                           | Support sentiment detection      | Feature exists; amount unconfirmed  |
| Salon Reviews                          | Analyze salon feedback           | No ratings yet                      |
| Review Details (product, seller, date) | Group issues by product and time | Unconfirmed                         |
| Chatbot Conversations (optional)       | Extra feedback source            | Unconfirmed                         |
| Return Reasons (optional)              | Extra feedback source            | Unconfirmed                         |
| Manually Labeled Reviews               | Test and measure accuracy        | Not available; needs to be prepared |

**Example:**

If a product has a 5-star rating but the text says "the bottle arrived broken", the star rating alone hides a packaging problem. This is why the review text must be analyzed, not only the stars.

## 8. Technical Feasibility

The first version can use existing language models:

- **Multilingual sentiment models:** pre-trained models that support Arabic and English.
- **Large Language Models (LLMs):** reading each review and returning its sentiment and topic, choosing from a fixed list of topics.
- **Simple alert rules:** for example, an alert when negative reviews about the same topic for one product exceed a set number within a week.

Later, the system can be improved by:

- Fine-tuning a model on GoCare's own labeled reviews, including local dialects.
- Automatic summaries of the main complaints per product.

**Initial assessment:** technically feasible with current multilingual models. The main questions are whether there are enough reviews, and how well the models handle local dialects.

## 9. Dependencies & Constraints

### Dependencies

- Enough customer reviews and feedback.
- Reviews linked to products, sellers, and dates.
- An agreed list of topics to detect.
- A set of manually labeled reviews to measure accuracy.
- Collaboration between the Data, Backend, and Recommendation teams, and the product and customer service teams.
- Coordination with the Analytics Dashboard feature, which can display the results.

### Constraints & Risks

**1. Few reviews**

If most products have few or no reviews, the analysis will have limited value at the start.

**2. Dialects and mixed language**

Reviews may use dialect words, spelling mistakes, emojis, or a mix of Arabic and English.

**3. Sarcasm and mixed opinions**

Some reviews are sarcastic, or praise one aspect and criticize another, which is harder to classify.

**4. Fake or spam reviews**

Fake positive or negative reviews can distort the results.

**Example:**

The review "تحفة، استخدمته يومين وطلعلي حبوب" uses a positive word ("تحفة") sarcastically, while the real meaning is negative. Simple models may classify it wrongly, which is why accuracy must be tested on real GoCare reviews.

------------------------------------------------------------------------

## Meeting Decisions

The following points were agreed in the meeting:

**1. The feature is important**

Sentiment Analysis is considered an important feature for GoCare, since it helps the team discover product problems early and understand what customers like and dislike.

**2. Not for now**

The feature will not be built at the moment, because there is currently not a large number of customer reviews to analyze. It stays in the plan, and can start when the number of reviews increases.

**3. Source: comments on the website**

The analysis uses the customer comments written on the GoCare website.

**4. Focus on negative feedback**

The feature focuses on all negative comments, to find product problems and complaints.

**5. Results shown in the Analytics Dashboard**

The analysis results are shown in the Analytics Dashboard, inside the existing Admin Dashboard.

<div dir="rtl" style="text-align: right;">
<p><strong>مثال:</strong></p>
<p>يريد الفريق معرفة رأي العملاء في المنتجات من خلال تقييماتهم.</p>
<ul>
<li><strong>إذا كان للمنتج ثلاثة تقييمات فقط:</strong> يستطيع الفريق قراءتها بسهولة بنفسه، فلا حاجة إلى تحليل تلقائي.</li>
<li><strong>عندما يحتوي الموقع على آلاف التقييمات:</strong> تصبح قراءتها كلها مستحيلة، وعندها تكون الميزة مفيدة.</li>
</ul>
</div>
