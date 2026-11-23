# Context-Aware Recommendations

## 1. Feature Overview

### The problem

Current recommendations depend on **who the user is**, such as their preferences and history. They do not consider **the user's current situation**, such as the time of day, where they are, or the weather. But beauty and care needs change with these conditions.

### What the feature does

**Context-Aware Recommendations** adjust recommendations based on the user's current context. The roadmap describes three types:

- **Time-based:** recommendations change with the time of day, day of the week, or season.
- **Location-based:** recommendations change with the user's city or area.
- **Weather-aware:** recommendations change with the current weather, such as heat, humidity, or dust.

**Example:**

| Context                | Recommendation                                        |
|------------------------|-------------------------------------------------------|
| Morning                | Sunscreen and day moisturizer                         |
| Evening                | Night cream and makeup remover                        |
| User in Jeddah (humid) | Light, oil-free products                              |
| User in Riyadh (dry)   | Richer moisturizers                                   |
| Very hot day           | Sunscreen with higher protection and cooling products |
| Dusty weather          | Deep cleansers                                        |

In short, the same user may see different recommendations depending on when and where they open GoCare.

## 2. Current Website Status

Based on the review in this report:

- GoCare serves customers in Saudi Arabia, with free shipping on the first order in Riyadh.
- Saudi cities have very different climates, such as humid coastal cities and dry inland cities.
- It is not yet confirmed whether the user's city is stored or detected.
- Smart Salon Services already plans to use the user's location.

**What does this mean for the feature?**

- Location and climate differences in Saudi Arabia make this feature especially relevant.
- The location handling planned for Smart Salon Services can be reused.

## 3. Business Objective

The main goal is to make recommendations feel more timely and relevant, which increases clicks and purchases.

**Expected benefits:**

- **More relevant recommendations:** matching the user's real needs at that moment.
- **Higher conversion:** users are more likely to buy what fits their current situation.
- **Better seasonal and daily planning:** connected to Demand Forecasting.

**Example:**

On a very hot summer day in Riyadh, the homepage highlights high-protection sunscreens and light moisturizers, instead of showing the same products as in winter.

**Priority:** Long-term vision, according to the roadmap.

## 4. Clarification Questions

### 4.1 Questions for the Client

**1. Which context should come first?**

Time, location, or weather?

**2. Where should context-aware recommendations appear?**

Homepage, product pages, notifications, or the chatbot?

**3. How should the user's location be determined?**

From the delivery address, a city selected by the user, or the device location with permission?

**4. Which cities should be supported first?**

### 4.2 Questions for the Backend and Data Team

1.  Is the user's city or delivery address stored?
2.  Can the website use a weather data service?
3.  Are product attributes available to match products with conditions, such as "oil-free" or "high SPF"?
4.  Can the recommendation system accept context as an extra input?

### 4.3 Shared Question for the Client and Data Team

**Which rules connect context to products?**

For example, which products should be prioritized in humid weather or at night? The client agrees on the rules, and the data team confirms that the needed product attributes exist.

## 5. Functional Requirements

**FR-01: Time-based recommendations**

The system must adjust recommendations based on the time of day and season.

**FR-02: Location-based recommendations**

The system must adjust recommendations based on the user's city or area.

**FR-03: Weather-aware recommendations**

The system must adjust recommendations based on current weather conditions in the user's city.

**FR-04: Fallback**

If context is not available, the system must show normal recommendations.

**Proposed additional requirements (need client confirmation):**

- **FR-05:** Explaining the reason, such as "Recommended for today's hot weather".
- **FR-06:** Context-aware notifications, such as a sunscreen reminder on very hot days.
- **FR-07:** Using context in the chatbot.

## 6. Non-Functional Requirements

**1. Performance**

Adding context must not slow down recommendations.

**2. Privacy**

Location must only be used with the user's permission, in line with data protection regulations in Saudi Arabia.

**3. Reliability**

If the weather service fails, normal recommendations must still work.

**4. Relevance**

Context rules must be reviewed to make sure they make sense for users.

## 7. Data Requirements

| Data                          | Purpose                        | Status                                   |
|-------------------------------|--------------------------------|------------------------------------------|
| User City / Location          | Location-based recommendations | Unconfirmed                              |
| Weather Data                  | Weather-aware recommendations  | Not available; needs an external service |
| Time and Date                 | Time-based recommendations     | Available                                |
| Product Attributes            | Match products to conditions   | Exists; completeness needs review        |
| Context Rules                 | Connect conditions to products | Not available; needs to be agreed        |
| Interaction Data with Context | Measure and improve results    | Not collected yet                        |

## 8. Technical Feasibility

The first version can be rule-based:

- Simple rules connect time, city, and weather to product attributes.
- A weather service provides current conditions for the user's city.
- The recommendation system boosts products that match the current context.

Later, Machine Learning models can learn which products perform best in each context, using interaction data.

**Initial assessment:** technically feasible, especially with rule-based logic. It depends on good product attributes and a reliable weather data source.

## 9. Dependencies & Constraints

### Dependencies

- Product attributes, supported by Automated Content Tagging.
- User location handling, shared with Smart Salon Services.
- A weather data service.
- Collaboration between the Data, Backend, and Recommendation teams.

### Constraints & Risks

**1. Location permission**

Many users may not share their location.

**2. Weak rules**

Wrong or obvious rules may make recommendations feel repetitive.

**3. External service cost and reliability**

Weather services may have costs or downtime.

**4. Measuring impact**

It may be hard to prove that context improved results without careful testing.

**Example:**

If the system recommends heavy moisturizers to a user in a humid city only because it is winter, the recommendation will feel wrong, which is why location and weather must be combined with time.

------------------------------------------------------------------------

## Meeting Decisions

The feature is not important at all at the moment.
