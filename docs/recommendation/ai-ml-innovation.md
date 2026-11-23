# AI/ML Innovation

## 1. Feature Overview

### The problem

As GoCare's AI systems grow, three challenges appear:

- Models are trained once and do not improve by themselves from user reactions.
- Neither users nor the team know **why** a product was recommended.
- Choosing and tuning models takes a lot of manual effort from the team.

### What the feature does

**AI/ML Innovation** introduces three advanced approaches:

- **Reinforcement Learning (RL) for dynamic optimization:** a model that learns by trying. It recommends something, observes whether the user clicks or buys, and improves itself over time.
- **Explainable AI (XAI):** the system explains why it made a recommendation or prediction.
- **AutoML integration:** tools that automatically try many models and settings, and choose the best one.

**Example:**

| Approach               | Example                                                                                                         |
|------------------------|-----------------------------------------------------------------------------------------------------------------|
| Reinforcement Learning | The homepage tries different product orders, learns which order leads to more purchases, and keeps improving it |
| Explainable AI         | "Recommended because you bought a cleanser for oily skin"                                                       |
| AutoML                 | Instead of the team manually testing 10 models for Demand Forecasting, AutoML tests them and picks the best     |

In short, these approaches make the AI systems self-improving, understandable, and easier to build.

## 2. Current System Status

Based on the information available in this report:

- GoCare has a recommendation system and plans several AI features, such as Demand Forecasting, Churn Prediction, and Collaborative Filtering.
- The current models are trained and tuned manually.
- It is not yet confirmed whether recommendation results are explained to users.

**What does this mean for the feature?**

- These approaches build on the other AI features, so they come after them.
- They improve how all models are built, measured, and explained.

## 3. Business Objective

The main goal is to make GoCare's AI systems continuously improve, more trustworthy, and faster to develop.

**Expected benefits:**

- **Continuous improvement:** recommendations and placements improve automatically from user feedback.
- **More trust:** users and the team understand why the system makes each decision.
- **Faster development:** less manual work to choose and tune models.
- **Easier debugging:** explanations help the team find and fix wrong results.

**Example:**

If Churn Prediction marks a customer as high-risk, Explainable AI shows the reasons, such as "no purchase in 90 days" and "fewer visits", so the marketing team knows how to act.

**Priority:** Long-term vision, according to the roadmap.

## 4. Clarification Questions

### 4.1 Questions for the Team Lead

**1. Which approach should come first?**

Explainable AI, AutoML, or Reinforcement Learning?

**2. Where should explanations appear?**

To users on the website, to the internal team only, or both?

**3. Which problems should Reinforcement Learning optimize?**

For example, the order of recommendations, discount levels, or notification timing?

**4. Is there a budget for AutoML tools or cloud services?**

### 4.2 Questions for the Backend and Data Team

1.  Is user feedback (clicks, purchases) logged quickly enough to train Reinforcement Learning models?
2.  Is there an A/B testing setup that can safely test new strategies?
3.  Which models are currently in production, and how are they trained and deployed?
4.  Is there a model monitoring setup?

### 4.3 Shared Question

**How do we safely test self-learning systems?**

The team lead agrees on safety limits, and the technical team confirms how to test and monitor them.

## 5. Functional Requirements

**FR-01: Reinforcement Learning optimization**

The system must learn from user feedback to improve a chosen decision, such as the order of recommendations.

**FR-02: Explanations for recommendations**

The system must provide a simple reason for each recommendation.

**FR-03: Explanations for predictions**

Prediction models, such as Churn Prediction, must show the main factors behind each result.

**FR-04: AutoML model selection**

The team must be able to use AutoML to automatically compare and select models for a given problem.

**Proposed additional requirements (need confirmation):**

- **FR-05:** Showing explanations to users on the website.
- **FR-06:** Safety limits for Reinforcement Learning, such as maximum discount.
- **FR-07:** Dashboards for model explanations and performance.

## 6. Non-Functional Requirements

**1. Safety**

Self-learning systems must work within clear limits and be easy to stop.

**2. Transparency**

Explanations must be simple and correct.

**3. Reliability**

If an advanced model fails, the system must fall back to a simpler model.

**4. Monitoring**

Model performance must be monitored continuously.

**5. Cost**

Tools and compute resources must be justified by the improvement in results.

## 7. Data Requirements

| Data                              | Purpose                      | Status                                          |
|-----------------------------------|------------------------------|-------------------------------------------------|
| User Feedback (clicks, purchases) | Train Reinforcement Learning | Partly available; real-time logging unconfirmed |
| Model Inputs & Outputs            | Generate explanations        | Depends on each model                           |
| Training Datasets                 | AutoML experiments           | Depends on each feature                         |
| A/B Testing Results               | Safely test new strategies   | Not collected yet                               |

## 8. Technical Feasibility

- **Explainable AI:** standard methods, such as SHAP, can explain many models. Simple rule-based explanations can also be used for recommendations.
- **AutoML:** many tools and cloud services exist for automatic model selection and tuning.
- **Reinforcement Learning:** simple forms, such as multi-armed bandits, are practical for testing and optimizing recommendation orders. Full Reinforcement Learning is more complex and risky.

**Initial assessment:** Explainable AI and AutoML are technically feasible and relatively low-risk. Reinforcement Learning is feasible in simple forms, but needs careful testing and safety limits.

## 9. Dependencies & Constraints

### Dependencies

- Models from other features, such as Collaborative Filtering, Demand Forecasting, and Churn Prediction, once they are built.
- The Analytics Dashboard and A/B testing setup.
- Model monitoring and deployment processes.
- Collaboration between the Data, Backend, and Recommendation teams.

### Constraints & Risks

**1. Unsafe learning**

Reinforcement Learning may learn strategies that increase clicks but hurt long-term trust or profit.

**2. Misleading explanations**

Simplified explanations may not fully reflect how the model works.

**3. Over-reliance on AutoML**

AutoML may choose models that are hard to understand or maintain.

**4. Complexity and cost**

These approaches add complexity to the system.

**Example:**

If a Reinforcement Learning model learns that showing only discounted products increases clicks, it may reduce profit, which is why it must be limited and monitored.

------------------------------------------------------------------------

## Assessment

**Overall: not a priority for now**

In my view, this feature should be postponed as a whole. However, each part is different in effort and value:

| Part                            | Effort    | Importance now      |
|---------------------------------|-----------|---------------------|
| Explainable AI (simple version) | Very easy | Medium, worth doing |
| AutoML                          | Easy      | Low                 |
| Reinforcement Learning          | Hard      | Very low            |

**1. Explainable AI (simple version): easy and worth doing**

The simple version does not need AI. When a product is recommended because of another product the customer bought, we show the reason next to it, such as: *"Recommended because you bought a cleanser for oily skin."* This should take about one or two days, if the recommendation system already knows why each product was recommended. It also helps customers trust the recommendations more.

**2. AutoML: easy, but not needed now**

Ready-made libraries can do this with a few lines of code. However, it is useful only when there are many models and a lot of data. Since most models were postponed because data is still limited, it would not make a real difference now.

**3. Reinforcement Learning: hard, and not the right time**

- It needs a very large number of visitors for the model to learn quickly.
- It needs an A/B testing and monitoring setup.
- It carries a risk: the model may learn the wrong behavior, such as showing only discounted products because they get more clicks, which reduces profit.

**Suggestion:** postpone the feature, and start only with the simple version of Explainable AI, since it is easy and gives value quickly.
