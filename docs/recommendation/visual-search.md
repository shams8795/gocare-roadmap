# Visual Search

## 1. Feature Overview

**Visual Search** allows GoCare users to upload an image and find similar products in the store, instead of searching by text when they don't know the product name.

The feature has three main parts:

- **Image upload:** the user uploads a photo or screenshot from the search bar.
- **Visual product matching:** a computer vision model compares the uploaded image with product images in the store.
- **Similar products results:** the system shows the most visually similar in-stock products.

**Example:**

A user sees a lipstick shade she likes in a social media photo. She uploads the screenshot, and GoCare shows the closest lipstick shades available in the store.

## 2. Current Website Status

Based on the review in this report:

- GoCare has a text search bar ("Search for products") on every page.
- The store includes visual product categories such as makeup, perfumes, beauty devices, and gift sets.
- There is no image-based search on the website currently.

**What does this mean for the feature?**

- Visual Search can be added next to the existing search bar.
- Product images already exist and can be used to build the image index.

## 3. Business Objective

The main goal is to help users find products they saw elsewhere, even when they don't know the name, and turn that interest into a purchase on GoCare.

**Expected benefits:**

- Easier product discovery for users who don't know product names.
- Higher conversion from social media inspiration to purchases.
- A modern search experience that differentiates GoCare from competitors.
- Fewer failed searches with no results.

**Example:**

Instead of typing "pink matte lipstick" and getting many unrelated results, the user uploads a photo and directly sees the closest matching shades.

**Business Impact:** High, according to the client's assessment.

## 4. Client Clarification Questions

### 4.1 Questions for the Backend and Data Team

1.  Does every product have at least one clear, good-quality image?
2.  Are product images stored in a way that allows processing them in bulk?
3.  Is there existing infrastructure for running computer vision models (e.g. GPU or a cloud vision service)?
4.  Can the search backend support a new image-based search endpoint?
5.  Is product color or shade stored as structured data?

## 5. Functional Requirements

**FR-01: Image upload**

The system must allow users to upload an image or take a photo from the search bar.

**FR-02: Visual product matching**

The system must find store products that are visually similar to the uploaded image.

*Example:* an uploaded photo of a red perfume bottle returns perfumes with similar bottle shape and color.

**FR-03: Similar products results**

The system must show a list of similar, in-stock products, ordered by similarity.

**FR-04: Filtering results**

The user must be able to filter visual search results by category, price, or brand.

**Proposed additional requirements (need client confirmation):**

- **FR-05:** Visual Search inside the chatbot.
- **FR-06:** Cropping the uploaded image to focus on a specific product.
- **FR-07:** Suggesting related products, such as products that complete the same look.

## 6. Non-Functional Requirements

**1. Performance**

Results must appear within a few seconds of uploading the image.

**2. Accuracy**

The most similar products must appear at the top of the results.

**3. Scalability**

The system must handle growth in the number of products and searches.

**4. Privacy & Security**

Uploaded images must be handled securely, not shared, and deleted when no longer needed, in line with data protection regulations in Saudi Arabia.

**5. Reliability**

If Visual Search fails, text search must keep working normally.

*Note: target values for response time and search accuracy must be defined with the technical team.*

## 7. Data Requirements

| Data                  | Purpose                       | Status                                      |
|-----------------------|-------------------------------|---------------------------------------------|
| Product Images        | Build the visual search index | Exists on the website; quality needs review |
| Product Categories    | Filter and organize results   | Exists on the website                       |
| Product Color / Shade | Improve matching for makeup   | Unconfirmed                                 |
| Stock Availability    | Show only available products  | Unconfirmed                                 |
| Search Logs           | Measure and improve results   | Not collected yet for image search          |

**Example:**

If some products have low-quality images or images with busy backgrounds, the model may match them incorrectly, so product images must be reviewed first.

## 8. Technical Feasibility

The first version can be built using a pre-trained computer vision model:

- Convert each product image into a numerical representation (image embedding).
- Store the embeddings in a vector search index.
- Convert the uploaded image the same way and find the closest product embeddings.

Later, improvements can be tested, such as:

- Fine-tuning the model on GoCare's product images.
- Combining image and text matching for better results.

**Initial assessment:** technically feasible using existing pre-trained models, provided that product images are of reasonable quality and infrastructure for running the model is available.

## 9. Dependencies & Constraints

### Dependencies

- Good-quality product images.
- Infrastructure for running the vision model and the vector search index.
- Integration with the existing search bar on the website.
- Collaboration between the Backend, Frontend, and Recommendation teams.

### Constraints & Risks

**1. Image quality**

User photos may be blurry, dark, or include many objects.

**2. Similar-looking products**

Many beauty products look alike, such as bottles of different perfumes.

**3. Infrastructure cost**

Running vision models may need extra computing resources.

**4. Privacy**

Uploaded images may include faces or personal information.

**Example:**

If a user uploads a selfie to find a lipstick shade, the system must focus on the lipstick color and must not store the user's face.

------------------------------------------------------------------------

## Meeting Decisions

The following points were agreed in the meeting:

**1. The feature is approved**

The team has no objections to the Visual Search feature, and it can move forward as described in this page.

**2. The feature is important**

Visual Search is considered an important feature for GoCare, since it helps users find products they saw elsewhere, even when they do not know the product name.

**3. All product categories are included**

Visual Search covers all product categories, not only visual categories such as makeup and perfumes.

**4. Visual Search appears in the search bar**

Users access Visual Search from the existing search bar on the website.

**5. Closest results when there is no exact match**

If no similar product is found, the system shows the closest available results instead of an empty "no results" message.

**6. Storing uploaded images depends on cost**

Whether uploaded images are stored, or only used during the search, will be decided based on the storage cost.

**7. "Similar" means the same shape and brand, and the same color for makeup**

A product is considered similar to the uploaded image when it has the same shape and the same brand. For makeup products, such as lipstick, the color or shade is also used.

<div dir="rtl" style="text-align: right;">
<p><strong>مثال:</strong></p>
<p>مستخدمة ترى لون أحمر شفاه يعجبها في صورة على <bdi>Instagram</bdi>، لكنها لا تعرف اسمه.</p>
<ol>
<li>ترفع الصورة في شريط البحث في <bdi>GoCare</bdi>.</li>
<li>يعرض لها <bdi>GoCare</bdi> أقرب درجات أحمر الشفاه المتوفرة في المتجر، فتشتري إحداها.</li>
</ol>
</div>
