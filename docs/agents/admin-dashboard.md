# Admin Dashboard

**Priority:** Medium

## 1. Overview

### The problem

Any change in the agent, such as changing information or following its performance, needs a developer. The team does not have one place to see how the agent is working.

### What the feature does

- **Web-based configuration UI:** the team changes the agent's settings without code.
- **Real-time monitoring and analytics:** the team sees conversations and numbers as they happen.
- **Knowledge base management interface:** the team adds or edits the information the agent answers from, such as the shipping and return policy.
- **User management and moderation:** the team follows conversations and handles abuse.
- **Tool performance metrics.**
- **System health dashboard:** whether the agent is working or down.

### Example

> The shipping price to Jeddah changed. Instead of a developer changing the code, a team member opens the dashboard, edits the information in the knowledge base, and the agent answers with the new price right away.

## 2. Requirements

### Functional Requirements

- **FR-01: Configuration:** the team can change the agent's settings from the web.
- **FR-02: Monitoring:** the dashboard shows conversations and numbers in real time.
- **FR-03: Knowledge base:** the team can add, edit, and delete knowledge base information.
- **FR-04: User management:** the team can view conversations and handle abusive ones.
- **FR-05: Tool performance:** the dashboard shows tool speed and failure rate.
- **FR-06: System health:** the dashboard shows the status of the agent and its parts.

### Non-Functional Requirements

- **Permissions:** each team member can only see and edit what they are allowed to.
- **Ease of use:** the dashboard is easy for the marketing and content team, not only for developers.
- **Change log:** every change is recorded: who made it and when.

## 3. Data Requirements

- **Current knowledge base information:** all the information the agent currently answers from (shipping, returns, payment, FAQs), so it can be moved to the dashboard and edited easily.
- **List of editable settings:** exactly what the team is allowed to change without a developer, such as the welcome message or shipping prices.
- **Performance numbers:** response time, error rate, and tool usage, which come from Performance Metrics.
- **Conversation logs:** for monitoring and user management, which depend on Conversation Memory Management.
- **Team roles and permissions:** who in the team will use the dashboard, and what each person is allowed to do.

## 4. Assessment

In my view, this feature is useful, but it is better to build it inside GoCare's existing Admin Dashboard:

- GoCare already has an Admin Dashboard, and it was decided in the meeting that the Analytics Dashboard will be inside it. So it is better to add agent pages inside it, instead of building a new dashboard.
- The most important part is knowledge base management, because it lets the team update the agent's information without a developer.
- The other parts (monitoring and tool performance) depend on Performance Metrics being built first.
