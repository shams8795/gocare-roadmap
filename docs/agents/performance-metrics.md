# Performance Metrics

**Priority:** Medium

## 1. Overview

### The problem

The team does not know if the agent is working well from a technical side: Is it fast? Does it make many errors? Which tools fail? So problems may stay without anyone noticing.

### What the feature does

The feature measures the agent's performance:

- **Response time monitoring:** how long the agent takes to answer.
- **Tool usage statistics:** which tools are used the most.
- **Success rate tracking:** how many requests the agent completes successfully.
- **Error rate monitoring:** how many times the agent or its tools fail.
- **User engagement metrics:** how much users use the agent.

### Example

> The team finds that the average response time became 8 seconds instead of 3 seconds, and that the product search tool fails 10% of the time. So they know where the problem is and fix it quickly.

## 2. Requirements

### Functional Requirements

- **FR-01: Response time:** the system measures the time of each response.
- **FR-02: Tool usage:** the system records each tool used and how many times.
- **FR-03: Success rate:** the system measures the percentage of requests completed successfully.
- **FR-04: Error rate:** the system records errors and their types.
- **FR-05: User engagement:** the system shows the number of conversations and messages.

### Non-Functional Requirements

- **Performance:** measuring must not slow down the agent.
- **Alerts:** the team receives an alert if errors or response time go above a set limit.
- **Reliability:** metrics data is kept even if the agent restarts.

## 3. Data Requirements

| Data                                 | Purpose                                 | Status                                     |
|--------------------------------------|-----------------------------------------|--------------------------------------------|
| Response Time per Message            | Measure the agent's speed               | Not collected yet                          |
| Tool Call Logs                       | Know which tools are used and how often | Not collected yet                          |
| Error Logs                           | Measure the error rate and its causes   | Partly available through the existing logs |
| Request Outcome (success or failure) | Measure the success rate                | Not collected yet                          |
| Number of Conversations and Messages | Measure user engagement                 | Depends on Session Management              |

## 4. Assessment

In my view, this feature is important for the team:

- It helps the team find problems quickly, before users get annoyed.
- It is not hard, and part of it already exists in the health monitoring endpoints.
- It has a small overlap with Session Management (number of sessions) and Feedback Collection (user satisfaction).
