# Skincare Routine Advisor

## 1. Feature Overview

**Skincare Routine Advisor** aims to help GoCare users build a complete skin care, hair care, or body care routine from the store's products, based on their skin, hair, or body care needs, instead of choosing products one by one without knowing what fits together.

The feature has three main parts:

- **Routine builder:** suggesting the right products for each routine step based on the user's skin or hair type and concerns (e.g. cleanser, serum, moisturizer, and sunscreen for skin; shampoo, conditioner, mask, and serum for hair).
- **Product sequencing:** showing the correct order of use, separating morning and night steps where relevant, and avoiding products that should not be used together.
- **Seasonal adjustments:** adapting the routine to the season, such as a lighter moisturizer and stronger sunscreen in summer, or more hydrating hair products in winter.

**Examples:**

- If a user has oily, acne-prone skin, the system may suggest a morning routine of a gel cleanser, a niacinamide serum, a light gel moisturizer, and an oil-free SPF 50 sunscreen.
- If a user has dry, frizzy hair, the system may suggest a moisturizing shampoo, a deep conditioner, a weekly hair mask, and an anti-frizz serum.

All suggested products come from GoCare's store.

The feature is offered through the chatbot: the AI Agent asks the user which routine she wants (skin, hair, or body care), asks about her type and concerns, and presents the routine within the conversation.

Product selection is handled by the recommendation system.

## 2. Current Website Status

Based on the review in this report:

- GoCare's store includes product categories such as skin care, hair care, makeup, personal care, body care, men's care, and beauty devices.
- Products are already tagged with their routine step (e.g. cleanser, serum, shampoo). It is not yet confirmed whether they are tagged with skin or hair type and key ingredients.
- The existing product recommendation system can already suggest related products.
- The AI Agent team already has ongoing work related to routines in the chatbot.

**What does this mean for the feature?**

- The products needed for skin, hair, and body care routines already exist in the store.
- The main question is whether product data is detailed enough to build reliable routines.
- Part of the logic may already exist or be planned in the AI Agent work, so scope must be aligned before starting.

## 3. Business Objective

The main goal is to help users choose the right products for their skin or hair, increase confidence in their purchases, and increase the number of products bought together.

**Expected benefits:**

- Easier product selection for users who don't know what fits their skin or hair.
- Higher average order value, since users buy a full routine instead of a single product.
- Encouraging repeat purchases when routine products run out.
- Building trust in GoCare as a source of beauty advice.

**Example:**

Instead of buying a shampoo only, the user sees a full hair routine for their hair type and adds three or four matching products to the cart in one step.

**Business Impact:** High, according to the client's assessment.

## 4. Functional Requirements

The functions the system must be able to perform.

**FR-01: Choose routine type**

The chatbot must first ask the user which routine she wants: skin care, hair care, or body care.

*Example:* the chatbot asks "Which routine are you looking for?" with three options: skin, hair, or body care.

**FR-02: Collect skin, hair, or body care profile**

Based on the chosen routine type, the system must collect the user's skin type, hair type, or body care needs, and her main concerns.

*Example:* for skin, the user selects "oily" and "acne"; for hair, the user selects "dry" and "frizz".

**FR-03: Build a routine based on the profile**

The system must define the routine steps that fit the user's profile.

*Example:* oily skin gets a morning routine of cleanser, serum, light moisturizer, and sunscreen; dry hair gets a routine of moisturizing shampoo, conditioner, and a weekly mask.

**FR-04: Recommend products for each step**

The system must suggest suitable, in-stock store products for each routine step.

*Example:* for the shampoo step, the system suggests a moisturizing shampoo tagged for dry hair.

**FR-05: Product sequencing**

The system must show products in the correct order of use and avoid combining products that should not be used together.

*Example:* the system does not place two strong exfoliating products in the same skin routine.

**FR-06: Seasonal adjustments**

The system must adjust routine recommendations according to the season.

*Example:* in summer, the system prefers lighter moisturizers and higher SPF sunscreens; in winter, more hydrating hair products.

**FR-07: Routine API for the chatbot**

The recommendation system must provide an API that the AI Agent can use to get routine products during conversations.

