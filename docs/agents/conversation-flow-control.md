# Conversation Flow Control

**Priority:** Medium

## 1. Overview

### The problem

Users come to the agent for many different reasons: searching for products, asking questions, managing their cart, or getting help with an order. Some tasks also need several steps, such as building a skincare routine or checking out. Without clear flow control, the agent may handle every message the same way, lose track of multi-step tasks, or get confused when the user interrupts or changes the subject.

### What the feature does

The feature controls how conversations move between tasks and steps:

- **Intent classification and routing:** understands what the user wants and sends the request to the right part of the agent.
- **Conversation branching:** follows different paths depending on the user's answers.
- **Step-by-step guided workflows:** guides users through multi-step tasks, one step at a time.
- **Conversation interruption handling:** handles questions in the middle of a task, then returns to the task.
- **Topic switching detection:** detects when the user moves to a completely new topic.

### Example

> **User:** I want to build a skincare routine.
>
> **Agent:** Great! Step 1 of 3: What is your skin type?
>
> **User:** Oily. Wait, how much is shipping to Jeddah?
>
> **Agent:** Shipping to Jeddah is 25 SAR. Now, back to your routine: Step 2 of 3: What is your main concern?

The agent recognized the routine-building intent, started a guided workflow, answered the interruption, then continued the workflow.

## 2. Why It Matters

- **Right answer for each request:** each type of request is handled by the right logic and tools.
- **Complex tasks become easy:** step-by-step guidance helps users complete multi-step tasks.
- **No lost progress:** interruptions do not reset the task.
- **Easier to extend:** new tasks can be added as new routes or workflows.

## 3. Requirements

### Functional Requirements

- **FR-01: Intent classification and routing:** the agent classifies each message (e.g. product search, product question, cart, order, knowledge base, out of scope) and routes it to the right handler.
- **FR-02: Conversation branching:** the agent follows different paths based on the user's answers.
- **FR-03: Guided workflows:** the agent supports multi-step workflows, showing the current step and remembering previous answers.
- **FR-04: Interruption handling:** the agent answers interruptions and then returns to the current workflow.
- **FR-05: Topic switching detection:** the agent detects a real topic change and asks whether to continue or cancel the current task.

### Non-Functional Requirements

- **Accuracy:** intent classification must be accurate, with a safe default when unsure.
- **Performance:** routing must not noticeably slow down responses.
- **Maintainability:** workflows must be easy to add and change.
- **Language support:** works in Arabic and English.

## 4. Technical Approach

- **Router node in LangGraph:** a node at the start of the graph classifies the intent and routes to the right sub-graph or set of tools.
- **Reuse the existing guardrail:** the current message classification guardrail already separates in-scope and out-of-scope messages. Intent classification can extend it with more detailed categories.
- **Workflows as sub-graphs:** each guided workflow (e.g. skincare routine, checkout) is a LangGraph sub-graph with its own steps and state.
- **Workflow state:** save the active workflow, current step, and collected answers in the conversation state.
- **Interruptions:** if a message does not belong to the current step, handle it as a side question, then return to the saved step.
- **Topic switching:** if the user clearly starts a new task, ask whether to pause or cancel the current one.
