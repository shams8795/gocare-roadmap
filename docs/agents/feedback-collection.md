# Feedback Collection

**Priority:** High

## 1. Overview

### The problem

The team cannot easily know whether users are happy with the agent's answers. Without feedback, it is hard to find wrong answers, understand what users need, or measure whether changes improve the agent.

### What the feature does

The feature collects feedback from users about the agent:

- **Message-level feedback:** thumbs up or thumbs down on each answer.
- **Conversation rating system:** a rating for the whole conversation, such as 1 to 5 stars.
- **Detailed feedback forms:** a short form to explain what went wrong or what could be better.
- **Issue reporting mechanism:** a way to report a problem, such as a wrong price or broken link.
- **Feature request collection:** a way for users to suggest new features.

### Example

> **Agent:** Here are 3 sunscreens for oily skin... `👍` `👎`
>
> *(the user taps 👎)*
>
> **Agent:** Sorry about that! What was wrong? `[ Wrong products ]` `[ Too long ]` `[ Wrong price ]` `[ Other ]`
>
> *(at the end of the conversation)*
>
> **Agent:** How was your experience today? ⭐⭐⭐⭐⭐

## 2. Why It Matters

- **Find wrong answers quickly:** negative feedback shows exactly which answers need fixing.
- **Measure quality:** feedback scores show whether the agent is improving over time.
- **Understand users:** issue reports and feature requests show what users really need.
- **Low effort, high value:** simple to build, and useful for every other feature.

## 3. Requirements

### Functional Requirements

- **FR-01: Message-level feedback:** users can rate each answer with thumbs up or down.
- **FR-02: Conversation rating:** users can rate the whole conversation.
- **FR-03: Detailed feedback forms:** users can explain their feedback with a short form or predefined reasons.
- **FR-04: Issue reporting:** users can report specific problems with an answer.
- **FR-05: Feature request collection:** users can suggest new features.

### Non-Functional Requirements

- **Non-intrusive:** feedback requests must not interrupt or annoy users.
- **Traceability:** each feedback item is linked to the exact message, conversation, and user.
- **Privacy:** feedback is stored securely, in line with data protection regulations in Saudi Arabia.
- **Reporting:** the team can view and analyze feedback easily.

## 4. Technical Approach

- **Feedback API:** an endpoint that saves feedback with `message_id`, `conversation_id`, `user_id`, rating, reason, and comment.
- **Message IDs:** each agent answer gets a unique ID, so feedback can be linked to it.
- **Frontend buttons:** thumbs up and down under each answer, and a rating at the end of the conversation.
- **Predefined reasons:** simple reason buttons for negative feedback, plus an optional comment.
- **Storage and review:** save feedback in a database table, and show summaries in the Analytics Dashboard.
- **Tracing:** link feedback to conversation logs, so the team can see the full context of a bad answer.

## 5. Dependencies & Risks

### Dependencies

- Frontend support for feedback buttons and forms.
- **Session Management** and **Conversation Memory Management**, to link feedback to conversations.
- A place to review feedback, such as the Analytics Dashboard.

### Risks

- **Low response rate:** many users do not leave feedback.
- **Biased feedback:** unhappy users are more likely to give feedback than happy ones.
- **No follow-up:** collecting feedback has no value if nobody reviews it.

## 6. Open Questions

- Who will review feedback, and how often?
- Should the conversation rating appear at the end of every conversation, or only sometimes?
- Should feedback be shown in the Analytics Dashboard?
