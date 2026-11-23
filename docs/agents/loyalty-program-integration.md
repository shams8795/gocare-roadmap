# Loyalty Program Integration

**Priority:** Low

## 1. Overview

### The problem

GoCare has loyalty points for its customers, but when a user wants to know how many points she has, when they expire, or how to use them, she has to search the website. The agent does not know anything about her points, so it cannot remind her to use them or tell her about offers made only for loyalty members. As a result, many users forget their points, and the points expire without being used.

### What the feature does

The feature connects the agent to GoCare's loyalty program:

- **Points balance queries:** the user asks the agent how many points she has, and when they expire.
- **Rewards redemption:** the user uses her points for a discount, free shipping, or a gift, directly from the chat.
- **Tier status information:** the user knows her membership level (for example, Silver or Gold), its benefits, and how much she needs to reach the next level.
- **Special offers for loyalty members:** the agent shows offers that are available only to loyalty members.

### Example

> **User:** How many points do I have?
>
> **Agent:** You have 450 points, which equals a 45 SAR discount on your next order. 120 of these points expire at the end of this month. Would you like to use them now? 🎁
>
> **User:** How far am I from Gold?
>
> **Agent:** You need 300 more points to reach Gold. Gold members get free shipping on every order.

## 2. Requirements

### Functional Requirements

- **FR-01: Points balance:** the agent shows the user's current points balance, their value in SAR, and the points that will expire soon.
- **FR-02: Rewards redemption:** the agent shows the available rewards and helps the user use her points on her cart or next order.
- **FR-03: Tier status:** the agent shows the user's current level, its benefits, and the points or orders needed for the next level.
- **FR-04: Special offers:** the agent shows the offers available for the user's level.
- **FR-05: Expiry reminders:** the agent reminds the user about points that will expire soon when she starts a conversation.

### Non-Functional Requirements

- **Accuracy:** the points balance must match the website exactly, because a wrong number damages trust.
- **Confirmation:** the agent must get a clear confirmation from the user before using her points.
- **Security:** the user can only see and use her own points, and only when she is logged in.
- **Consistency:** the rules shown by the agent must be the same as the rules on the website.
- **Language support:** works in Arabic and English.

## 3. Data Requirements

- **Loyalty program rules:** how users earn points (for example, one point for each SAR), how many points equal one SAR, the minimum points needed for redemption, and when points expire.
- **User points balance:** an API that returns the current points balance for each user, the points history, and the expiry date of each group of points.
- **Tiers and their conditions:** the names of the levels, the points or number of orders needed for each level, and the benefits of each level, such as free shipping or extra discounts.
- **Available rewards:** a list of what the user can redeem her points for (discount, free shipping, gift), how many points each reward needs, and any conditions, such as a minimum order value.
- **Current special offers:** the active offers for loyalty members, which levels they are for, and their start and end dates.
- **Redemption API:** an API that lets the agent apply points to the user's cart or order safely, and returns the result.

## 4. Assessment

In my view, this feature is not important at the moment:

- **The website already shows the points:** the user can see her points from her account on the website.
- **It needs backend work first:** the agent needs APIs for the points balance, rewards, and redemption before it can do anything.
- **Redemption is sensitive:** using points affects the order price, so any mistake costs money and needs strong confirmation.
- **A simple first step:** later, we can start with showing the points balance and expiry only, without redemption.
