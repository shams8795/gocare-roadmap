# Social Recommendations

## 1. Feature Overview

### The problem

Many beauty purchases are influenced by other people: influencers on social media, friends, and family. However, GoCare's recommendations today are based only on the user's own behavior and on product attributes, not on the people the user trusts.

### What the feature does

**Social Recommendations** recommend products based on people. The roadmap describes two types:

- **Influencer suggestions:** showing products used or recommended by beauty influencers.
- **Friend-based recommendations:** showing products that the user's friends bought or liked, with their permission.

**Example:**

| Type                         | What the user sees                                              |
|------------------------------|-----------------------------------------------------------------|
| Influencer suggestions       | "Products used by \[influencer name\] in her skin care routine" |
| Friend-based recommendations | "Your friend Sara added this serum to her favorites"            |

In short, the feature adds a social layer to recommendations, based on trust in real people.

## 2. Current Website Status

Based on the review in this report:

- GoCare has user accounts and a favorites (wishlist) feature.
- There is no friends or followers system on the website.
- It is not yet confirmed whether GoCare works with influencers or has influencer partnerships.

**What does this mean for the feature?**

- Friend-based recommendations need a new social system, which is a large change.
- Influencer suggestions may be simpler to start with, if GoCare has influencer partnerships.

## 3. Business Objective

The main goal is to increase trust and sales by using recommendations from people that users trust.

**Expected benefits:**

- **More trust:** users trust products recommended by people they follow.
- **Higher conversion:** influencer and friend recommendations often lead to purchases.
- **Marketing value:** influencer collections can be part of marketing campaigns.
- **Engagement:** users may return to see what friends and influencers like.

**Example:**

An influencer collection page showing her full skin care routine can drive many sales during a campaign.

**Priority:** Long-term vision, according to the roadmap.

## 4. Clarification Questions

### 4.1 Questions for the Client

**1. Does GoCare work with influencers?**

Are there existing partnerships, and can influencers create their own product lists?

**2. Should there be a friends or followers system?**

Is this part of GoCare's long-term plan?

**3. Which should come first?**

Influencer suggestions or friend-based recommendations?

**4. How should privacy work?**

Should users choose to share their purchases or favorites, or should everything be private by default?

### 4.2 Questions for the Backend and Data Team

1.  Can new data such as influencer lists and friend connections be stored?
2.  Is there a way to link social media accounts?
3.  Are favorites and purchases stored in a way that can be shared with permission?

### 4.3 Shared Question for the Client and Data Team

**What can be shared, and with whom?**

The client decides the privacy rules, and the data team confirms how to store and enforce them.

## 5. Functional Requirements

**FR-01: Influencer collections**

The system must allow showing product lists recommended by influencers.

**FR-02: Influencer-based recommendations**

The system must recommend influencer products to users interested in similar products.

**FR-03: Friend connections**

The system must allow users to connect with friends, with their consent.

**FR-04: Friend-based recommendations**

The system must show products that friends chose to share, such as favorites or purchases.

**Proposed additional requirements (need client confirmation):**

- **FR-05:** Privacy settings for what each user shares.
- **FR-06:** Tracking sales from influencer collections.
- **FR-07:** Influencer discount codes connected to their collections.

## 6. Non-Functional Requirements

**1. Privacy**

Nothing about a user's purchases or favorites must be shown to others without clear consent, in line with data protection regulations in Saudi Arabia.

**2. Transparency**

Paid influencer recommendations must be clearly marked as advertising.

**3. Performance**

Social recommendations must not slow down the website.

**4. Moderation**

Shared content must be reviewable to prevent misuse.

## 7. Data Requirements

| Data                     | Purpose                           | Status                 |
|--------------------------|-----------------------------------|------------------------|
| Influencer Product Lists | Influencer suggestions            | Not available          |
| Influencer Partnerships  | Know which influencers to include | Unconfirmed            |
| Friend Connections       | Friend-based recommendations      | Not available          |
| User Sharing Consent     | Respect privacy                   | Not available          |
| Favorites & Purchases    | Content to share                  | Available, but private |

## 8. Technical Feasibility

- **Influencer suggestions** are relatively simple: influencer product lists can be stored and shown as collections, and recommended to users with similar interests.
- **Friend-based recommendations** require a new social system: friend connections, privacy settings, and sharing controls.

**Initial assessment:** influencer suggestions are technically feasible with limited effort. Friend-based recommendations are feasible but require a large product and privacy design effort.

## 9. Dependencies & Constraints

### Dependencies

- Influencer partnerships and content.
- A social system and privacy design for friend-based recommendations.
- Collaboration with the marketing team.
- Collaboration between the Backend, Frontend, and Recommendation teams.

### Constraints & Risks

**1. Privacy concerns**

Users may not want others to know what they buy, especially personal care products.

**2. Small social network**

Friend-based recommendations only work if many users connect with friends.

**3. Advertising rules**

Paid influencer content must follow advertising regulations.

**4. Influencer reliability**

An influencer's reputation can affect GoCare's brand.

**Example:**

If a user's purchase of a personal care product is shown to their friends without clear consent, it can seriously damage trust in GoCare.

------------------------------------------------------------------------

## Meeting Decisions

The following points were agreed in the meeting:

**1. Important, but not a high priority**

Social Recommendations is considered important, but not very important at the moment.

**2. Monthly viral products by the marketing team**

Instead of building influencer or friend systems, the marketing team will search every month for products that are viral on social media, and add them to the website. The list is updated every month.

<div dir="rtl" style="text-align: right;">
<p><strong>مثال:</strong></p>
<p>في بداية كل شهر، يبحث فريق التسويق في مواقع التواصل الاجتماعي عن منتجات التجميل الرائجة.</p>
<ul>
<li><strong>ما يجده الفريق:</strong> مثلًا، سيروم معيّن ينتشر بشكل واسع على تيك توك وإنستغرام هذا الشهر.</li>
<li><strong>ما يفعله الفريق:</strong> يضيفه إلى قسم «الأكثر رواجًا هذا الشهر» في موقع <bdi>GoCare</bdi>، لكي يجده العملاء ويشتروه بسهولة.</li>
<li><strong>في الشهر التالي:</strong> يحدّث الفريق القائمة بالمنتجات الرائجة الجديدة.</li>
</ul>
</div>
