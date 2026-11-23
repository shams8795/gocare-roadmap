# Automated Content Tagging

## 1. Feature Overview

**Automated Content Tagging** aims to automatically classify GoCare products and add the right attributes and categories to them, by reading product names and descriptions in Arabic and English, instead of entering this information manually for each product.

The feature has three main parts:

- **Category classification:** assigning each product to the correct category and sub-category (e.g. skin care, then cleanser).
- **Attribute extraction:** extracting product attributes from the text, such as suitable skin or hair type, key ingredients, scent, shade, size, and gender.
- **Bilingual support:** handling product content written in Arabic, English, or a mix of both.

**Example:**

For a product named "Niacinamide Gel Cleanser for Oily Skin", the system extracts: category = skin care, product type = cleanser, skin type = oily, key ingredient = niacinamide.

## 2. Current Website Status

Based on the review in this report:

- GoCare offers products across many categories, such as skin care, hair care, makeup, perfumes, personal care, men's care, and beauty devices.
- The website supports both Arabic and English.
- GoCare hosts products from different brands and sellers, so product names and descriptions may be written in different styles and languages.
- Products are already tagged with their type or routine step (e.g. cleanser, serum, shampoo). It is not yet confirmed whether they have other structured attributes, such as skin type and ingredients.

**What does this mean for the feature?**

- Product text already exists and can be used as input for the model.
- Inconsistent product descriptions make manual tagging slow, which is the main reason for this feature.
- Several other roadmap features depend on good product attributes, so this feature can support them.

## 3. Business Objective

The main goal is to make product data complete and consistent, which improves search, filtering, and recommendations, while reducing manual work.

**Expected benefits:**

- Less manual effort when adding new products.
- More consistent categories and attributes across all sellers and brands.
- Better search and filters, such as filtering by skin type or ingredient.
- Better recommendations, since recommendation features rely on product attributes.

**Example:**

The Skincare Routine Advisor needs each product to be tagged with skin type and ingredients. Products already have their routine step, so automated tagging can add the missing attributes to thousands of products instead of doing it manually.

**Business Impact:** Moderate, according to the client's assessment.

## 4. Client Clarification Questions

### 4.1 Questions for the Backend and Data Team

1.  How many products are in the catalog, and how many already have categories and attributes?
2.  Are product names and descriptions stored in both Arabic and English, or in one language only?
3.  Is there a database structure ready to store new attributes, such as skin type and ingredients?
4.  Are there already correctly tagged products that can be used to train or test the model?
5.  Is there an existing API for adding or updating product attributes?

### 4.2 Shared Question for the Client and Data Team

**What is the official list of tags?**

The client defines which categories and attributes should exist and what their allowed values are, and the data team confirms how they will be stored and used by search and recommendations.

## 5. Functional Requirements

**FR-01: Category classification**

The system must assign each product to the correct category and sub-category.

*Example:* a product named "Argan Oil Hair Mask" is classified as hair care, then hair mask.

**FR-02: Attribute extraction**

The system must extract product attributes from the product name and description.

*Example:* "Fragrance-free moisturizer for sensitive skin" gives skin type = sensitive and fragrance = free.

**FR-03: Arabic and English support**

The system must handle product text in Arabic, English, or a mix of both.

*Example:* the Arabic and English descriptions of the same product give the same tags.

**FR-04: Confidence score**

The system must give a confidence score for each tag, so low-confidence tags can be reviewed.

*Example:* skin type = oily (95% confidence) is applied directly, while scent = floral (55% confidence) is sent for review.

**Proposed additional requirements (need client confirmation):**

- **FR-05:** A review screen where the team can approve or correct suggested tags.
- **FR-06:** Suggesting tags to sellers while they add a new product.
- **FR-07:** Bulk tagging of the existing catalog.
- **FR-08:** Learning from manual corrections to improve future tags.

## 6. Non-Functional Requirements

**1. Accuracy**

Tags must be accurate enough to be used in search, filters, and recommendations, and their accuracy must be measured on a test set.

**2. Consistency**

