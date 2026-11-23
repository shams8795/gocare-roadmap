# User Engagement Features

**Priority:** Low

## 1. Overview

### The problem

Users sometimes receive useful answers from the agent, such as a skincare routine or a product comparison, but they cannot easily save, find, or share them later. Once the conversation moves on, useful information gets lost.

### What the feature does

The feature lets users keep and reuse their conversations:

- **Conversation bookmarking:** save a whole conversation to find it later.
- **Message starring and saving:** save a specific answer, such as a routine or a product list.
- **Conversation export:** download a conversation as PDF or JSON.
- **Share conversation snippets:** share part of a conversation with others, such as a friend.
- **Conversation search:** search through past conversations.

### Example

> The agent builds a full morning and night skincare routine for a user. She stars the answer, so she can open it again next week without asking again.
>
> Later, she searches her history for "sunscreen" and finds the conversation where the agent compared three sunscreens.

## 2. Why It Matters

- **Saves time:** users do not need to ask the same question again.
- **Useful long-term:** routines and comparisons can be reused.
- **Sharing:** users can share recommendations with friends, which may bring new customers.
- **More engagement:** users return to the agent more often.

## 3. Requirements

### Functional Requirements

- **FR-01: Conversation bookmarking:** users can bookmark conversations.
- **FR-02: Message starring:** users can star and save individual messages.
- **FR-03: Conversation export:** users can export conversations as PDF or JSON.
- **FR-04: Share snippets:** users can share selected messages through a link.
- **FR-05: Conversation search:** users can search their past conversations by keyword.

### Non-Functional Requirements

- **Privacy:** shared snippets must not include personal information unless the user chooses it.
- **Security:** users can only access, search, and export their own conversations.
- **Performance:** search must return results quickly.
- **Language support:** search works in Arabic and English.

## 4. Technical Approach

- **Conversation storage:** relies on stored conversations from Conversation Memory Management.
- **Bookmarks and stars:** simple tables linking `user_id` to `conversation_id` or `message_id`.
- **Export:** generate PDF and JSON files on the server from the stored conversation.
- **Sharing:** create a shareable link with a read-only copy of the selected messages.
- **Search:** keyword search over stored conversations, with possible semantic search later using the existing vector database.

## 5. Dependencies & Risks

### Dependencies

- **Conversation Memory Management**, for stored conversations.
- **User Profiles & Authentication**, since these features need a logged-in user.
- Frontend support for bookmark, star, export, and share actions.

### Risks

- **Low usage:** users may not use these features much, which is why the priority is low.
- **Privacy in sharing:** shared conversations may contain personal details.
- **Storage growth:** saving and exporting many conversations increases storage.

## 6. MVP Scope

### In Scope

- Message starring and a "saved messages" list.
- Conversation search by keyword.

### Out of Scope (for now)

- Conversation export to PDF and JSON.
- Sharing snippets through links.
- Semantic search.

## 7. Open Questions

- Do users currently have a conversation history screen in the chat?
- Should shared snippets be public links, or only visible to logged-in users?
- How long should saved conversations be kept?
