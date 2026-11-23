# Response Quality Improvements

**Priority:** Medium

## 1. Overview

### The problem

The agent can answer questions correctly, but its answers are not always easy to read. Some answers are too long, the tone may change from one answer to another, Arabic answers may sound less natural than English ones, and the agent may repeat the same sentences.

### What the feature does

The feature improves how the agent's answers look and sound:

- **Response length optimization:** short answers for simple questions, and more detail only when needed.
- **Tone and style consistency:** the same friendly GoCare voice in every answer.
- **Multilingual response quality:** natural, high-quality answers in both Arabic and English.
- **Response formatting:** using lists, tables, and emojis where they make answers clearer.
- **Response variation:** avoiding repeating the same phrases in every message.

### Example

**Before:**

> Thank you for your question. There are many sunscreens available in our store. Sunscreens are important for protecting the skin. Here are some options that you may find suitable for your needs and preferences...

**After:**

> Here are 3 sunscreens for oily skin ☀️
>
> 1.  **Sunscreen A** – SPF 50, oil-free – 85 SAR
> 2.  **Sunscreen B** – SPF 50, matte finish – 95 SAR
> 3.  **Sunscreen C** – SPF 30, lightweight – 70 SAR
>
> Want me to compare any of them?

## 2. Why It Matters

- **Easier to read:** users find the information they need quickly.
- **Professional brand image:** consistent tone reflects GoCare's identity.
- **Better Arabic experience:** important for GoCare's Saudi customers.
- **More natural conversations:** less repetition makes the agent feel less robotic.

## 3. Requirements

### Functional Requirements

- **FR-01: Response length optimization:** answers match the complexity of the question.
- **FR-02: Tone and style consistency:** all answers follow GoCare's voice guidelines.
- **FR-03: Multilingual response quality:** Arabic and English answers have the same quality.
- **FR-04: Response formatting:** answers use lists, tables, and emojis when helpful.
- **FR-05: Response variation:** the agent avoids repeating the same openings and closings.

### Non-Functional Requirements

- **Readability:** answers display correctly in the chat interface, including Arabic right-to-left text.
- **Consistency:** formatting rules are applied the same way across all features.
- **Measurability:** response quality can be checked with a test set of example questions.

## 4. Technical Approach

- **Style guide in the system prompt:** clear rules for tone, length, formatting, and emoji use, in Arabic and English.
- **Language-specific instructions:** separate guidance for natural Arabic, including the preferred dialect or Modern Standard Arabic.
- **Formatting rules:** define when to use lists (several products), tables (comparisons), and emojis (light use only).
- **Frontend support:** make sure the chat interface renders Markdown, tables, and mixed Arabic and English text correctly.
- **Evaluation set:** a set of common questions with expected answer quality, used to test changes before release.
- **Variation:** instruct the model to avoid repeated phrases, and review conversation logs for repetitive patterns.

## 5. Dependencies

- A GoCare brand voice and style guide.
- Frontend support for rich formatting.
- Sample conversations for evaluation.

## 6. Open Questions

- Is there an official GoCare brand voice?
- Does the chat interface support Markdown tables?
