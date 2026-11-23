# User Profiles & Authentication

**Priority:** Low

## 1. Overview

### The problem

The agent currently protects its API with an API key, but it does not clearly know **who the user is**. Without a reliable user identity, the agent cannot save memory, preferences, or sessions for each user, and cannot treat logged-in users and guests differently.

### What the feature does

The feature gives the agent a clear and secure user identity:

- Supports user registration and login, or connects to GoCare's existing accounts.
- Manages user profiles, including preferences and settings.
- Identifies the same user across different sessions.
- Handles anonymous (guest) users and authenticated (logged-in) users differently.
- Encrypts sensitive profile data.

### Example

> A guest opens the chat and asks about sunscreens. The agent answers normally, but does not save long-term preferences.
>
> Later, she logs in. The agent now recognizes her, links the conversation to her profile, and can remember her skin type in future conversations.

## 2. Why It Matters

- **Foundation for personalization:** memory, preferences, and personalized responses all need a reliable user identity.
- **Security:** users can only access their own data, sessions, and carts.
- **Better experience for logged-in users:** saved preferences and history across devices.
- **Privacy:** sensitive profile data is protected.

## 3. Requirements

### Functional Requirements

- **FR-01: Registration and login:** users can register and log in, or the agent uses GoCare's existing login.
- **FR-02: Profile management:** users have a profile that stores their preferences and settings.
- **FR-03: User identification across sessions:** the same user is recognized in every session and on every device.
- **FR-04: Anonymous vs authenticated handling:** guests can chat with limited features, while logged-in users get full features such as memory and saved preferences.
- **FR-05: Profile data encryption:** sensitive profile data is encrypted.

### Non-Functional Requirements

- **Security:** authentication must use secure, standard methods, and tokens must be validated on every request.
- **Privacy:** profile data must follow data protection regulations in Saudi Arabia.
- **Performance:** checking the user identity must not slow down responses.
- **Compatibility:** must work with GoCare's existing user accounts, instead of creating a separate login.

## 4. Technical Approach

- **Reuse GoCare's authentication:** instead of building a new login system, the agent validates the token issued by GoCare's backend (e.g. a JWT) and reads the user ID from it.
- **User ID as the key:** the authenticated user ID is used to link sessions, memory, preferences, and carts.
- **Guest users:** generate a temporary guest ID stored on the device, with limited features and a short data retention period.
- **Guest to user:** when a guest logs in, the current conversation can be linked to the user's account.
- **Profile store:** store agent-specific profile data (e.g. language, communication style) in a profile table linked to the user ID.
- **Encryption:** encrypt sensitive fields at rest, and use HTTPS for all communication.

## 5. Dependencies & Risks

### Dependencies

- GoCare's existing user accounts and authentication service.
- Coordination with the Backend and Frontend teams to pass the user token to the agent.

### Risks

- **Identity spoofing:** if the agent trusts a user ID sent in the request instead of a validated token, users could access other users' data.
- **Duplicate identities:** the same person may appear as a guest and a logged-in user.
- **Two login systems:** building a separate login for the agent would confuse users.

## 6. MVP Scope

### In Scope

- Validating GoCare's user token and extracting the user ID.
- Linking sessions and conversations to the user ID.
- Basic guest handling with limited features.

### Out of Scope (for now)

- A separate registration and login system for the agent.
- Linking guest conversations to accounts after login.
- Full profile management screens.

## 7. Open Questions

- Does GoCare's backend issue tokens (e.g. JWT) that the agent can validate?
- Which features should guests have?
- Which profile fields are considered sensitive and need encryption?

## 8. Assessment

This feature is not very important at the moment. It is not important for the agent to know or say the user's name. What matters more is that the agent helps the user find what she wants.

### Example

> A user asks for a moisturizer for oily skin. It does not matter much if the agent says "Hello Sara". What matters is that it recommends the right moisturizer.
