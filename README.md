# 🍕 Pizza Order Recognition (NLP)

Extracting structured pizza-order information from raw customer text. This project converts free-form customer orders into structured records suitable for downstream use, such as order fulfillment, analytics, or UI confirmation.

---

## 📖 Table of Contents

<table>
  <tr>
    <td><a href="#project-summary">📌 Project Summary</a></td>
  </tr>
  <tr>
    <td><a href="#goals">🎯 Goals</a></td>
  </tr>
  <tr>
    <td><a href="#high-level-design--data-contract">🏗 High-Level Design & Data Contract</a></td>
  </tr>
  <tr>
    <td><a href="#repository-layout">📂 Repository Layout</a></td>
  </tr>
  <tr>
    <td><a href="#getting-started">🚀 Getting Started</a></td>
  </tr>
  <tr>
    <td><a href="#notebooks--scripts">📓 Notebooks & Scripts</a></td>
  </tr>
  <tr>
    <td><a href="#evaluation-artifacts">📊 Evaluation Artifacts</a></td>
  </tr>
  <tr>
    <td><a href="#common-issues--edge-cases">⚠️ Common Issues & Edge Cases</a></td>
  </tr>
  <tr>
    <td><a href="#next-steps--recommendations">➡️ Next Steps & Recommendations</a></td>
  </tr>
  <tr>
    <td><a href="#contributors">🤝 Contributors</a></td>
  </tr>
</table>

---

## 📝 Project Summary <a name="project-summary"></a>

This project focuses on recognizing pizza orders from natural language text and converting them into structured JSON-like order records. The repository includes:

- Data  preprocessing
- Embedding experiments (Word2Vec, FastText, trainable embeddings)
- Keras model for extracting order details
- Post-processing utilities to format predictions
- Scripts for preprocessing and formatting output  

The pipeline handles noisy inputs (misspellings, informal phrasing) and converts them into structured order records.

---

## 🎯 Goals <a name="goals"></a>

- Convert raw pizza-order utterances into structured JSON records.
- Reduce errors from noisy inputs using preprocessing and spelling-correction.
- Compare performance of static pretrained embeddings versus trainable embeddings.

---

## 🏗 High-Level Design & Data Contract <a name="high-level-design--data-contract"></a>

**Input:** A raw customer utterance (string) or a CSV column of utterances.  
**Output:** Structured object with at least:

- `order_items`: array of items, each containing:
  - `name` (string)
  - `quantity` (int)
  - `size` (string, optional)
  - `toppings/modifiers` (list of strings)
  - `special_instructions` (string, optional)
- `meta`: order-level fields like `order_type` (delivery/pickup), `address/contact` (if present), and `raw_text`.

**Error Handling:**

- Missing or ambiguous fields are handled with post-processing heuristics.
- Misspellings or unknown toppings are normalized using spelling-correction scripts.
- Multi-item utterances may require rule-based fixes in post-processing.

**Success Criteria:** Accurate extraction of item names and quantities on held-out test sets with post-processed output formatted for human comparison.

---

## 📂 Repository Layout <a name="repository-layout"></a>

- **Main branch**: Core README, LICENSE  
- **Order_details branch**: Data preprocessing, embedding experiments, model training, and post-processing  
- **Order-Categorization branch**: Experiments for order-type classification  
- **JSON_PARSER branch**: Conversion and parsing utilities  

---

## 🤝 Contributors <a name="contributors"></a>

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/Omar-Said-4" target="_black">
        <img src="https://avatars.githubusercontent.com/u/87082462?v=4" alt="Omar Said"/>
        <br />
        <sub><b>Omar Said</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/MostafaMagdyy" target="_black">
        <img src="https://avatars.githubusercontent.com/u/97239596?v=4" alt="Mostafa Magdy"/>
        <br />
        <sub><b>Mostafa Magdy</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/nouraymanh" target="_black">
        <img src="https://avatars.githubusercontent.com/u/102790603?v=4" alt="Nour Ayman"/>
        <br />
        <sub><b>Nour Ayman</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/3abqreno" target="_black">
        <img src="https://avatars.githubusercontent.com/u/102177769?v=4" alt="Abdelrahman Mohamed"/>
        <br />
        <sub><b>Abdelrahman Mohamed</b></sub>
      </a>
    </td>
  </tr>
</table>
