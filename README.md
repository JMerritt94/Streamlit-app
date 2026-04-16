# Semmelweis Hand-Washing Study - Interactive Dashboard

## Project Overview

This Streamlit application presents an interactive analysis of the famous Semmelweis dataset, which documents mortality rates in two hospital clinics from 1841-1849. The data shows the dramatic impact of hand-washing practices on reducing childbed fever deaths.

### Key Features

- **Interactive Visualizations**: Line charts and bar charts showing mortality trends
- **Time Period Filters**: Explore data across different year ranges
- **Clinic Comparison**: Compare mortality rates between Clinic 1 and Clinic 2
- **Mortality Metrics**: Real-time calculations of mortality rates per 100 births
- **Historical Context**: Comprehensive explanation of the historical significance

### The Story

Dr. Ignaz Semmelweis discovered that mandatory hand-washing could reduce maternal mortality by over 85%. In 1847, when he introduced hand-washing protocols in Clinic 1:
- Mortality rate dropped from **18.3%** to **1.3%**
- Clinic 2 (where midwives practiced) already had lower rates due to different procedures
- This provided early evidence of germ transmission, long before germ theory was accepted

---

## How to Run Locally

### Prerequisites
- Python 3.7+
- pip

### Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/semmelweis-dashboard.git
   cd semmelweis-dashboard
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Place your CSV file** in the project directory
   - The app looks for `yearly_deaths_by_clinic-1.csv`
   - Or create a `data/` folder and place the CSV there

5. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```

The app will open in your browser at `http://localhost:8501`

---

## Deployment to Streamlit Cloud

### Step 1: Prepare Your GitHub Repository

1. Create a new GitHub repository named `semmelweis-dashboard` (or your preferred name)

2. Initialize git locally and push your code:
   ```bash
   git init
   git add app.py requirements.txt README.md yearly_deaths_by_clinic-1.csv
   git commit -m "Initial commit: Semmelweis dashboard"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/semmelweis-dashboard.git
   git push -u origin main
   ```

### Step 2: Deploy to Streamlit Cloud

1. Go to [Streamlit Cloud](https://streamlit.io/cloud)
2. Click **"New app"**
3. Connect your GitHub account (if not already connected)
4. Select:
   - **Repository**: `YOUR_USERNAME/semmelweis-dashboard`
   - **Branch**: `main`
   - **Main file path**: `app.py`

5. Click **"Deploy!"**

Streamlit Cloud will automatically:
- Install dependencies from `requirements.txt`
- Run your app
- Provide you with a public URL (e.g., `https://YOUR_USERNAME-semmelweis-dashboard.streamlit.app`)

### Step 3: Submit Your URL

Copy your Streamlit Cloud URL and submit it in Canvas.

---

## Project Structure

```
semmelweis-dashboard/
├── app.py                              # Main Streamlit application
├── requirements.txt                    # Python dependencies
├── README.md                           # This file
├── yearly_deaths_by_clinic-1.csv       # Historical data
└── .gitignore                          # (Optional) Git ignore file
```

### .gitignore (Optional)
```
venv/
.streamlit/secrets.toml
*.pyc
__pycache__/
.DS_Store
```

---

## Data Source

**Dataset**: Yearly Deaths by Clinic (1841-1849)
- **Clinic 1**: Teaching hospital, physicians delivered babies
- **Clinic 2**: Midwife clinic
- **Key Event**: Hand-washing introduced in Clinic 1 in 1847

**Historical Context**: Vienna General Hospital obstetrical wards

---

## Code Attribution

This project includes code snippets assisted by Claude (Anthropic's AI assistant):
- **Streamlit configuration & layout design**: AI-assisted for optimal UX
- **Data visualization functions**: AI-assisted for chart rendering
- **Filtering logic**: AI-assisted for interactive controls
- **Historical context section**: Written by Claude with fact-checking

For transparency, all AI-assisted sections are noted in the code comments.

---

## Troubleshooting

### "FileNotFoundError: CSV not found"
- Ensure `yearly_deaths_by_clinic-1.csv` is in the project root or `data/` folder
- The app will use sample data as a fallback if the file is missing

### App doesn't run locally
1. Verify all dependencies are installed: `pip install -r requirements.txt`
2. Check Python version: `python --version` (should be 3.7+)
3. Try running with: `python -m streamlit run app.py`

### Deployment issues
- Check that `requirements.txt` is in the root of your GitHub repository
- Ensure `app.py` is in the root directory
- Verify the file is named exactly `app.py` (case-sensitive on Linux)

---

## Learning Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [Semmelweis Biography](https://en.wikipedia.org/wiki/Ignaz_Semmelweis)
- [Matplotlib Documentation](https://matplotlib.org)
- [Pandas Documentation](https://pandas.pydata.org)

---

## License

This project is provided as-is for educational purposes. The Semmelweis dataset is historical and in the public domain.

---

**Happy analyzing! 🏥📊**
