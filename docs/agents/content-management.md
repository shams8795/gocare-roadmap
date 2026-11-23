# Content Management

**Priority:** Low

## 1. Overview

### The problem

The information the agent answers from, such as FAQs and offers, is fixed inside the code. So when there is a new offer or a season such as Ramadan or the Saudi National Day, the agent does not know about it until a developer changes the code. This means the agent may give old information, such as an offer that already ended, or miss new offers that could increase sales.

### What the feature does

The feature lets the team manage the agent's content without a developer:

- **Dynamic FAQ management:** the team adds, edits, and deletes FAQs and their answers.
- **Promotional content delivery:** the agent knows the current offers and tells users about them when relevant.
- **Seasonal content updates:** the agent talks about seasons, such as Ramadan offers or White Friday.
- **Banner and announcement system:** short messages appear in the chat, such as "20% off today only".

### Example

> Ramadan offers start. The marketing team adds the offer to the system, with a start date and an end date.
>
> **User:** Are there any offers?
>
> **Agent:** Yes! 25% off all skincare products during Ramadan. 🌙 The offer ends on the last day of Ramadan.
>
> When Ramadan ends, the offer disappears automatically, and the agent stops mentioning it.

## 2. Requirements

### Functional Requirements

- **FR-01: FAQ management:** the team can add, edit, and delete FAQs in Arabic and English.
- **FR-02: Promotional content:** the agent knows the current offers and mentions them when the user asks or when they are related to the products she is looking at.
- **FR-03: Seasonal content:** the team can add seasonal content with a start and end date.
- **FR-04: Announcements:** the team can add a short announcement that appears in the chat for a set period.
- **FR-05: Content preview:** the team can preview how the agent will answer with the new content before publishing it.

### Non-Functional Requirements

- **Ease of use:** the marketing team can edit content without a developer.
- **Fast updates:** changes appear in the agent's answers right away.
- **Automatic expiry:** offers and seasonal content disappear automatically when their end date passes.
- **Approval:** content is reviewed before it is shown to users.
- **Language support:** all content is available in Arabic and English.

## 3. Data Requirements

- **Current FAQs:** all the FAQs on the website and their answers, in Arabic and English, as the starting point.
- **Current offers:** for each offer: its name, details, the products or categories it covers, the discount value, and its start and end dates.
- **Seasons calendar:** the important seasons for Saudi customers (Ramadan, Eid, Saudi National Day, White Friday), their dates, and the suitable content for each one.
- **Announcement content:** the text of each announcement, where and when it appears, and its end date.
- **Content approval process:** who in the team reviews content before it is shown to users, and how long the review takes.

## 4. Assessment

In my view, this feature is not important as a separate feature:

- **FAQ management** is already covered in the Admin Dashboard (knowledge base management).
- **Promotional content** overlaps with Personalized Marketing, which the marketing team reviews.
- **The better option** is to add it as part of the Admin Dashboard, instead of building it as a separate feature.
