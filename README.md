# 💳 Retail Banking RFM Segmentation

A data-driven segmentation project that applies **RFM analysis** (Recency, Frequency, Monetary) and **unsupervised machine learning** to classify customers of a fictional retail bank based on their transaction behavior.

---

## 📌 Project Highlights

* Cleaned and preprocessed over 1 million bank transaction records.
* Calculated RFM metrics to understand customer behavior.
* Scored and ranked customers into segments (e.g. Best, Loyal, At Risk, Churned).
* Created **Weighted RFM Scores** to enhance targeting accuracy.
* Applied **K-Means Clustering** to reveal hidden customer patterns.
* Visualized distributions and segments using histograms, boxplots, and 3D plots.
* Outputted final CSV file for business consumption or deployment.

---

## 📂 Folder Structure

```
📁 data/                → Raw input dataset (bank_data_C.csv)
📁 notebook/            → Jupyter notebook (solution.ipynb) with full step-by-step analysis
📁 output/              → Exported customer segments (RFM_segmented_customers.csv)
📁 venv/                → Virtual environment (excluded from GitHub)
📄 requirements.txt     → Python dependencies
📄 README.md            → Project overview and setup guide
```

---

## 🛠️ Tech Stack

* **Python 3.9+**
* **Jupyter Notebook / VS Code**
* **Libraries:**

  * `pandas`, `numpy`, `matplotlib`, `seaborn`
  * `scikit-learn`, `yellowbrick`, `dateutil`

---

## 🚀 Quick Start

1. **Clone this repo**

   ```bash
   git clone https://github.com/your-username/retail-banking-rfm.git
   cd retail-banking-rfm
   ```

2. **Create virtual environment**

   ```bash
   python -m venv venv
   venv\Scripts\activate    # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the analysis**
   Open `notebook/solution.ipynb` in Jupyter Notebook or VS Code and run all cells.

---

## 📊 Outputs

* `RFM_Score`: Based on quantile scoring (1–4) across Recency, Frequency, and Monetary.
* `Segment`: Categorical grouping (e.g. Best, Loyal, Churned).
* `Cluster`: Group assigned using KMeans unsupervised learning.
* `Weighted Score`: Recency × 2 + Frequency + Monetary for business prioritization.

---

## 🔮 Streamlit Dashboard (Optional)

To deploy this segmentation model as an interactive dashboard:

```bash
streamlit run streamlit_app.py
```

*(Streamlit app development ongoing — coming soon!)*

---

## 👤 Author

Enoch Hagan • [@LinkedIn](https://www.linkedin.com/in/ehagan1)

---

## 📄 License

MIT License — feel free to reuse with credit.

---

> *Empowering smarter banking strategies through data.*
