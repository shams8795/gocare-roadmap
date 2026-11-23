# Session Management

**Priority:** High · **Effort:** Medium

## 1. Overview

### The problem

A **session** is one conversation between a user and the agent, from when the chat is opened until it ends. Today, the agent does not manage sessions: there is no clear way to identify a conversation, continue it later, continue it on another device, or clean up old ones.

### What the feature does

The feature organizes conversations into sessions:

- Gives each session a unique ID and tracks it.
- Synchronizes the same session across devices.
- Ends inactive sessions and cleans up temporary data.
- Lets users resume a session where they left off.
- Lets the team monitor active sessions.

### Example

> The user starts a conversation on her phone, asking about a vitamin C serum. Later, she opens GoCare on her laptop and finds the same conversation, and continues from where she stopped.
>
> If she leaves the chat for a long time, the session is closed automatically, and its temporary data is cleaned up.

## 2. Why It Matters

- **Continuity:** users do not lose their conversation when they change devices or close the page.
- **Organized data:** every message belongs to a clear session and user.
- **Server health:** inactive sessions are cleaned up, saving resources.
- **Foundation for memory:** Conversation Memory Management needs sessions to know which messages belong together.

## 3. Requirements

### Functional Requirements

- **FR-01: Session identification and tracking:** each session has a unique ID linked to a user, with start time, last activity, and status.
- **FR-02: Multi-device synchronization:** a logged-in user can continue the same session on different devices.
- **FR-03: Session timeout and cleanup:** inactive sessions are closed after a set time, and temporary data is cleaned up.
- **FR-04: Session resume:** users can reopen and continue a previous session.
- **FR-05: Active session monitoring:** the team can see the number and status of active sessions.

### Non-Functional Requirements

- **Security:** session IDs must not be guessable, and users can only access their own sessions.
- **Performance:** creating and loading sessions must be fast.
- **Scalability:** sessions must work across multiple agent instances.
- **Reliability:** an expired or invalid session must be handled gracefully, for example by starting a new one.

## 4. Technical Approach

- **Session store:** store sessions in a shared database or cache, such as Redis or PostgreSQL, with fields like `session_id`, `user_id`, `created_at`, `last_activity`, and `status`.
- **Session ID:** generate secure, random IDs (e.g. UUIDs) on the server.
- **Link to LangGraph:** use the session ID as the LangGraph `thread_id`, so memory and checkpoints are tied to the session.
- **Multi-device:** for logged-in users, sessions are linked to the user ID instead of the device, so any device can load them.
- **Timeout and cleanup:** use an expiry time (e.g. a TTL in Redis) or a scheduled cleanup job.
- **Monitoring:** expose the number of active sessions through the existing health monitoring endpoints.

## 5. Dependencies & Risks

### Dependencies

- User authentication, to link sessions to users across devices.
- A shared session store.
- Coordination with the frontend, to store and send the session ID.

### Risks

- **Session hijacking:** if a session ID is exposed, someone else could access the conversation.
- **Wrong timeout:** too short annoys users; too long wastes resources.
- **Sync conflicts:** sending messages from two devices at the same time may cause ordering issues.
- **Guest users:** guests cannot be synced across devices without an account.

## 6. MVP Scope

### In Scope

- Session IDs and tracking.
- Session timeout and cleanup.
- Session resume on the same device.
- Basic active session count in health monitoring.

### Out of Scope (for now)

- Multi-device synchronization.
- Multiple conversations per user.
- A detailed monitoring dashboard.

## 7. Open Questions

- What is the right inactivity timeout (e.g. 30 minutes, 1 hour, 24 hours)?
- Should guest sessions be kept, and for how long?
- Should a user have one ongoing conversation, or multiple conversations they can choose from?

## 8. Business Impact

- **Lower server costs:** closing inactive sessions saves server resources, so costs do not grow without need.
- **Fewer lost customers:** users do not have to start over every time, so they are more likely to continue and buy.
- **Foundation for sales features:** Conversation Memory Management and personal recommendations cannot work without sessions.
- **Better planning for the team:** knowing the number of active sessions helps the team know when the system needs to scale.

### Example

> If 1,000 users open the chat and leave it, without session timeout the server keeps all 1,000 sessions open without need. With session timeout, they are closed automatically, and costs go down.
