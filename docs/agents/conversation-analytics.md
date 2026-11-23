# Conversation Analytics

**Priority:** Medium

## 1. Overview

### The problem

The team does not know what users talk about with the agent, where they leave the conversation, or how many conversations end with a purchase. So it is hard to know what the agent needs to improve.

### What the feature does

The feature analyzes users' conversations with the agent:

- **Intent classification and tracking:** what users ask about the most, such as products, orders, or shipping.
- **Sentiment analysis:** whether users are happy or unhappy in the conversation.
- **Common query patterns:** the most frequent questions.
- **Drop-off points identification:** where users leave the conversation.
- **User satisfaction metrics:** measures of how satisfied users are with the conversations.
- **Conversion funnel analysis:** how many conversations start with a question and end with a purchase.

### Example

> The team opens the report and finds:
>
> - 40% of the questions are about sunscreen.
> - Many users leave the conversation after asking about the shipping price.
> - 15% of conversations end with a purchase.
>
> So the team understands that the shipping answer needs to be improved.

## 2. Requirements

### Functional Requirements

- **FR-01: Intent classification:** the system classifies each conversation by request type.
- **FR-02: Sentiment analysis:** the system detects whether a conversation is positive or negative.
- **FR-03: Common queries:** the system shows the most frequent questions.
- **FR-04: Drop-off points:** the system detects the stage where users leave the conversation.
- **FR-05: Satisfaction metrics:** the system shows user satisfaction measures.
- **FR-06: Conversion funnel:** the system shows how many conversations reach each stage until purchase.

### Non-Functional Requirements

- **Privacy:** the analysis does not show users' personal data.
- **Performance:** the analysis does not affect the agent's response speed.
- **Accuracy:** classification must be accurate in Arabic and English.

## 3. Data Requirements

| Data                               | Purpose                                      | Status                                                                     |
|------------------------------------|----------------------------------------------|----------------------------------------------------------------------------|
| Conversation Logs                  | Analyze what users talk about                | Depends on Conversation Memory Management                                  |
| Message Intent Labels              | Know the type of each request                | Not available; can come from the existing message classification guardrail |
| Conversation End Point             | Find where users leave the conversation      | Not collected yet                                                          |
| Order Data Linked to Conversations | Know if a conversation ended with a purchase | Not available                                                              |
| User Feedback Ratings              | Measure user satisfaction                    | Depends on Feedback Collection                                             |

## 4. Assessment

In my view, this feature is useful, but it is not a high priority at the moment:

- **Sentiment analysis** was considered not needed now in the meeting, and its source is the website comments.
- The results need the **Analytics Dashboard** to be shown, which is not a top priority.
- The effort is high.