**Proposed additional requirements (need client confirmation):**

- **FR-08:** "Add full routine to cart" button.
- **FR-09:** "Complete your routine" section on product pages and in the cart.
- **FR-10:** Saving the user's skin and hair profiles in their account for future recommendations.
- **FR-11:** A clear disclaimer that recommendations are cosmetic advice, not medical advice.

## 5. Non-Functional Requirements

**1. Performance**

Routine results must appear quickly in the chatbot after the user answers the questions.

*Example:* the routine appears in the conversation without a noticeable delay after the last answer.

**2. Reliability**

If the routine service fails, the rest of the store must keep working normally.

*Example:* product pages still load even if the "complete your routine" section is unavailable.

**3. Safety & Responsibility**

Recommendations must stay within cosmetic advice, avoid medical claims, and show a disclaimer where needed.

**4. Privacy & Security**

Skin and hair profile data must be stored and used only with the user's consent, in line with data protection regulations in Saudi Arabia.

**5. Recommendation Quality**

Routine rules and product matches must be reviewed for accuracy through a medical consultation before launch.

*Note: target values for response time and recommendation accuracy must be defined with the technical team.*

## 6. Data Requirements

| Data                         | Purpose                                                          | Status                                                                                                    |
|------------------------------|------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Product Catalog              | Know which products can be recommended                           | Exists in the store                                                                                       |
| Product Categories           | Group products by type                                           | Exists on the website                                                                                     |
| Skin / Hair Type per Product | Match products to user profiles                                  | Unconfirmed                                                                                               |
| Ingredients                  | Check product conflicts                                          | Unconfirmed (structured or free text?)                                                                    |
| Routine Step per Product     | Place each product in the right step                             | Available                                                                                                 |
| Stock Availability           | Avoid recommending unavailable products                          | Unconfirmed                                                                                               |
| Routine Rules                | Define steps, order, and conflicts for skin, hair, and body care | Based on common skincare rules (from lightest to heaviest); to be reviewed through a medical consultation |
| User Skin / Hair Profile     | Personalize routines                                             | Not collected yet                                                                                         |
| Purchase History (optional)  | Improve recommendations and suggest refills                      | Available in the product recommendation system                                                            |

**Example:**

If products are not tagged with hair type, the system cannot tell whether a shampoo is suitable for dry or oily hair, and the routine would be unreliable.

Therefore, product data must be reviewed first, and missing attributes added before building the feature.

## 7. Technical Feasibility

The first version can be built as a **Rule-Based Recommendation System**:

- A routine template for each skin type, hair type, and body care need defines the required steps.
- Products are filtered by skin or hair type, routine step, and stock.
- Conflict rules remove products that should not be used together.
- Products are ranked by sales, ratings, or price range.
- Seasonal rules adjust the routine based on the current month.

The same logic is exposed as an API, so it can be used by the AI Agent and at checkout.

Later, more advanced approaches can be tested, such as:

- **Content-Based Filtering:** matching products to users based on product attributes.
- **Collaborative Filtering:** suggesting products bought by users with similar profiles.

**Initial assessment:** feasibility depends mainly on product data quality. If products are tagged with skin or hair type, ingredients, and routine step, the feature is technically feasible. If not, data preparation will be the largest part of the work.

## 8. Dependencies & Constraints

### Dependencies

- Product data with skin or hair type and ingredients (routine step is already available).
- Common skincare rules for the order of use (from lightest to heaviest), reviewed through a medical consultation.
- Alignment with the AI Agent team on the existing routine work.
- Collaboration between the Backend, Frontend, Data, and Recommendation teams.

### Constraints & Risks

**1. Incomplete product data**

Many products may be missing skin or hair type or ingredients information.

**2. Accuracy of routine rules**

Wrong combinations or order of use could harm user trust or cause skin or scalp irritation.

**3. Medical boundary**

Users may describe skin or scalp conditions that need a doctor, not product recommendations.

**4. Overlap with existing work**

Building the same logic twice in the chatbot and the recommendation system wastes effort and may give users different answers.

**Example:**

If the chatbot shows one order of use and the checkout shows another for the same user, users will lose trust in both. This is why both must use the same recommendation logic.

