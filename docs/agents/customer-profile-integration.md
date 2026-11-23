# Customer Profile Integration

**Priority:** Low

## 1. Overview

### The problem

The agent does not know anything about the user's account on GoCare. It cannot see what she bought before, her saved addresses, or her wishlist, so she has to repeat this information, and the agent cannot use it to help her.

### What the feature does

The feature connects the agent to the user's GoCare account:

- **Purchase history access:** the agent knows what the user bought before.
- **Saved addresses and payment methods:** the agent uses the user's saved details, so she does not type them again.
- **Order preferences and recurring orders:** the agent knows products the user orders regularly.
- **Wishlist management:** the user can add or remove products from her wishlist through the chat.
- **Recent views and interactions:** the agent knows the products the user viewed recently.

### Example

> **User:** Add this serum to my wishlist.
>
> **Agent:** Done! The serum is now in your wishlist. ❤️
>
> **User:** Recommend something for me.
>
> **Agent:** You bought a vitamin C serum last month. This sunscreen goes well with it. Would you like to see it?

## 2. Requirements

### Functional Requirements

- **FR-01: Purchase history access:** the agent can read the user's past purchases.
- **FR-02: Saved addresses and payment methods:** the agent can use the user's saved addresses and payment methods.
- **FR-03: Order preferences and recurring orders:** the agent knows the user's regular orders and preferences.
- **FR-04: Wishlist management:** the agent can show, add, and remove wishlist products.
- **FR-05: Recent views and interactions:** the agent can use the products the user viewed recently.

### Non-Functional Requirements

- **Security:** the agent can only access the data of the logged-in user.
- **Privacy:** payment details must never be shown in full in the chat.
- **Accuracy:** profile data must match the user's account on the website.
- **Performance:** loading profile data must not slow down responses.

## 3. Assessment

In my view, this feature is not a high priority at the moment, because it overlaps with other features:

- **User Profiles & Authentication:** both features are about knowing the user and her data.
- **User Preferences & Settings:** both features save the user's preferences.
- **Personalization Engine:** both features use the user's past purchases to suggest products.

The most useful part of this feature is using past purchases in recommendations, and this is already covered by the Personalization Engine.
