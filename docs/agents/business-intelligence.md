# Business Intelligence

**Priority:** Medium

## 1. Overview

### The problem

Users' conversations with the agent contain important business information, such as the products users are looking for, but nobody uses this information.

### What the feature does

The feature extracts business information from the conversations:

- **Product inquiry trends:** which products users ask about the most.
- **Popular search terms:** the words users use the most.
- **Category interest analysis:** which categories users are interested in, such as skin care, hair care, or perfumes.
- **Peak usage times:** when users use the chat the most.
- **User retention metrics:** how many users come back to use the agent again.

### Example

> The marketing team finds that many users ask about a "serum for dark spots", and this product is not available on the website. So they decide to add it.

## 2. Requirements

### Functional Requirements

- **FR-01: Product inquiries:** the system shows the products users ask about the most.
- **FR-02: Search terms:** the system shows the words users use the most.
- **FR-03: Categories:** the system shows users' interest in each category.
- **FR-04: Peak times:** the system shows the busiest usage times.
- **FR-05: Retention:** the system shows the percentage of users who come back.

### Non-Functional Requirements

- **Privacy:** reports show general numbers, not data about specific users.
- **Updates:** reports are updated regularly, for example every week.
- **Readability:** reports are clear for the marketing team, not only for developers.

## 3. Data Requirements

| Data                                | Purpose                           | Status                                    |
|-------------------------------------|-----------------------------------|-------------------------------------------|
| Conversation Logs                   | Find what users ask about         | Depends on Conversation Memory Management |
| Products Mentioned in Conversations | Find the most requested products  | Not collected yet                         |
| Product Categories                  | Analyze interest in each category | Available on the website                  |
| Message Timestamps                  | Find peak usage times             | Available                                 |
| User IDs                            | Measure how many users come back  | Depends on User Profiles & Authentication |

## 4. Assessment

In my view, this feature is important, because it shows the team what users ask about the most. This helps the marketing team know which products are in demand, and which products are missing from the website and need to be added.