------------------------------------------------------------------------

## Meeting Decisions

The following points were agreed in the meeting:

**1. The routine is built in the chatbot**

The routine feature will be offered through the chatbot. The AI Agent asks the user about her needs and presents the routine in the conversation, while the recommendation system selects the products for each step.

**2. Routines cover skin care, hair care, and body care**

In addition to skin care and hair care, the feature will also support body care routines.

**3. Order of use for all routine types**

The system shows the correct order of use for skin care, hair care, and body care products.

| Routine type | Order of use                                   |
|--------------|------------------------------------------------|
| Skin care    | Cleanser, toner, serum, moisturizer, sunscreen |
| Hair care    | Shampoo, conditioner, mask, serum              |
| Body care    | Shower gel, scrub, body lotion                 |

**4. Order of use appears in two places**

- **In the chatbot:** when the user asks how to use her products, or in which order, the chatbot shows the correct order of use.
- **At checkout (if the cost is low):** a small "How to use your products" card lists the products in the user's cart in the correct order of use.

Rules for both places:

- The checkout card is for information only, and must not block or slow down the checkout.
- The order of use can also be shown on the order confirmation page or in the order email.
- Products without a known routine step are shown at the end, instead of being placed in the wrong order.
- The chatbot and checkout must use the same ordering rules, so the user always sees the same order.

<div dir="rtl" style="text-align: right;">
<p><strong>مثال:</strong></p>
<p>مستخدمة لديها في سلة التسوق واقي شمس، وغسول، وسيروم، وشامبو.</p>
<ul>
<li><strong>في روبوت المحادثة:</strong> تسأل بأي ترتيب يجب أن تستخدم هذه المنتجات، فيرد عليها روبوت المحادثة بالترتيب الصحيح.</li>
<li><strong>عند إتمام الطلب:</strong> تظهر لها بطاقة بعنوان <strong>طريقة استخدام منتجاتك</strong> تحتوي على:
      <ul>
<li><strong>العناية بالبشرة:</strong>
<ol>
<li>الغسول</li>
<li>السيروم</li>
<li>واقي الشمس</li>
</ol>
</li>
<li><strong>العناية بالشعر:</strong>
<ol>
<li>الشامبو</li>
</ol>
</li>
</ul>
</li>
</ul>
</div>

**5. Product data is ready**

All products are already tagged with their type (e.g. cleanser, serum, shampoo), so the system can order them directly without extra data preparation.

**6. Quiz-style questions in the chatbot**

The user provides her routine type and profile by answering short quiz-style questions inside the chatbot. The chatbot asks one question at a time, and the user chooses from ready options.

<div dir="rtl" style="text-align: right;">
<p><strong>مثال:</strong></p>
<p>مستخدمة تطلب روتينًا من روبوت المحادثة:</p>
<ul>
<li><strong>السؤال الأول:</strong> ما نوع الروتين الذي تبحثين عنه؟ تختار: البشرة.</li>
<li><strong>السؤال الثاني:</strong> ما نوع بشرتك؟ تختار: دهنية.</li>
<li><strong>السؤال الثالث:</strong> ما مشكلتك الرئيسية؟ تختار: حب الشباب.</li>
<li><strong>النتيجة:</strong> يعرض لها روبوت المحادثة روتينًا كاملًا للعناية بالبشرة.</li>
</ul>
</div>

**7. Routine rules follow common skincare knowledge, reviewed by a medical consultation**

The routine rules follow common, well-known skincare rules. The main rule for skin care is to apply products from the lightest to the heaviest texture. Before launch, these rules will be reviewed through a medical consultation, to make sure they are correct and safe.

<div dir="rtl" style="text-align: right;">
<p><strong>مثال:</strong></p>
<p>ترتيب استخدام منتجات البشرة من الأخف إلى الأثقل:</p>
<ul>
<li><strong>التونر:</strong> هو الأخف، مثل الماء، لذلك يأتي أولًا.</li>
<li><strong>السيروم:</strong> يأتي بعده، وهو أكثف قليلًا.</li>
<li><strong>المرطب:</strong> يأتي في النهاية، وهو الأثقل.</li>
</ul>
</div>
