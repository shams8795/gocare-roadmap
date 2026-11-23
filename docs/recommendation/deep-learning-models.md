# Deep Learning Models

## 1. Feature Overview

### The problem

Simple recommendation and search models work well at the start, but they have limits:

- They understand simple relationships between users and products, but miss more complex patterns.
- They understand product text by keywords only, not by meaning.
- They struggle with Arabic text, which has many spellings, forms, and dialects.

### What the feature does

**Deep Learning Models** introduce more advanced models that understand users, products, and text more deeply. The roadmap describes three parts:

- **Neural Collaborative Filtering (NCF):** the same idea as collaborative filtering ("users similar to you bought this"), but using a neural network that can learn more complex patterns.
- **Transformer-based product embeddings:** converting each product into a list of numbers that represents its meaning, so similar products have close numbers, even if their names are different.
- **BERT for Arabic text understanding:** a language model trained on Arabic that understands the meaning of Arabic text, useful for search, tagging, and review analysis.

**Example:**

| Case                                            | Simple model                                                                 | Deep learning model                                          |
|-------------------------------------------------|------------------------------------------------------------------------------|--------------------------------------------------------------|
| User searches "كريم للبشرة الناشفة"             | Looks for the exact words, may miss products written as "مرطب للبشرة الجافة" | Understands that both mean the same thing                    |
| Two serums with different names but similar use | Treats them as unrelated                                                     | Their embeddings are close, so they are recommended together |
| Review: "تحفة، استخدمته يومين وطلعلي حبوب"      | May classify it as positive because of "تحفة"                                | Understands that the meaning is negative                     |

In short, deep learning models make recommendations, search, and text understanding smarter, especially for Arabic.

## 2. Current System Status

Based on the information available in this report:

- GoCare already has a product recommendation system in production.
- The roadmap plans simpler approaches first, such as rule-based recommendations and Collaborative Filtering.
- The website supports Arabic and English, and product content and reviews are written in both.
- It is not yet confirmed what computing resources (CPU or GPU) are available.

**What does this mean for the feature?**

- Deep learning models should come after simpler models are in place and measured.
- They need more data and more computing resources than the current models.

## 3. Business Objective

The main goal is to improve the quality of recommendations, search, and text understanding, especially for Arabic content, once enough data is available.

**Expected benefits:**

- **More accurate recommendations:** learning complex user preferences.
- **Better search:** finding products by meaning, not only exact words.
- **Better Arabic understanding:** supporting Automated Content Tagging and Sentiment Analysis.
- **Shared product representations:** the same product embeddings can be reused by recommendations, search, Visual Search, and the chatbot.

**Example:**

With product embeddings, a user who likes a specific niacinamide serum can be recommended other serums with similar effects, even from different brands with different names.

**Priority:** Medium, according to the roadmap.

## 4. Clarification Questions

### 4.1 Questions for the Team Lead / Client

**1. Which use case should come first?**

Recommendations (NCF), product embeddings for search and similarity, or Arabic text understanding (BERT)?

**2. What improvement would justify the extra cost?**

For example, a clear increase in click-through or conversion compared to the simpler models.

**3. Is there a budget for GPU resources?**

Deep learning models often need GPUs for training, and sometimes for serving.

### 4.2 Questions for the Backend and Data Team

1.  How much interaction data is available for training NCF?
2.  Are product names and descriptions available in Arabic and English for embeddings and BERT?
3.  What computing resources are available for training and serving models?
4.  How are models currently deployed and monitored?
5.  Is there a labeled Arabic dataset, such as tagged products or labeled reviews, for fine-tuning BERT?

### 4.3 Shared Question

**When should deep learning replace or extend the simpler models?**

The team lead agrees on the success criteria, and the technical team compares the deep learning models with the simpler models on the same data before deciding.

## 5. Functional Requirements

**FR-01: Neural Collaborative Filtering**

The system must train a neural network on user-product interactions to predict which products each user may like.

**FR-02: Product embeddings**

The system must create an embedding for each product using a Transformer model, based on its name, description, and attributes.

*Example:* two moisturizers for dry skin from different brands have close embeddings.

**FR-03: Arabic text understanding**

The system must use an Arabic-capable BERT model to understand Arabic product text, search queries, and reviews.

*Example:* "بشرة ناشفة" and "بشرة جافة" are understood as the same meaning.

**FR-04: Comparison with existing models**

Each deep learning model must be compared with the current or simpler model before it is used in production.

**Proposed additional requirements (need confirmation):**

- **FR-05:** Reusing product embeddings in search, Visual Search, and the chatbot.
- **FR-06:** Fine-tuning BERT on GoCare's own Arabic data.
- **FR-07:** Regular retraining with new data.

## 6. Non-Functional Requirements

**1. Performance**

Model responses must be fast enough for real-time use on the website.

**2. Cost**

Training and serving costs must be justified by the improvement in results.

**3. Quality**

Deep learning models must perform better than simpler models on agreed metrics before replacing them.

**4. Maintainability**

Models must be documented, versioned, and easy to retrain.

**5. Reliability**

If a deep learning model fails, the system must fall back to the simpler model.

*Note: target values for response time, cost, and quality improvement must be defined with the technical team.*

## 7. Data Requirements

| Data                                              | Purpose                                  | Status                                                       |
|---------------------------------------------------|------------------------------------------|--------------------------------------------------------------|
| User Interactions                                 | Train Neural Collaborative Filtering     | Partly available (purchases); other interactions unconfirmed |
| Product Names & Descriptions (Arabic and English) | Create product embeddings and train BERT | Exists on the website                                        |
| Product Attributes                                | Improve embeddings                       | Exists; completeness needs review                            |
| Search Queries                                    | Improve search understanding             | Unconfirmed                                                  |
| Labeled Arabic Data                               | Fine-tune BERT                           | Not available; needs to be prepared                          |
| Computing Resources (GPU)                         | Train and serve models                   | Unconfirmed                                                  |

**Example:**

If GoCare has only a few thousand interactions, a neural collaborative filtering model may perform worse than simple matrix factorization, because deep models need much more data.

## 8. Technical Feasibility

All three parts use well-known approaches:

- **Neural Collaborative Filtering** can be built with standard deep learning libraries.
- **Product embeddings** can start from pre-trained multilingual Transformer models, without training from scratch.
- **Arabic BERT models** are publicly available and pre-trained on Arabic text, and can be fine-tuned on GoCare's data.

The recommended approach is to start with pre-trained models and fine-tune them, instead of training large models from scratch.

**Initial assessment:** technically feasible, but it requires more data, more computing resources, and more expertise than simpler models. It should come after the simpler models are in place and measured.

## 9. Dependencies & Constraints

### Dependencies

- Enough interaction and text data.
- GPU or cloud computing resources.
- Simpler baseline models, such as Collaborative Filtering, for comparison.
- Model Compression, to reduce the size and cost of the deep learning models.
- The Analytics Dashboard, to measure the impact.
- Collaboration between the Data, Backend, and Recommendation teams.

### Constraints & Risks

**1. Data requirements**

Deep models need much more data than simple models to perform well.

**2. Cost**

Training and serving deep models can be expensive.

**3. Complexity**

Deep models are harder to build, debug, explain, and maintain.

**4. Arabic dialects**

Pre-trained Arabic models may not fully understand local dialects and mixed Arabic-English text without fine-tuning.

**Example:**

If a deep learning model improves click-through by only 1% but doubles server costs, it may not be worth using in production.

------------------------------------------------------------------------

## Meeting Decisions

The feature is not important at the moment.
