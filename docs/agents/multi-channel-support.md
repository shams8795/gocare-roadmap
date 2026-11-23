# Multi-Channel Support

**Priority:** Medium

## 1. Overview

### The problem

The agent works only inside the website chat. But many customers in Saudi Arabia use WhatsApp and Instagram more than the website, so when they want to ask about a product, they have to open the website first.

### What the feature does

The feature lets the same agent answer customers in more than one place:

- **WhatsApp:** through the WhatsApp Business API.
- **Instagram:** answering DM messages.
- **Facebook Messenger.**
- **SMS messages.**
- **Email.**

It is the same agent, with the same knowledge, not a new chatbot.

### Example

> A user sees a GoCare ad on Instagram and sends a DM: "Is this serum suitable for sensitive skin?" The agent answers her in the same DM and sends her the product link.

## 2. Requirements

### Functional Requirements

- **FR-01: WhatsApp:** the agent receives and answers WhatsApp messages.
- **FR-02: Instagram:** the agent receives and answers Instagram DM messages.
- **FR-03: Facebook Messenger:** the agent receives and answers Messenger messages.
- **FR-04: SMS:** the agent can send and receive SMS messages.
- **FR-05: Email:** the agent can answer emails.

### Non-Functional Requirements

- **Same experience:** the agent answers with the same quality and style in every channel.
- **Message format:** the answer is adapted to each channel, because, for example, WhatsApp does not support the same buttons and cards as the website.
- **Compliance:** the agent follows each platform's rules, such as WhatsApp messaging rules.
- **Privacy:** customer data is protected in all channels.

## 3. Data Requirements

- **WhatsApp Business API account:** an official, active account, a dedicated phone number, and message templates approved by Meta. This is the same account needed for Churn Prediction.
- **Social media account access:** access to GoCare's Instagram and Facebook accounts, so the agent can read and answer messages.
- **Linking the user's identity across channels:** a way to know that a WhatsApp number belongs to the same user who has an account on the website, usually through the phone number.
- **Message format rules for each channel:** what is allowed in each channel (images, links, buttons, message length), so the answer is displayed correctly.
- **Conversation logs from all channels:** all conversations are saved in one place, with the name of the channel they came from.

## 4. Assessment

In my view, only WhatsApp is important at the moment, and the other channels can wait:

- Users already confirm their orders on WhatsApp, so this is where they are.
- The WhatsApp Business API is already needed for Churn Prediction, so the same work serves both features.
- Instagram, Facebook, SMS, and email need very high effort and have less value now.
