# Advanced Product Recommendations

**Priority:** Medium

## 1. Overview

### The problem

When the user asks the agent for a recommendation, the agent searches products in a simple way. It does not use the recommendation system, so its suggestions are not based on the user's behavior or on what similar users bought.

### What the feature does

The feature lets the agent show smarter recommendations inside the chat, by using the recommendation system:

- **Collaborative filtering based on user behavior:** "Users like you also bought this."
- **Purchase history-based recommendations:** products based on what the user bought before.
- **Context-aware product suggestions:** products based on the situation, such as the time or the weather.
- **Similar product recommendations:** products similar to the one the user is looking at.
- **Frequently bought together suggestions:** products that are often bought together, such as a cleanser and a moisturizer.

### Example

> **User:** Recommend something for me.
>
> **Agent:** Customers who bought the same cleanser as you also liked this moisturizer. Would you like to see it? 😊
>
> **User:** I'm buying this cleanser.
>
> **Agent:** Customers often buy it together with this toner. Would you like to add it to your cart?

## 2. Requirements

### Functional Requirements

- **FR-01: Collaborative filtering:** the agent shows products based on what similar users bought.
- **FR-02: Purchase history recommendations:** the agent suggests products based on the user's past purchases.
- **FR-03: Context-aware suggestions:** the agent adjusts suggestions to the user's situation.
- **FR-04: Similar products:** the agent suggests products similar to the one the user is viewing.
- **FR-05: Frequently bought together:** the agent suggests products that are often bought together.

### Non-Functional Requirements

- **Performance:** recommendations must load quickly inside the chat.
- **Relevance:** recommendations must match what the user is asking for.
- **Fallback:** if the recommendation system is not available, the agent uses normal product search.
- **Consistency:** recommendations in the chat must match the recommendations on the website.

## 3. Assessment

In my view, this feature is useful, but most of its work is in the recommendation system, not in the agent:

- **The agent only shows the results:** the agent asks the recommendation system for suggestions, then shows them in the chat.
- **It overlaps with the recommendation roadmap:** Collaborative Filtering and Context-Aware Recommendations are already planned in the recommendation system, and Context-Aware Recommendations was considered not important at the moment.

So the agent part is to connect the chat to the recommendation system once its features are ready.
