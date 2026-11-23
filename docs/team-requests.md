# Team Requests

This page lists problems and requests reported by the GoCare team in existing tools.

## Product Codes Sheet

The team registers products in a sheet, using a code for each product. The team reported two problems:

### 1. No alert for duplicate codes

The sheet should show an alert when the same product code is entered more than once, but this does not happen today. As a result, the same product can be registered twice without anyone noticing.

### 2. Product sizes appear as separate products

When a product has more than one size, such as 40 ml and 90 ml, the website treats them as two different products, and each one appears in a different place.

### What the team needs

- **Duplicate alert:** the sheet shows an alert when a product code already exists.
- **Related sizes:** the different sizes of the same product are linked together as related products, so they appear together, and the user chooses the size from the same product page.

### Example

> A moisturizer is available in 40 ml and 90 ml.
>
> - **Today:** the two sizes appear as two separate products in different places on the website.
> - **What the team needs:** one product page shows the moisturizer, and the user chooses 40 ml or 90 ml from it.

## Catalog and Admin Panel Problems

The catalog team reported these problems while auditing products. Most of them are in the admin panel (Backend and Frontend work), and some are related to the Audit Agent and Description Enhancement (AI work).

### 1. Shades and Sizes

- **No shade field:** a lipstick has shades such as "Nude 01" and "Red 05". There is no dedicated shade field in the admin panel, so shades are written inside the description. As a result, users cannot filter products by shade.
- **Shades are duplicated after editing:** when the team changes "Nude 01" to "Nude 02", both shades appear together on the website.
- **Size is not visible in the admin panel:** the size appears to users on the website, but the team cannot see or edit it in the admin panel.
- **Size breaks the product:** adding a size changes the product status from "Successful" to "Failed". Writing the size in the title (such as "Cream 50 ml") causes an error, because the system needs a separate size field, and this field does not exist.

### 2. Titles

- **Unclear titles:** some titles say only "Cream", without the brand or the product type.
- **Bad formatting:** titles are not bold and have no space under them, so they look merged with the description.
- **Arabic changes to English:** any Arabic word written in the title is changed to English automatically.

### 3. Descriptions (only 65% pass the audit)

- **No standard structure:** each description should have 5 sections: Key Benefits, Ingredients/Materials, How to Use, Specifications, and Best Suited For. Most descriptions do not follow this structure.
- **Missing information:** ingredients and usage steps are often missing. When the supplier does not send them, the Audit Agent marks the product as failed.
- **Perfume notes are missing:** perfume listings do not include the top, middle, and base notes.
- **5 required fields are missing:** cruelty-free, vegan, made in, country of origin, and shelf life. These are the main reason why 35% of products fail the audit, and they also stop products from appearing in filters.

### 4. Admin Panel Workflow

- **No bulk selection:** the team cannot select many products and update them at once.
- **One product at a time:** each product must be opened, edited, and confirmed alone, which takes a very long time.
- **No default values:** when the supplier does not send a required field, such as country of manufacture, the system fails the product instead of filling a default value such as "Not Specified" or "Imported".

### 5. Suggested Fixes

- **New fields:** add Shade and Size fields in the admin panel.
- **Title formatting:** make titles bold, with space under them.
- **Standard template:** apply the 5-section structure to all descriptions.
- **Default values:** fill missing fields automatically, so products can pass the audit.
- **Correct categories:** classify products correctly, such as makeup brushes under beauty tools.
