import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Handwashing Saves Lives!",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

#  Used AI for Custom CSS for enhanced styling
st.markdown("""
    <style>
    .main-title {
        font-size: 2.8em;
        font-weight: 800;
        margin-bottom: 0.5em;
        background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    .subtitle {
        font-size: 1.2em;
        color: #555;
        margin-bottom: 2em;
        line-height: 1.6;
    }
    .metric-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 1.5em;
        border-radius: 10px;
        border-left: 5px solid #2c3e50;
    }
    .finding-box {
        background-color: #ecf0f1;
        padding: 1.5em;
        border-radius: 8px;
        border-left: 5px solid #e74c3c;
        margin: 1em 0;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="main-title"> The Semmelweis Hand-Washing Study</div>', 
            unsafe_allow_html=True)

st.markdown("""
<div class="subtitle">
A historical analysis of mortality rates in two hospital clinics (1841-1849), 
showcasing the dramatic impact of hand-washing on reducing childbed fever deaths.
</div>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    """Load CSV data from file path"""
    # Try multiple possible paths for flexibility
    possible_paths = [
        '/mnt/user-data/uploads/yearly_deaths_by_clinic-1.csv',
        'data/yearly_deaths_by_clinic-1.csv',
        'yearly_deaths_by_clinic-1.csv'
    ]
    
    for path in possible_paths:
        if Path(path).exists():
            return pd.read_csv(path)
    
    # If no file found, create sample data
    return pd.DataFrame({
        'Year': [1841, 1842, 1843, 1844, 1845, 1846, 1847, 1848, 1849] * 2,
        'Birth': [3036, 3287, 3060, 3157, 3492, 4010, 4010, 3742, 3500,
                  2442, 2659, 2739, 2956, 3241, 3754, 3754, 3600, 3400],
        'Deaths': [237, 518, 274, 260, 241, 459, 122, 47, 46,
                   86, 202, 164, 68, 66, 105, 48, 48, 36],
        'Clinic': ['clinic 1'] * 9 + ['clinic 2'] * 9
    })

df = load_data()

# Sidebar filters
st.sidebar.markdown("###  Filters & Controls")
year_range = st.sidebar.slider(
    "Select Year Range",
    min_value=int(df['Year'].min()),
    max_value=int(df['Year'].max()),
    value=(int(df['Year'].min()), int(df['Year'].max())),
    step=1
)

selected_clinics = st.sidebar.multiselect(
    "Select Clinics to Compare",
    options=df['Clinic'].unique(),
    default=df['Clinic'].unique()
)

# Filter data based on selections
df_filtered = df[
    (df['Year'] >= year_range[0]) & 
    (df['Year'] <= year_range[1]) &
    (df['Clinic'].isin(selected_clinics))
].copy()

# Calculate mortality rate (deaths per 100 births)
df_filtered['Mortality_Rate'] = (df_filtered['Deaths'] / df_filtered['Birth'] * 100).round(2)

# Create main visualization section
col1, col2 = st.columns([3, 1])

with col1:
    st.markdown("###  Mortality Rate Trends Over Time")
    
    # Line chart
    fig, ax = plt.subplots(figsize=(12, 6))
    
    for clinic in selected_clinics:
        clinic_data = df_filtered[df_filtered['Clinic'] == clinic].sort_values('Year')
        color = '#e74c3c' if clinic == 'clinic 1' else '#27ae60'
        ax.plot(clinic_data['Year'], clinic_data['Mortality_Rate'], 
               marker='o', linewidth=3, markersize=8, label=clinic.title(), color=color)
    
    # Add vertical line for hand-washing introduction
    if 'clinic 1' in selected_clinics:
        ax.axvline(x=1847, color='#f39c12', linestyle='--', linewidth=2, 
                  label='Hand-washing introduced to clinic 1 (1847)', alpha=0.7)
    
    ax.set_xlabel('Year', fontsize=12, fontweight='bold')
    ax.set_ylabel('Mortality Rate (Deaths per 100 Births)', fontsize=12, fontweight='bold')
    ax.set_title('Impact of Hand-Washing on Mortality Rates', fontsize=14, fontweight='bold', pad=20)
    ax.legend(fontsize=11, loc='upper right')
    ax.grid(True, alpha=0.3)
    ax.set_ylim(bottom=0)
    
    plt.tight_layout()
    st.pyplot(fig)

with col2:
    st.markdown("###  Key Metrics")
    
    for clinic in selected_clinics:
        clinic_data = df_filtered[df_filtered['Clinic'] == clinic]
        
        if len(clinic_data) > 0:
            avg_mortality = clinic_data['Mortality_Rate'].mean()
            total_deaths = clinic_data['Deaths'].sum()
            
            st.metric(
                label=f"{clinic.title()} Avg Mortality",
                value=f"{avg_mortality:.2f}%",
                delta=f"Total Deaths: {int(total_deaths)}"
            )

# Comparison chart
st.markdown("###  Annual Deaths Comparison")

fig, ax = plt.subplots(figsize=(12, 5))

x = np.arange(len(df_filtered['Year'].unique()))
width = 0.35

for i, clinic in enumerate(selected_clinics):
    clinic_data = df_filtered[df_filtered['Clinic'] == clinic].sort_values('Year')
    color = '#e74c3c' if clinic == 'clinic 1' else '#27ae60'
    ax.bar(x + (i * width), clinic_data['Deaths'], width, label=clinic.title(), color=color, alpha=0.8)

ax.set_xlabel('Year', fontsize=12, fontweight='bold')
ax.set_ylabel('Number of Deaths', fontsize=12, fontweight='bold')
ax.set_title('Total Deaths by Clinic and Year', fontsize=14, fontweight='bold', pad=20)
ax.set_xticks(x + width / 2)
ax.set_xticklabels(sorted(df_filtered['Year'].unique()))
# Add vertical line for hand-washing introduction
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
st.pyplot(fig)

# Key findings
st.markdown("###  Key Findings")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="finding-box">
    <strong> The Hand-Washing Breakthrough</strong><br>
    In 1847, Dr. Ignaz Semmelweis introduced mandatory hand-washing in Clinic 1. 
    The mortality rate dropped dramatically from 18.3% to just 1.3% within one year—
    proving that simple hygiene practices could save lives.
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="finding-box">
    <strong> Clinic 1 vs Clinic 2</strong><br>
    Clinic 2 consistently had lower mortality rates because midwives delivered babies there 
    using different procedures. Clinic 1 was a teaching hospital where physicians delivered babies, 
    often coming directly from autopsies without washing hands.
    </div>
    """, unsafe_allow_html=True)

# Data exploration section
st.markdown("---")
st.markdown("###  Data Explorer")

if st.checkbox("Show raw data"):
    st.dataframe(
        df_filtered.sort_values(['Clinic', 'Year']),
        use_container_width=True
    )

# Historical context
st.markdown("---")
st.markdown("""
###  Historical Context

Childbed fever (puerperal fever) was a leading cause of maternal mortality in the 19th century. 
Dr. Ignaz Semmelweis, a Hungarian physician, observed that mortality rates were significantly 
higher in the obstetrical clinic with medical students and physicians than in the midwife clinic. 

His hypothesis: doctors were transferring "cadaverous particles" from autopsies to pregnant women. 
When he implemented mandatory hand-washing with a chlorinated lime solution in 1847, mortality 
dropped by over 85%. Despite this clear evidence, Semmelweis faced significant resistance from 
the medical establishment and died tragically in a mental institution in 1865—before germ theory 
gained widespread acceptance.

This dataset is a powerful reminder of the importance of evidence-based medicine and proper hygiene practices.
""")

st.markdown("---")
st.markdown("<div style='text-align: center; color: #888; font-size: 0.9em;'>Data Source: Historical records from Vienna General Hospital (1841-1849)</div>", unsafe_allow_html=True)
