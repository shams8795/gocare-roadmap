# Smart Salon Services

## 1. Feature Overview

**Smart Salon Services** aims to help GoCare users easily find suitable salon services, instead of manually searching through a large number of salons and services.

The recommendation system relies on three main factors:

- **User preferences:** e.g. interest in hair care or skin care services.
- **Booking history:** services the user has previously booked through GoCare.
- **Location:** suggesting services at salons near the user.

Recommendations are also linked to the booking system already on the website, making it easy to book the suggested services.

**Example:**

If a user is interested in hair care, has booked a **Hair Spa** service twice, and lives in Al Olaya, Riyadh, the system may suggest a **Hair Treatment** service at a nearby salon.

## 2. Current Website Status

Based on the review in this report:

- GoCare has a salons section for searching salons and booking their services, with 43 salons at the time of review.
- Salons are grouped into 12 categories.
- Each salon shows its operating status (open or closed), as well as a ratings section.
- The ratings feature exists, but almost all salons had no ratings at the time of review.
- The website combines a beauty products store with a salon booking system.

**What does this mean for the feature?**

- The booking system already exists; the task is to integrate with it rather than build a new one.
- The existing service categories can be used to generate recommendations.
- Ratings data is currently not enough to rely on.
- Having the store and salons on one platform allows cross-recommendations between products and services in the future.

## 3. Business Objective

The main goal is to help users reach salon services that fit their needs, improve the GoCare experience, and increase booking completion.

**Expected benefits:**

- Less time spent searching for services.
- Higher likelihood of booking recommended services.
- Encouraging users to return to GoCare.
- Helping salons reach customers interested in their services.

**Example:**

Instead of browsing 43 salons, the system can show three services related to the user's interests and location, making it easier to choose a service and complete the booking.

**Business Impact:** High, according to the client's assessment.

## 4. Client Clarification Questions

### 4.1 Questions for the Client

**1. Where will recommendations appear?**

On the homepage, the salons page, inside a specific salon's page, or during search?

**2. Do price, salon status, and offers affect recommendations?**

For example, should we recommend services at salons that are currently closed? Should discounted services get priority?

**3. What happens when a recommendation is clicked?**

Does the user go to the salon page, or directly to the booking process?

### 4.2 Questions for the Backend and Data Team

1.  Does the current booking system provide an API that the recommendation system can use?
2.  Is users' booking history stored and accessible?
3.  Are salon locations stored as geographic coordinates, or only by city and area names?
4.  Is available booking slot data stored and accessible?
5.  Is every service linked to its correct category?

### 4.3 Shared Question for the Client and Data Team

**What exactly counts as user preferences and activity history?**

Should recommendations rely on past bookings only, or also include searches, salons the user viewed, favorites, and product purchases?

The data team must also confirm that this information is actually recorded in GoCare.

## 5. Functional Requirements

The functions the recommendation system must be able to perform.

**FR-01: Recommendations based on user preferences**

The system must suggest services related to the user's recorded interests.

*Example:* if the user is interested in hair care, the system can suggest Hair Spa and Hair Treatment.

**FR-02: Use of booking history**

The system must take services the user previously booked into account when ranking recommendations.

*Example:* if the user has booked Hair Spa more than once, hair care services may get higher priority.

**FR-03: Location-based recommendations**

The system must provide recommendations based on the location the user enters herself.

*Example:* if the user selects Al Olaya in Riyadh, salons in or near that district can be prioritized.

**FR-04: Integration with the booking system**

Recommended services must be linked to GoCare's current booking system.

*Example:* the user clicks a recommended Hair Spa service, views its details, and picks an available time slot.

**FR-05: Recommendations for new users**

Users with no booking history must receive general salon recommendations.

**Proposed additional requirements (need client confirmation):**

- **FR-06:** Show recommended service details, such as price, salon name, location, and operating status.
- **FR-07:** Do not show cancelled or non-bookable services as available.
- **FR-08:** Support future cross-recommendations between store products and salon services.

## 6. Non-Functional Requirements

**1. Performance**

Recommendations must load at a suitable speed without affecting website performance.

*Example:* loading recommendations must not delay the homepage content from appearing.

**2. Scalability**

The system must handle growth in users, salons, and services without significant performance degradation.

**3. Reliability**

