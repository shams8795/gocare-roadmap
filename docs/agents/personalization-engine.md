# Personalization Engine

**Priority:** Medium · **Effort:** High

## 1. Overview

### The problem

Even with memory and saved preferences, the agent still answers every user in the same general way. It does not adapt its greeting, its content, or its tone to who the user is, how they behave, or what time it is.

### What the feature does

The Personalization Engine adapts the agent's responses to each user:

- **Personalized greetings and responses:** greeting returning users by name, and referring to their recent activity.
- **Behavior-based content adaptation:** adapting answers based on what the user usually browses or buys.
- **Time-of-day awareness:** adapting suggestions to the time of day, such as morning or night routines.
- **User journey tracking:** knowing where the user is in their shopping journey (e.g. new visitor, browsing, comparing, returning customer).
- **Adaptive response tone:** adapting the tone and length of answers to the user's style.

### Example

> **Morning, returning user:** **Agent:** Good morning, Sara! Your sunscreen from last month may be running low. Would you like to reorder it?
>
> **Night, new user:** **Agent:** Welcome to GoCare! Are you looking for anything for your night routine?

## 2. Why It Matters

- **Better engagement:** personal conversations feel more natural and helpful.
- **Higher conversion:** suggestions match the user's behavior and timing.
- **Repeat purchases:** reminders based on past purchases encourage reordering.
- **Builds loyalty:** users feel the assistant knows them.

## 3. Requirements

### Functional Requirements

- **FR-01: Personalized greetings and responses:** the agent greets users by name and refers to relevant past activity.
- **FR-02: Behavior-based content adaptation:** the agent adapts suggestions to the user's browsing and purchase behavior.
- **FR-03: Time-of-day awareness:** the agent adapts suggestions to the current time of day.
- **FR-04: User journey tracking:** the agent identifies the user's current stage in their shopping journey.
- **FR-05: Adaptive response tone:** the agent adapts its tone and answer length to the user's communication style.

### Non-Functional Requirements

- **Privacy:** personalization must not feel intrusive, and must only use data the user agreed to share.
- **Transparency:** users should understand why they see personalized suggestions.
- **Performance:** personalization must not noticeably slow down responses.
- **Fallback:** if personalization data is missing, the agent answers normally.

## 4. Technical Approach

- **User context builder:** at the start of each conversation, build a small user context from the profile, preferences, long-term memory, and recent orders.
- **Prompt personalization:** add this context to the system prompt, such as the user's name, language, tone, and recent purchases.
- **Journey stage:** a simple rule-based classifier based on account age, number of orders, and recent activity (e.g. "new", "browsing", "returning customer").
- **Time awareness:** pass the user's local time to the agent, and use simple rules for morning and night suggestions.
- **Recommendation integration:** use the recommendation system to get personalized product suggestions for the user.
- **Tone adaptation:** detect the user's style (e.g. short messages or casual language) and adjust the response style, within GoCare's brand voice.

## 5. Dependencies & Risks

### Dependencies

- **User Profiles & Authentication**, **User Preferences & Settings**, and **Conversation Memory Management**.
- Access to order and browsing history.
- The recommendation system, for personalized product suggestions.

### Risks

- **Feeling intrusive:** too much personal detail can make users uncomfortable.
- **Wrong assumptions:** the agent may personalize based on incorrect data.
- **Inconsistent brand voice:** adapting tone too much may not fit GoCare's style.
- **More tokens:** adding user context to each request increases cost.

## 6. MVP Scope

### In Scope

- Personalized greetings for logged-in users.
- Using preferences and recent purchases in suggestions.
- Basic time-of-day awareness (morning and night).

### Out of Scope (for now)

- Full user journey tracking.
- Automatic tone adaptation.
- Behavior-based adaptation using browsing history.

## 7. Open Questions

- Which user data is the agent allowed to mention in conversations (e.g. past orders)?

## 8. Assessment

In my view, this feature is partly important:

- **Important:** suggesting products based on the user's past purchases, such as "Your sunscreen may be running low. Would you like to reorder it?" This directly increases sales.
- **Not important:** greeting the user by name and adapting the tone. As in User Profiles & Authentication, what matters is that the agent helps the user find what she wants, not that it says her name.
