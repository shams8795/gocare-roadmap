# Multi-Agent Workflows

**Priority:** Low

## 1. Overview

### The problem

Today, one agent does everything: it searches for products, answers skincare questions, and handles orders. As tasks grow, one agent may get confused, and its prompt becomes large and hard to change.

### What the feature does

The feature divides the work between several agents, each one specialized in one area:

- **Supervisor agent:** understands what the user wants and sends the request to the right agent.
- **Specialized agents:** a product expert, a skincare specialist, and an order handler.
- **Agent collaboration and handoff:** agents pass the conversation to each other.
- **Task delegation and coordination:** a large task is divided between them.

### Example

> **User:** I want a routine for my oily skin, and where is my last order?
>
> - The **supervisor** splits the request into two parts.
> - The **skincare specialist** builds the routine.
> - The **order handler** gets the order status.
> - The **supervisor** combines both answers and sends them to the user.

## 2. Requirements

### Functional Requirements

- **FR-01: Supervisor agent:** classifies each request and sends it to the right agent.
- **FR-02: Specialized agents:** each agent has its own tools and instructions for its area.
- **FR-03: Handoff:** an agent can pass the conversation to another agent without losing context.
- **FR-04: Task delegation:** the supervisor can split a request into several tasks and combine the results.

### Non-Functional Requirements

- **Performance:** having several agents must not slow down the response much.
- **Cost:** the number of model calls must not increase without need.
- **Consistency:** the user must feel she is talking to one assistant, not several.

## 3. Data Requirements

- **Request categories:** a clear list of request types users ask about (product search, skincare question, order, shipping, cart), with real message examples for each type in Arabic and English. The supervisor needs this to send each message to the right agent, and it can start from the categories in the existing message classification guardrail.
- **Tool assignment per agent:** a list of all existing tools, and which agent owns each tool. For example, product search belongs to the product expert, and order status belongs to the order handler. We must make sure no important tool is left without an agent.
- **Instructions for each agent:** a separate system prompt for each agent, with its area, what it is allowed to do, and when to return the request to the supervisor.
- **Shared conversation state:** one place that all agents read from and write to: previous messages, products shown, and user information such as skin type. Without it, the user would have to repeat herself every time the request moves to another agent.
- **Handoff log:** a record of every time the conversation moved from one agent to another, and why. The team needs it to check whether the supervisor routes requests correctly.

## 4. Assessment

In my view, this feature is not a priority at the moment:

- **The effort is very high.**
- **It overlaps with Conversation Flow Control**, which already includes a router that directs requests.
- **Higher cost**, because each agent uses the model.
- **One agent with tools is enough** until the number of tasks really grows.
