# Context Awareness

**Priority:** High · **Effort:** High

## 1. Overview

### The problem

People do not talk in complete, separate sentences. They refer to things mentioned earlier, ask short follow-up questions, and change topics. Without context awareness, the agent cannot understand messages such as "the second one", "is it suitable for me?", or "add it to the cart".

### What the feature does

The feature helps the agent understand a conversation as a whole:

- Understands conversations across multiple turns.
- Resolves references, such as "it", "this one", "the second one", and "that product".
- Handles follow-up questions.
- Tracks the current topic, and handles topic changes.
- Keeps track of the conversation state (e.g. browsing, comparing, adding to cart, checkout).

### Example

> **User:** Show me vitamin C serums.
>
> **Agent:** *(shows three products)*
>
> **User:** How much is **the second one**?
>
> **User:** Is **it** suitable for oily skin?
>
> **User:** Has my last order shipped yet?
>
> **User:** OK, add **the serum** to my cart.

The agent must know that "the second one", "it", and "the serum" all refer to the same product, and that the question about the order was a temporary topic change.

## 2. Why It Matters

- **Natural conversations:** users can talk normally, without repeating product names.
- **Fewer mistakes:** the agent acts on the right product.
- **Better shopping flow:** browsing, comparing, and adding to cart happen smoothly in one conversation.
- **Required for complex features:** such as building a skincare routine in the chat.

## 3. Requirements

### Functional Requirements

- **FR-01: Multi-turn understanding:** the agent understands each message in the context of previous messages.
- **FR-02: Reference resolution:** the agent links references (pronouns, "that product", "the second one") to the correct item.
- **FR-03: Follow-up question handling:** the agent answers short follow-up questions about the current item or topic.
- **FR-04: Topic tracking and switching:** the agent detects topic changes, and can return to the previous topic.
- **FR-05: Conversation state management:** the agent tracks the current stage of the conversation, such as browsing, comparing, cart, or checkout.

### Non-Functional Requirements

- **Accuracy:** references must be resolved correctly, especially before actions such as adding to cart.
- **Safety:** when a reference is unclear, the agent must ask for clarification instead of guessing.
- **Performance:** context handling must not noticeably slow down responses.
- **Language support:** works in Arabic and English, including mixed messages.

## 4. Technical Approach

- **Structured state in LangGraph:** besides the message history, store structured context in the graph state, such as `last_shown_products`, `current_product`, `current_topic`, and `conversation_stage`.
- **Reference resolution:** when the agent shows products, save them in order in the state. References like "the second one" are mapped to that list.
- **Query rewriting:** before calling tools, the agent rewrites short follow-up messages into complete requests (e.g. "is it suitable for oily skin?" becomes "is Vitamin C Serum X suitable for oily skin?").
- **Topic tracking:** save the current topic in the state, and keep the previous topic when the user temporarily switches.
- **Clarification:** if a reference matches more than one item, the agent asks the user which one they mean.

## 5. Dependencies & Risks

### Dependencies

- **Conversation Memory Management**, to keep the conversation history and state.
- **Session Management**, to keep the state tied to the right conversation.
- Marketplace and cart tools that return product IDs, so references can be linked to real products.

### Risks

- **Wrong references:** the agent may add the wrong product to the cart.
- **Ambiguity:** messages like "this one" may be unclear when several products were discussed.
- **Arabic references:** Arabic pronouns and dialect expressions (e.g. "ده", "اللي قبله") make resolution harder.
- **Higher costs:** query rewriting adds extra model calls.

## 7. Open Questions

- Should the agent always confirm before actions like adding to cart, or only when the reference is unclear?
- How many recent products should be kept in the state?
- Should context be kept when the user returns to a session later?
