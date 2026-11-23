# Order Management

**Priority:** Low

## 1. Overview

### The problem

Today, when a user wants to know where her order is, cancel it, or return a product, she has to search the website or contact customer service. The agent cannot help her with her orders.

### What the feature does

The feature lets the user manage her orders directly from the chat:

- **Order status tracking:** the user asks about the status of her order.
- **Order history retrieval:** the user sees her past orders.
- **Cancellation and modification support:** the user can cancel an order or change details, such as the address.
- **Return and refund assistance:** the agent helps the user return a product and get her money back.
- **Delivery tracking:** the user knows where her shipment is and when it will arrive.

### Example

> **User:** Where is my order?
>
> **Agent:** Your order \#1234 was shipped yesterday, and it will arrive tomorrow. 🚚
>
> **User:** The cream arrived damaged. What should I do?
>
> **Agent:** Sorry about that! I can start a return request for you. Would you like a refund or a replacement?

## 2. Requirements

### Functional Requirements

- **FR-01: Order status tracking:** the agent shows the current status of the user's order.
- **FR-02: Order history retrieval:** the agent shows the user's past orders.
- **FR-03: Cancellation and modification:** the agent can cancel an order or change its details, if the order has not been shipped yet.
- **FR-04: Return and refund assistance:** the agent guides the user through the return process and starts a return request.
- **FR-05: Delivery tracking:** the agent shows the shipment location and the expected delivery date.

### Non-Functional Requirements

- **Security:** the user can only see and change her own orders.
- **Confirmation:** the agent must ask the user to confirm before cancelling or changing an order.
- **Accuracy:** order information must be up to date and match the website.
- **Performance:** order information must load quickly.
- **Language support:** works in Arabic and English.

## 3. Assessment

In my view, this feature is not a high priority at the moment, for these reasons:

- **Orders are already confirmed through WhatsApp:** the user already talks with the team on WhatsApp about her order, so she can ask about its status there.
- **The website already shows order information:** the user can see her order status and order history from her account on the website.
- **Cancellation and refunds are sensitive:** letting the agent cancel orders or start refunds needs strong confirmation and backend support, and a mistake can cost money.
- **It needs backend work first:** the agent needs order, shipping, and return APIs before it can answer any order question.
