# Clarification & Fallback Handling

**Priority:** Medium

## 1. Overview

### The problem

Users often send messages that are unclear, incomplete, or outside what the agent can do. When this happens, the agent may guess the wrong meaning, return an error, or give a confusing answer. This makes users lose trust in the assistant.

### What the feature does

The feature helps the agent handle unclear or failed situations in a helpful way:

- **Ambiguous query clarification:** asks the user what they mean when a message has more than one possible meaning.
- **Missing information requests:** asks for the details needed to complete a request.
- **Graceful error recovery:** handles technical errors, such as a failed tool call, without breaking the conversation.
- **"I don't understand" fallback responses:** responds politely when it cannot understand the message.
- **Suggested alternative queries:** suggests what the user could ask instead.

### Example

> **User:** I want a cream.
>
> **Agent:** Sure! Is it for your face, hands, or body? And what is your skin type?
>
> *(the product search tool fails)*
>
> **Agent:** Sorry, I couldn't load products right now. You can try again in a moment, or tell me the brand you're looking for and I'll help another way.
>
> **User:** asdfgh
>
> **Agent:** I didn't quite understand that. You can ask me things like "Show me sunscreens under 100 SAR" or "Track my order".

## 2. Why It Matters

- **Fewer wrong answers:** the agent asks instead of guessing.
- **No dead ends:** users always know what to do next.
- **More trust:** errors are handled calmly and clearly.
- **Better completion rate:** more conversations end with the user getting what they need.

## 3. Requirements

### Functional Requirements

- **FR-01: Ambiguous query clarification:** the agent detects unclear requests and asks a short clarifying question.
- **FR-02: Missing information requests:** the agent asks for missing details needed to complete a task, such as size, skin type, or address.
- **FR-03: Graceful error recovery:** when a tool or service fails, the agent explains the problem simply and offers another option.
- **FR-04: Fallback responses:** when the agent cannot understand a message, it responds politely instead of guessing.
- **FR-05: Suggested alternative queries:** the agent suggests example questions the user can ask.

### Non-Functional Requirements

- **Balance:** the agent should not ask too many questions; it should only clarify when really needed.
- **Consistency:** fallback messages follow GoCare's tone in Arabic and English.
- **Reliability:** errors are logged for the team to review.
- **Safety:** technical error details are never shown to users.

## 4. Risks

- **Too many questions:** asking for clarification too often annoys users.
- **Hidden errors:** friendly messages may hide real problems if errors are not logged.
- **Repetitive fallbacks:** the same fallback message every time feels robotic.

## 5. MVP Scope

### In Scope

- Clarifying questions for clearly ambiguous requests.
- Requests for missing information in key actions, such as adding to cart.
- Friendly error messages when tools fail.
- Fallback responses with example questions.

### Out of Scope (for now)

- Smart, personalized alternative suggestions.
- Analytics dashboards for fallback cases.

## 6. Open Questions

- When should the agent ask for clarification, and when should it make a reasonable assumption?
- After how many failed attempts should the agent offer human support?
- Is there a human support channel the agent can hand over to?

## 7. Assessment

This feature is important, but there is an alternative: users already confirm their orders through WhatsApp. So even if the agent misunderstands a request, the order is checked with the user before it is completed.
