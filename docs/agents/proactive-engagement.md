# Proactive Engagement

**Priority:** Medium

## 1. Overview

### The problem

Today, the agent only answers when the user writes first. It does not welcome new users, remind users about things they care about, or bring back users who stopped visiting. This means many sales and engagement opportunities are missed.

### What the feature does

The feature lets the agent start useful conversations at the right time:

- **Welcome messages for new users:** greet new users and show what the agent can do.
- **Re-engagement messages for inactive users:** contact users who have not visited for a while.
- **Proactive product suggestions:** suggest products based on the user's interests and history.
- **Timely reminders and notifications:** remind users about things like reordering or price drops.
- **Abandoned cart reminders:** remind users about products left in their cart.

### Example

> **New user opens the chat:** **Agent:** Welcome to GoCare! 👋 I can help you find products, build a skincare routine, or track your order. What are you looking for today?
>
> **Abandoned cart (next day):** **Agent:** You left a vitamin C serum in your cart. It's still available. Would you like to complete your order?
>
> **Reorder reminder:** **Agent:** It's been about two months since you bought your sunscreen. Would you like to reorder it?

## 2. Why It Matters

- **Better first impression:** new users quickly understand how to use the agent.
- **Recover lost sales:** abandoned cart reminders bring users back to complete orders.
- **Repeat purchases:** reorder reminders encourage users to buy again.
- **Bring back inactive users:** re-engagement messages reduce customer loss.

## 3. Requirements

### Functional Requirements

- **FR-01: Welcome messages:** new users receive a welcome message with examples of what the agent can do.
- **FR-02: Re-engagement messages:** inactive users receive a message after a set period of inactivity.
- **FR-03: Proactive product suggestions:** the agent suggests products based on the user's interests and history.
- **FR-04: Timely reminders and notifications:** the agent sends reminders, such as reorder reminders and price drop alerts.
- **FR-05: Abandoned cart reminders:** users with items left in the cart receive a reminder.

### Non-Functional Requirements

- **User control:** users can choose which messages they receive, and can turn them off.
- **Frequency limits:** users must not receive too many proactive messages.
- **Privacy & Compliance:** messages follow user consent and marketing regulations in Saudi Arabia.
- **Relevance:** messages must be useful, not generic spam.

## 4. Technical Approach

- **Event triggers:** define events that start a proactive message, such as first visit, cart left for 24 hours, no visit for 30 days, or time to reorder.
- **Scheduler:** a background job checks these conditions and creates messages.
- **Message templates:** prepare templates in Arabic and English, personalized with the user's name and products.
- **Delivery channels:** messages appear in the chat when the user returns, or are sent as notifications, depending on what GoCare supports.
- **Preferences check:** check User Preferences & Settings before sending any message.
- **Recommendation integration:** use the recommendation system for proactive product suggestions.
- **Link to other features:** coordinate with Churn Prediction and Personalized Marketing in the recommendation roadmap, to avoid sending the same user too many messages from different systems.
