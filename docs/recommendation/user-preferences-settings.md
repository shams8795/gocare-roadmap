# User Preferences & Settings

**Priority:** Medium · **Effort:** Medium

## 1. Overview

### The problem

Every user has different preferences: some prefer Arabic, some English; some like a formal tone, others a casual one; some only buy certain brands or within a certain budget. Today, the agent does not store these preferences, so users must repeat them, and the agent cannot adapt its answers.

### What the feature does

The feature stores and uses each user's preferences:

- **Language preference:** Arabic or English.
- **Notification preferences:** which alerts the user wants, such as price alerts.
- **Communication style:** formal or casual.
- **Product category interests:** such as skin care, hair care, or perfumes.
- **Price range preferences:** the user's usual budget.
- **Brand preferences:** brands the user likes, or wants to avoid.

### Example

> A user tells the agent once: "I prefer to talk in Arabic, keep it casual, and my budget is under 150 SAR."
>
> In every future conversation, the agent answers in Arabic, uses a friendly tone, and recommends products under 150 SAR first.

## 2. Why It Matters

- **Less repetition:** users do not have to repeat their preferences.
- **More relevant results:** products match the user's budget, brands, and interests.
- **Better experience:** the agent talks in the user's preferred language and style.
- **Fewer unwanted notifications:** users only receive the alerts they chose.

## 3. Requirements

### Functional Requirements

- **FR-01: Language preference storage:** the agent saves and uses the user's preferred language.
- **FR-02: Notification preferences:** users choose which notifications they receive.
- **FR-03: Communication style preference:** the agent adapts between formal and casual tones.
- **FR-04: Product category interests:** the agent saves categories the user is interested in and prioritizes them.
- **FR-05: Price range preferences:** the agent saves the user's budget and uses it to filter or rank products.
- **FR-06: Brand preferences:** the agent saves preferred and avoided brands.

### Non-Functional Requirements

- **User control:** users can view, change, or reset their preferences at any time.
- **Privacy:** preferences are stored securely and only used for this user.
- **Performance:** loading preferences must not slow down responses.

## 4. Technical Approach

- **Preferences store:** a preferences table or document linked to the user ID, with fields such as `language`, `tone`, `categories`, `price_min`, `price_max`, `preferred_brands`, `avoided_brands`, and `notifications`.
- **Two ways to set preferences:**
- **Explicitly**, through a settings page or by asking the agent ("speak to me in Arabic").
- **Implicitly**, by detecting preferences from conversations, then confirming them with the user before saving.
- **Using preferences:** preferences are loaded at the start of each conversation and added to the agent's state. Language and tone are applied in the system prompt, while categories, price range, and brands are passed to the marketplace tools as filters.
- **Link to long-term memory:** preferences can be stored as part of the long-term memory from Conversation Memory Management.

## 5. Dependencies & Risks

### Dependencies

- **User Profiles & Authentication**, to link preferences to a user.
- **Conversation Memory Management**, for long-term storage.
- Marketplace tools that support filtering by price, brand, and category.

### Risks

- **Wrong detected preferences:** the agent may guess a preference incorrectly and keep using it.
- **Too narrow results:** strict filters may hide good products the user would like.
- **Outdated preferences:** users' budgets and interests change over time.

## 7. Open Questions

- Should preferences be managed from the website settings, from the chat, or both?
- Should price range and brands be strict filters, or only used to rank results?
- Which notifications are currently supported by GoCare?
