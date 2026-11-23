# Interactive Elements

**Priority:** Medium

## 1. Overview

### The problem

Today, users interact with the agent mainly by typing. Typing every request takes effort, especially on mobile, and showing products as plain text is less attractive than showing them with images and buttons.

### What the feature does

The feature adds interactive elements to the chat:

- **Quick reply suggestions:** small buttons with suggested answers, such as "Oily skin" or "Dry skin".
- **Button-based actions:** buttons for actions, such as "Add to cart" or "View details".
- **Carousel for product display:** products shown as cards with image, name, and price, which the user can swipe through.
- **Suggested follow-up questions:** buttons with possible next questions after each answer.
- **Form-based data collection:** small forms inside the chat for collecting several details at once, such as an address.

### Example

> **Agent:** What is your skin type?
>
> `[ Oily ]` `[ Dry ]` `[ Combination ]` `[ Sensitive ]`
>
> **Agent:** Here are some moisturizers for oily skin:
>
> *(a carousel of product cards, each with an image, name, price, and an "Add to cart" button)*
>
> `[ Compare these ]` `[ Show cheaper options ]`

## 2. Why It Matters

- **Faster interaction:** users tap instead of typing.
- **Better on mobile:** easier to use on small screens.
- **More attractive product display:** images and prices increase interest.
- **Higher conversion:** "Add to cart" buttons shorten the path to purchase.
- **Guided conversations:** suggestions show users what the agent can do.

## 3. Requirements

### Functional Requirements

- **FR-01: Quick reply suggestions:** the agent can send suggested replies as buttons.
- **FR-02: Button-based actions:** product messages include action buttons, such as "Add to cart" and "View details".
- **FR-03: Product carousel:** the agent can show multiple products as swipeable cards.
- **FR-04: Suggested follow-up questions:** the agent can suggest the next questions as buttons.
- **FR-05: Form-based data collection:** the agent can show a small form to collect structured information.

### Non-Functional Requirements

- **Fallback to text:** if an element cannot be displayed, the same information is shown as text.
- **Mobile-friendly:** elements work well on small screens.
- **Accessibility and language:** elements support Arabic and English, including right-to-left layout.
- **Consistency:** the same element types are used across all features.

## 4. Technical Approach

- **Structured response format:** the agent returns structured data along with the text, such as `quick_replies`, `buttons`, `carousel`, and `form`, instead of only plain text.
- **Frontend components:** the chat interface renders each element type (buttons, cards, forms).
- **Actions:** when a user taps a button, the frontend sends a defined action (e.g. `add_to_cart` with a product ID) back to the agent.
- **Product cards:** use product data from the marketplace tools, such as image, name, price, and ID.
- **Streaming:** text can be streamed first, and interactive elements added at the end of the response.
