# Conversation Memory Management

**Priority:** High · **Effort:** High

## 1. Overview

### The problem

The GoCare agent is currently **stateless**: each message is handled as if it were the first one. The language model itself does not remember anything between messages, so the agent cannot recall what the user said earlier in the conversation, or in previous conversations.

### What the feature does

The feature gives the agent memory at two levels:

- **Short-term memory:** remembers what was said in the current conversation.
- **Long-term memory:** remembers important information about the user across conversations, such as skin type, preferred brands, or allergies.

It also stores conversation history permanently, keeps each user's memory separate, and summarizes long conversations so they stay fast and affordable.

### Example

> **User:** My skin is oily.
>
> *(three messages later)*
>
> **User:** Can you recommend a moisturizer?
>
> **Agent:** Since your skin is oily, here is a light gel moisturizer...
>
> *(the same user returns a week later)*
>
> **Agent:** Welcome back! Last time you were looking for products for oily skin. Would you like to continue?

## 2. Why It Matters

- **Users do not repeat themselves:** the agent remembers what they already said.
- **More personal recommendations:** answers use the user's known preferences.
- **Foundation for other features:** Context Awareness and the Skincare Routine Advisor both depend on memory.
- **Continuity:** users can return to previous conversations without losing anything.

## 3. Requirements

### Functional Requirements

- **FR-01: Short-term memory:** the agent keeps the context of the current session and uses it in every response.
- **FR-02: Long-term memory:** the agent stores and reuses important user preferences and history across sessions.
- **FR-03: Conversation history persistence:** conversations are stored permanently and are not lost after a restart or a closed page.
- **FR-04: Context retention across messages:** the agent connects related messages into one request (e.g. "shampoo", "for colored hair", "under 100 SAR").
- **FR-05: User-specific memory isolation:** each user's memory is accessible only to that user.
- **FR-06: Memory summarization:** older parts of long conversations are summarized, while recent messages are kept in full.

### Non-Functional Requirements

- **Privacy & Security:** memory must never leak between users, and must follow data protection regulations in Saudi Arabia.
- **Performance:** loading memory must not noticeably slow down responses.
- **Cost:** summarization must keep the number of tokens sent to the model under control.
- **Scalability:** memory must work across multiple agent instances, in line with the current stateless, horizontally scalable design.
- **Reliability:** if the memory store is unavailable, the agent must still answer, without memory.

## 4. Technical Approach

- **Short-term memory and persistence:** use a LangGraph **checkpointer** to save the conversation state after each step, backed by a shared database such as PostgreSQL or Redis, so any agent instance can continue the conversation.
- **Thread per conversation:** each conversation has a unique `thread_id`, linked to the user's ID.
- **Long-term memory:** use a LangGraph **store** (or a dedicated table) to save extracted facts per user, such as skin type, hair type, preferred brands, and allergies.
- **Memory extraction:** after each conversation, or at key moments, the agent extracts important facts and saves them to long-term memory.
- **Summarization:** when a conversation exceeds a set length, older messages are replaced with a short summary, and only the last N messages are kept in full.
- **Isolation:** every read and write is filtered by the authenticated user ID, never by an ID sent in the message.

## 5. Dependencies & Risks

### Dependencies

- **Session Management**, to identify conversations and users.
- A shared database for memory and checkpoints.
- A stable user ID from authentication.

### Risks

- **Memory leakage between users:** a bug could show one user's information to another. This is the most serious risk.
- **Wrong long-term facts:** the agent may save something incorrect, such as the wrong skin type, and keep using it.
- **Lost details in summaries:** important information may be dropped when summarizing.
- **Higher costs:** sending more context with each message increases model usage.

## 6. MVP Scope

### In Scope

- Short-term memory within a conversation.
- Conversation history persistence using a LangGraph checkpointer.
- User-specific memory isolation.

### Out of Scope (for now)

- Long-term memory across conversations.
- Automatic memory summarization.
- A screen for users to view or delete their memory.

## 7. Open Questions

- Which database should be used: PostgreSQL, Redis, or the existing database?
- How long should conversations and long-term memory be kept?
- Should guest users (not logged in) have memory?

## 8. Business Impact

- **Higher conversion:** the agent remembers what the user is looking for, so it reaches the right product faster, and the user is more likely to buy.
- **Fewer abandoned conversations:** users leave less often when they do not have to repeat their skin type, budget, or preferences.
- **More returning customers:** when the agent welcomes the user back and continues from where they stopped, the user is more likely to return and buy again.
- **Better personal recommendations:** recommendations based on what the user already said lead to more relevant products and larger orders.
- **Controlled model costs:** summarizing long conversations keeps the number of tokens low, so costs do not grow with conversation length.

### Example

A user tells the agent that her skin is oily and her budget is under 100 SAR. Without memory, she has to repeat this in every message, and she may leave. With memory, the agent recommends suitable products directly, and she buys in the same conversation.