The same type of product must always get the same tags, regardless of language or writing style.

**3. Performance**

Tagging a single product must be fast enough to work while a product is being added, and bulk tagging must be able to process the full catalog.

**4. Reviewability**

Every automatic tag must be traceable, so the team knows whether it was added by the model or by a person.

**5. Reliability**

A failure in the tagging service must not prevent products from being added or shown on the website.

*Note: target values for tagging accuracy and processing time must be defined with the technical team.*

## 7. Data Requirements

| Data                         | Purpose                              | Status                                          |
|------------------------------|--------------------------------------|-------------------------------------------------|
| Product Names & Descriptions | Main input for tagging               | Exists on the website                           |
| Arabic and English Content   | Bilingual tagging                    | Exists on the website; completeness unconfirmed |
| Current Categories           | Category classification              | Exists on the website                           |
| Official Attribute List      | Define which tags to extract         | Not available; needs to be agreed               |
| Correctly Tagged Products    | Train and test the model             | Unconfirmed                                     |
| Product Images (optional)    | Support tagging when text is missing | Exists on the website                           |

**Example:**

If product descriptions are very short, such as "Cream 50 ml", the model cannot reliably tell the skin type or ingredients, so these products may need manual review or images as extra input.

## 8. Technical Feasibility

The first version can be built with a combination of simple rules and Natural Language Processing:

- **Keyword and rule-based extraction:** detecting clear terms such as "oily skin", "بشرة دهنية", "niacinamide", or "shampoo".
- **Text classification models:** classifying products into categories using a multilingual model that supports Arabic and English.
- **Large Language Models (LLMs):** extracting structured attributes from product descriptions, with a fixed list of allowed values.

Later, improvements can be tested, such as:

- Fine-tuning a model on GoCare's correctly tagged products.
- Combining product text and images for better accuracy.

**Initial assessment:** technically feasible, especially with current multilingual models. The main effort is in agreeing on the official tag list and preparing a test set to measure accuracy.

## 9. Dependencies & Constraints

### Dependencies

- An agreed official list of categories and attributes.
- Access to product names and descriptions.
- A database structure to store the new attributes.
- A set of correctly tagged products for testing.
- Collaboration between the Data, Backend, and Recommendation teams, and the team that manages products.
- Coordination with features that use product attributes, such as Skincare Routine Advisor and Visual Search.

### Constraints & Risks

**1. Inconsistent product content**

Sellers and brands write product descriptions in different styles, lengths, and languages.

**2. Arabic language challenges**

Arabic product text may include different spellings, dialect words, or a mix of Arabic and English.

**3. Wrong tags**

Wrong tags can lead to wrong filters and wrong recommendations, such as recommending a product for the wrong skin type.

**4. Missing information**

Some products may not mention important attributes at all in their text.

**Example:**

If a cleanser is wrongly tagged as suitable for dry skin, the Skincare Routine Advisor may recommend it to the wrong users, which is why low-confidence tags must be reviewed.

------------------------------------------------------------------------

## Meeting Decisions

The following points were agreed in the meeting:

**1. The feature is important**

Automated Content Tagging is considered an important feature for GoCare, since complete and correct product information improves search, filters, and recommendations, and reduces manual work.

<div dir="rtl" style="text-align: right;">
<p><strong>مثال:</strong></p>
<p>تمت إضافة منتج جديد إلى الموقع باسم: <bdi>Niacinamide Gel Cleanser for Oily Skin</bdi>. يقرأ النظام الاسم ويضيف معلومات المنتج بنفسه، دون أن يكتبها أحد يدويًا:</p>
<ul>
<li><strong>نوع المنتج:</strong> غسول</li>
<li><strong>نوع البشرة:</strong> دهنية</li>
<li><strong>المكوّن الأساسي:</strong> النياسيناميد</li>
</ul>
<p>بعد ذلك، يمكن للعميلة أن تجد المنتج عندما تختار فلتر البشرة الدهنية، ويقترحه روتين العناية بالبشرة على العميلات ذوات البشرة الدهنية فقط.</p>
</div>
