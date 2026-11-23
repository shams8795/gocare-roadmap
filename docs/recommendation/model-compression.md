# Model Compression

## 1. Feature Overview

**Model Compression** is an internal technical improvement that reduces the size of GoCare's recommendation models by 30–50% using model quantization, enabling faster loading times and lower memory usage.

This is not a user-facing feature. Users will not see a new screen, but they may notice faster recommendations.

The improvement has three main parts:

- **Quantization:** storing model weights with lower numerical precision (e.g. from 32-bit to 8-bit), which reduces model size.
- **Performance testing:** measuring loading time, memory usage, and response time before and after compression.
- **Quality validation:** making sure recommendation quality does not drop significantly after compression.

**Example:**

A recommendation model of 400 MB is compressed to about 200–280 MB. It loads faster when the service starts and uses less server memory, while giving nearly the same recommendations.

## 2. Current System Status

Based on the information available in this report:

- GoCare runs a product recommendation system in production.
- The size, format, and loading time of the current models are not yet confirmed.
- It is not yet confirmed whether the models run on CPU or GPU servers.

**What does this mean for the improvement?**

- The current models must be measured first, to know the actual gain from compression.
- The best compression method depends on the model type and the server it runs on.

## 3. Business Objective

The main goal is to make the recommendation system faster and cheaper to run.

**Expected benefits:**

- Faster service startup and recommendation responses.
- Lower memory usage and possibly lower server costs.
- Easier scaling when the number of users grows.
- Room to run more models, such as Visual Search, on the same servers.

**Example:**

If each model uses half the memory, the same server can run two models instead of one.

**Priority:** Medium, according to the roadmap.

## 4. Clarification Questions

### 4.1 Questions for the Team Lead / Client

**1. What is the main goal of compression?**

Faster responses, lower server costs, or freeing resources for new models?

**2. How much quality loss is acceptable?**

For example, is a 1–2% drop in recommendation accuracy acceptable in exchange for a 50% smaller model?

**3. Which models should be compressed first?**

All recommendation models, or only the largest ones?

### 4.2 Questions for the Backend and Data Team

1.  Which models are used in production, and what are their sizes and formats?
2.  Do the models run on CPU or GPU?
3.  What are the current loading time, memory usage, and response time?
4.  Is there an offline evaluation dataset to compare recommendation quality before and after compression?
5.  How are models deployed, and can a compressed model be tested side by side with the current one?

### 4.3 Shared Question

**How will we decide that a compressed model is good enough?**

The team lead agrees on the acceptable quality and speed thresholds, and the technical team confirms they can be measured.

## 5. Functional Requirements

**FR-01: Compress recommendation models**

The models must be compressed using quantization, reducing their size by 30–50%.

**FR-02: Keep the same outputs format**

The compressed models must return recommendations in the same format, so no changes are needed in other systems.

**FR-03: Measure performance before and after**

Size, loading time, memory usage, and response time must be measured for both versions.

**FR-04: Validate recommendation quality**

Recommendation quality must be compared between the original and compressed models.

**Proposed additional requirements (need confirmation):**

- **FR-05:** The ability to quickly switch back to the original model if problems appear.
- **FR-06:** A/B testing of the compressed model with real users before full rollout.

## 6. Non-Functional Requirements

**1. Performance**

Loading time and memory usage must decrease noticeably after compression.

**2. Quality**

Recommendation quality must stay within the agreed acceptable limit.

**3. Reliability**

Replacing the model must not cause downtime in the recommendation service.

**4. Maintainability**

The compression steps must be documented and repeatable whenever models are retrained.

*Note: target values for size reduction, speed, and acceptable quality loss must be defined with the technical team.*

## 7. Data Requirements

| Data                        | Purpose                         | Status               |
|-----------------------------|---------------------------------|----------------------|
| Current Model Files         | Apply compression               | Exists in production |
| Model Size & Format         | Choose the compression method   | Unconfirmed          |
| Current Performance Metrics | Compare before and after        | Unconfirmed          |
| Evaluation Dataset          | Validate recommendation quality | Unconfirmed          |
| Server Specifications       | Choose CPU or GPU optimizations | Unconfirmed          |

**Example:**

Without an evaluation dataset, we cannot prove that the compressed model gives recommendations as good as the original one.

## 8. Technical Feasibility

Quantization is a standard and well-supported technique:

- **Post-training quantization:** compressing an already trained model, without retraining. This is the fastest option.
- **Quantization-aware training:** retraining the model with quantization in mind, if quality drops too much.

The method depends on the model type. For example, embedding-based recommendation models can often have their embeddings stored at lower precision with little quality loss.

**Initial assessment:** technically feasible, and usually low-risk, provided that the current models and an evaluation dataset are available.

## 9. Dependencies & Constraints

### Dependencies

- Access to the production models and their training code.
- An evaluation dataset and quality metrics.
- A testing environment similar to production.
- Collaboration with the Backend / DevOps team for deployment.

### Constraints & Risks

**1. Quality loss**

Some models may lose more accuracy than expected after compression.

**2. Hardware support**

Some quantized formats run faster only on specific hardware.

**3. Limited gain**

If the models are already small, the improvement may not be worth the effort.

**4. Retraining process**

If compression is not added to the training pipeline, it must be repeated manually every time models are retrained.

**Example:**

If a model is compressed by 50% but its response time does not improve on the current servers, the main gain will be lower memory only.

------------------------------------------------------------------------

## Assessment

**Importance: Medium to Low (for now)**

- This is an internal improvement, so users will not notice a big difference, and it does not directly increase sales.
- Its real value depends on the current model sizes and server load, which are not measured yet.
- Its importance increases if recommendations are slow, server costs are high, or heavier models such as Visual Search need to run on the same servers.

**Suggestion:** measure the current models first, and decide on compression based on the results.