A failure in the recommendation system must not stop the website's core functions.

*Example:* if recommendations fail, the user can still search for salons and complete bookings.

**4. Privacy & Security**

User data, especially booking history and location, must be protected and used according to the appropriate permissions and consent, in line with data protection regulations in Saudi Arabia.

**5. Recommendation Quality**

The relevance of recommended services to user interests must be evaluated, and result quality improved.

*Note: target values for response time, availability, and concurrent users must be defined with the technical team.*

## 7. Data Requirements

| Data                     | Purpose                                                 | Status                                                     |
|--------------------------|---------------------------------------------------------|------------------------------------------------------------|
| User Preferences         | Know the user's interests                               | Unconfirmed                                                |
| Booking History          | Know which services the user booked before              | Unconfirmed                                                |
| Service Catalog          | Know which services can be recommended                  | Visible on the website; needs review                       |
| Service Categories       | Identify similar services                               | Available                                                  |
| Salon Locations          | Suggest nearby salons when the user enters her location | Storage method unconfirmed                                 |
| Service Availability     | Confirm the service can be booked                       | Unconfirmed                                                |
| Prices & Promotions      | Consider prices and discounts                           | Unconfirmed                                                |
| User Ratings             | Improve recommendation quality                          | Not enough ratings currently                               |
| Product Purchase History | Cross-recommendations between the store and salons      | Reported as available in the product recommendation system |

**Example:**

If the system knows the user is interested in hair care, but services are not correctly linked to their categories, it cannot reliably identify Hair Care services.

Therefore, the data must be reviewed and confirmed complete before choosing how to build the recommendation system.

## 8. Technical Feasibility

The first version can be built as a **Rule-Based Recommendation System** using a set of simple rules, without the need for complex Machine Learning models.

**Example rules:**

- Prioritize services related to the user's interests.
- Use the user's previous booking history.
- Prefer salons close to the user.
- Exclude services that cannot be booked.

As more data becomes available, more advanced approaches can be tested, such as:

- **Content-Based Filtering:** recommending services similar to the user's interests.
- **Collaborative Filtering:** using behavior patterns of similar users.

Reusing the current product recommendation system can also be studied, if some of its components are reusable.

**Initial assessment:** the feature is technically feasible in principle, provided that data availability and integration with the booking system are confirmed.

## 9. Dependencies & Constraints

### Dependencies

- Availability of user and service data.
- An API for integrating with the current booking system.
- Availability of salon location data.
- Collaboration between the Backend, Frontend, and Recommendation teams.
- Coordination with the AI Agent team, since the chatbot can use the recommendation system to suggest services during conversations.

### Constraints & Risks

**1. Sparse data**

New users may have no booking history, and the ratings currently available are not enough.

**2. Incomplete service data**

Some services may be missing important information such as price, category, or location.

**3. Slot availability**

A service may suit the user, but have no available slots to book.

**4. Location privacy**

Some users may not enter their location.

**Example:**

If a salon's exact location is not available, the system cannot calculate the distance between it and the user. In this case, the city or area can be used instead of distance, as agreed.

------------------------------------------------------------------------

## Meeting Decisions

The following points were agreed in the meeting:

- **Recommend services, not salons:** by default, the system recommends salon services, such as Hair Spa or Hair Treatment, instead of recommending whole salons.
- **Salon recommendations when location is entered:** if the user enters her location herself, the system can also recommend nearby salons that offer these services.
- **New users:** users with no booking history receive general salon recommendations.
- **Number of recommendations:** the system shows 3 recommendations.

<div dir="rtl" style="text-align: right;">
<p><strong>مثال:</strong></p>
<p>مستخدمة مهتمة بالعناية بالشعر، وسبق لها حجز خدمة <bdi>Hair Spa</bdi>.</p>
<ul>
<li><strong>إذا لم تُدخل موقعها:</strong> تظهر لها الخدمات المقترحة فقط، مثل <bdi>Hair Treatment</bdi> و<bdi>Hair Spa</bdi>.</li>
<li><strong>إذا أدخلت موقعها بنفسها:</strong> تظهر لها أيضًا الصالونات القريبة التي تقدم هذه الخدمات، مثل <bdi>Salon A</bdi> – العليا – على بُعد كيلومترين.</li>
</ul>
</div>
