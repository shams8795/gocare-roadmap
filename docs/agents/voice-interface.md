# Voice Interface

**Priority:** Low

## 1. Overview

### The problem

Some users prefer to speak instead of typing, especially on mobile. Many users in Saudi Arabia send voice notes on WhatsApp. The agent currently understands only written text.

### What the feature does

- **Speech-to-text for voice queries:** the user speaks, and the agent understands.
- **Text-to-speech responses:** the agent answers with voice.
- **WhatsApp voice message support:** the agent understands voice notes sent on WhatsApp.
- **Voice command shortcuts:** such as "Where is my order?" by voice.

### Example

> A user sends a voice note on WhatsApp: "I have dry skin and I want a good moisturizer." The agent converts the voice to text and answers her with recommendations.

## 2. Requirements

### Functional Requirements

- **FR-01: Speech-to-text:** the agent converts voice messages into text.
- **FR-02: Text-to-speech:** the agent can answer with a voice message.
- **FR-03: WhatsApp voice notes:** the agent understands voice notes from WhatsApp.
- **FR-04: Voice commands:** the agent understands short voice commands.

### Non-Functional Requirements

- **Dialect accuracy:** speech-to-text must understand the Saudi dialect well.
- **Speed:** voice conversion must not delay the answer much.
- **Privacy:** voice recordings are stored securely, or deleted after conversion.

## 3. Data Requirements

- **Speech-to-text service:** a service that supports Arabic and the Saudi dialect, such as Whisper or a cloud service, with its cost per minute.
- **Saudi voice samples:** real recordings of customer questions in the Saudi dialect, to test conversion accuracy before launching the feature.
- **Product and brand names:** a list of brand and product names, because they are often foreign, and the voice service may understand them incorrectly.
- **Text-to-speech service:** if the agent answers with voice, a natural Arabic voice that fits GoCare's style is needed.
- **Recording storage rules:** how long recordings are kept, or whether they are deleted right after conversion.

## 4. Assessment

In my view, this feature is not important at the moment:

- The effort is very high.
- It needs Multi-Channel Support (WhatsApp) to be built first.
- The Saudi dialect and brand names make conversion accuracy harder.
- Later, we can start with a small part only: understanding WhatsApp voice notes.
