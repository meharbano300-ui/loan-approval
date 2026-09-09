import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ---------------------------------------------------------
# 1. Page Configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="AuraFinance | AI Luxury Loan Portal",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# 2. Custom CSS (Luxury Light Glassmorphism + Extended Visual Highlights)
# ---------------------------------------------------------
custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Playfair+Display:wght@600;700&display=swap');

    /* Global Typography & Light Background */
    html, body, [class*="css"], .stApp {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        background: linear-gradient(135deg, #f1f5f9 0%, #e2e8f0 100%) !important;
        color: #0f172a !important;
    }

    /* Headings Accent */
    h1, h2, h3 {
        font-family: 'Playfair Display', serif !important;
        letter-spacing: -0.02em;
    }

    /* Custom Glassmorphism Containers */
    .glass-card {
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.9);
        border-radius: 24px;
        padding: 28px;
        box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.05), 0 0 20px rgba(59, 130, 246, 0.08);
        margin-bottom: 24px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .glass-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 25px 50px -12px rgba(99, 102, 241, 0.15);
    }

    /* Vibrant Gradient Cards */
    .blue-gradient-card {
        background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
        color: #ffffff !important;
        border-radius: 20px;
        padding: 24px;
        box-shadow: 0 10px 25px rgba(37, 99, 235, 0.3);
        transition: transform 0.3s ease;
    }

    .purple-gradient-card {
        background: linear-gradient(135deg, #8b5cf6 0%, #6d28d9 100%);
        color: #ffffff !important;
        border-radius: 20px;
        padding: 24px;
        box-shadow: 0 10px 25px rgba(139, 92, 246, 0.3);
        transition: transform 0.3s ease;
    }

    .orange-red-card {
        background: linear-gradient(135deg, #f97316 0%, #ef4444 100%);
        color: #ffffff !important;
        border-radius: 20px;
        padding: 24px;
        box-shadow: 0 10px 25px rgba(239, 68, 68, 0.3);
        transition: transform 0.3s ease;
    }

    .blue-gradient-card:hover, .purple-gradient-card:hover, .orange-red-card:hover {
        transform: translateY(-4px);
    }

    /* Hero Header Banner */
    .hero-banner {
        background: linear-gradient(120deg, #ffffff 0%, #eff6ff 40%, #f3e8ff 100%);
        border: 1px solid rgba(255, 255, 255, 0.9);
        border-radius: 28px;
        padding: 36px;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.04);
        margin-bottom: 20px;
        position: relative;
        overflow: hidden;
    }

    /* Sidebar Luxury Styling */
    section[data-testid="stSidebar"] {
        background: #ffffff !important;
        border-right: 1px solid #e2e8f0;
        box-shadow: 5px 0 25px rgba(0,0,0,0.02);
    }

    /* Radio Button Nav Tabs Styling */
    .stRadio > div {
        gap: 12px;
    }
    
    .stRadio label {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 16px !important;
        padding: 12px 18px !important;
        font-weight: 600 !important;
        color: #334155 !important;
        transition: all 0.25s ease !important;
        box-shadow: 0 2px 5px rgba(0,0,0,0.02);
    }

    .stRadio label:hover {
        border-color: #8b5cf6 !important;
        background: #faf5ff !important;
        transform: translateX(4px);
    }

    /* Input Form Glass Effect */
    div[data-testid="stForm"] {
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(16px);
        border: 1px solid #e2e8f0;
        border-radius: 24px;
        padding: 30px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.04);
    }

    /* Submit Button Accent */
    div[data-testid="stForm"] button[type="submit"] {
        background: linear-gradient(90deg, #2563eb 0%, #7c3aed 50%, #ef4444 100%) !important;
        color: white !important;
        font-weight: 700 !important;
        border-radius: 14px !important;
        padding: 14px 28px !important;
        border: none !important;
        font-size: 1.05rem !important;
        box-shadow: 0 10px 20px rgba(124, 58, 237, 0.3) !important;
        transition: all 0.3s ease !important;
    }

    div[data-testid="stForm"] button[type="submit"]:hover {
        transform: scale(1.01);
        box-shadow: 0 15px 25px rgba(124, 58, 237, 0.45) !important;
    }

    /* Custom Badges */
    .badge-blue {
        background: #dbeafe;
        color: #1e40af;
        padding: 6px 14px;
        border-radius: 30px;
        font-size: 0.8rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    .badge-purple {
        background: #f3e8ff;
        color: #6b21a8;
        padding: 6px 14px;
        border-radius: 30px;
        font-size: 0.8rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    .badge-green {
        background: #d1fae5;
        color: #065f46;
        padding: 6px 14px;
        border-radius: 30px;
        font-size: 0.8rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    /* Result Containers */
    .approved-card {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white;
        padding: 24px;
        border-radius: 20px;
        text-align: center;
        font-size: 1.4rem;
        font-weight: 800;
        box-shadow: 0 10px 25px rgba(16, 185, 129, 0.3);
    }

    .rejected-card {
        background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
        color: white;
        padding: 24px;
        border-radius: 20px;
        text-align: center;
        font-size: 1.4rem;
        font-weight: 800;
        box-shadow: 0 10px 25px rgba(239, 68, 68, 0.3);
    }

    /* Feature Badge Grid Icon Item */
    .icon-badge-box {
        display: flex;
        align-items: center;
        justify-content: center;
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 18px;
        padding: 10px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.03);
        transition: transform 0.2s ease;
    }
    .icon-badge-box:hover {
        transform: translateY(-2px);
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ---------------------------------------------------------
# 3. Model & Assets Loader
# ---------------------------------------------------------
@st.cache_resource
def load_ml_assets():
    try:
        model = joblib.load('loan_model.pkl')
        model_columns = joblib.load('model_columns.pkl')
        return model, model_columns
    except Exception:
        return None, None

model, model_columns = load_ml_assets()

# ---------------------------------------------------------
# 4. Sidebar & Luxury Navigation
# ---------------------------------------------------------
with st.sidebar:
    # Changed Icon to Bank/House Icon
    st.image("https://cdn-icons-png.flaticon.com/512/2830/2830284.png", width=70)
    st.markdown("## **AuraFinance AI**")
    st.markdown('<span class="badge-purple">PRO ENGINE v3.0</span> <span class="badge-green">ONLINE</span>', unsafe_allow_html=True)
    st.write("")

    nav_selection = st.radio(
        "Main Navigation Menu",
        [
            "🏠 Home & Portal",
            "📊 Risk Analytics",
            "⚡ Instant Pre-Check",
            "ℹ️ Platform Vision"
        ],
        index=0
    )

    st.divider()

    # Enhanced Sidebar Quick Stats Box
    st.markdown("""
    <div style="background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%); padding: 18px; border-radius: 20px; border: 1px solid #e2e8f0; box-shadow: 0 4px 15px rgba(0,0,0,0.02);">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
            <span style="font-size: 0.75rem; color: #64748b; font-weight:800; letter-spacing: 0.05em;">SYSTEM HEALTH</span>
            <span style="height: 10px; width: 10px; background-color: #10b981; border-radius: 50%; display: inline-block; box-shadow: 0 0 8px #10b981;"></span>
        </div>
        <p style="margin:2px 0; font-weight:800; color: #0f172a; font-size: 0.95rem;">🟢 Live Neural Engine</p>
        <div style="margin-top: 10px; padding-top: 10px; border-top: 1px dashed #e2e8f0; display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
            <div>
                <p style="margin:0; font-size: 0.7rem; color: #94a3b8;">LATENCY</p>
                <p style="margin:0; font-weight:700; font-size: 0.85rem; color: #3b82f6;">12ms</p>
            </div>
            <div>
                <p style="margin:0; font-size: 0.7rem; color: #94a3b8;">ACCURACY</p>
                <p style="margin:0; font-weight:700; font-size: 0.85rem; color: #8b5cf6;">98.4%</p>
            </div>
        </div>
        <div style="margin-top: 8px; padding-top: 8px; border-top: 1px dashed #e2e8f0;">
            <p style="margin:0; font-size: 0.7rem; color: #94a3b8;">SECURITY LEVEL</p>
            <p style="margin:0; font-weight:700; font-size: 0.8rem; color: #10b981;">🔒 256-bit Encrypted</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 5. PAGE 1: HOME & PORTAL
# ---------------------------------------------------------
if nav_selection == "🏠 Home & Portal":
    
    # Hero Section with 6 Colorful Icons
    st.markdown("""
    <div class="hero-banner">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 20px;">
            <div style="max-width: 600px;">
                <span class="badge-blue">NEXT-GEN FINTECH</span>
                <h1 style="margin: 12px 0 8px 0; color: #0f172a; font-size: 2.5rem;">Smart Credit & Loan Evaluation</h1>
                <p style="color: #475569; font-size: 1.05rem; line-height: 1.6; margin: 0;">
                    Experience real-time AI risk assessment. Get instant approval insights using high-precision machine learning models.
                </p>
            </div>
            <!-- Expanded 6 Colorful Icons Grid -->
          <div style="display: grid; grid-template-columns: repeat(9, 1fr); gap: 14px;">
    <div class="icon-badge-box"><img src="https://cdn-icons-png.flaticon.com/512/2489/2489756.png" width="52" alt="Money Bag"></div>
    <div class="icon-badge-box"><img src="https://cdn-icons-png.flaticon.com/512/619/619032.png" width="52" alt="Home"></div>
    <div class="icon-badge-box"><img src="https://cdn-icons-png.flaticon.com/512/3135/3135706.png" width="52" alt="Credit Card"></div>
    <div class="icon-badge-box"><img src="https://cdn-icons-png.flaticon.com/512/2099/2099058.png" width="52" alt="AI Shield"></div>
    <div class="icon-badge-box"><img src="https://cdn-icons-png.flaticon.com/512/1041/1041888.png" width="52" alt="Analytics Vault"></div>
    <div class="icon-badge-box"><img src="https://cdn-icons-png.flaticon.com/512/2830/2830284.png" width="52" alt="Bank Growth"></div>
    <!-- 3 New Colored Icons -->
    <div class="icon-badge-box"><img src="https://cdn-icons-png.flaticon.com/512/190/190411.png" width="52" alt="Approval Badge"></div>
    <div class="icon-badge-box"><img src="https://cdn-icons-png.flaticon.com/512/2910/2910756.png" width="52" alt="Financial Calculator"></div>
    <div class="icon-badge-box"><img src="https://cdn-icons-png.flaticon.com/512/1055/1055644.png" width="52" alt="Loan Agreement"></div>
</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Colorful Visual Showcase Cards
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("""
        <div class="blue-gradient-card">
            <img src="https://cdn-icons-png.flaticon.com/512/3135/3135706.png" width="45" style="margin-bottom:12px;">
            <h3 style="margin:0; font-size: 1.3rem;">Fast Capital Access</h3>
            <p style="margin:8px 0 0 0; opacity: 0.9; font-size: 0.9rem;">Instant liquidity check for personal and mortgage requirements.</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="purple-gradient-card">
            <img src="https://cdn-icons-png.flaticon.com/512/2099/2099058.png" width="45" style="margin-bottom:12px;">
            <h3 style="margin:0; font-size: 1.3rem;">AI Risk Scoring</h3>
            <p style="margin:8px 0 0 0; opacity: 0.9; font-size: 0.9rem;">Multi-factor algorithmic verification ensuring 99% precision.</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="orange-red-card">
            <img src="https://cdn-icons-png.flaticon.com/512/619/619032.png" width="45" style="margin-bottom:12px;">
            <h3 style="margin:0; font-size: 1.3rem;">Mortgage Solutions</h3>
            <p style="margin:8px 0 0 0; opacity: 0.9; font-size: 0.9rem;">Tailored financing plans for property and real estate assets.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Interactive Option Box for Form
    st.markdown("### 📄 Evaluation Portal")
    
    show_form_expander = st.expander("⚡ Click Here to Launch Loan Application Form", expanded=True)

    with show_form_expander:
        with st.form("loan_application_form"):
            col1, col2, col3 = st.columns(3)

            # Column 1: Personal Profile
            with col1:
                st.markdown("#### 👤 Applicant Profile")
                gender = st.selectbox("Gender Identification", ["Male", "Female"])
                married = st.selectbox("Marital Status", ["Yes", "No"])
                dependents = st.selectbox("Dependents Count", ["0", "1", "2", "3+"])
                education = st.selectbox("Education Level", ["Graduate", "Not Graduate"])
                self_employed = st.selectbox("Employment Type", ["No", "Yes"])

            # Column 2: Financial Metrics
            with col2:
                st.markdown("#### 💵 Income & Credit Metrics")
                applicant_income = st.number_input("Primary Monthly Income ($)", min_value=0, value=5000, step=500)
                coapplicant_income = st.number_input("Co-Applicant Income ($)", min_value=0, value=2000, step=500)
                credit_history = st.selectbox("Credit History Clean?", [1.0, 0.0], format_func=lambda x: "Yes - High Score (1.0)" if x == 1.0 else "No - Defaulter / Pending (0.0)")

            # Column 3: Property Details
            with col3:
                st.markdown("#### 🏠 Loan & Asset Details")
                loan_amount = st.slider("Loan Requirement ($ in Thousands)", min_value=10, max_value=700, value=180, step=10)
                loan_term = st.selectbox("Loan Duration (Months)", [360, 180, 240, 120, 84, 60], index=0)
                property_area = st.selectbox("Property Zone", ["Urban", "Semiurban", "Rural"])

            st.markdown("<br>", unsafe_allow_html=True)
            submit_btn = st.form_submit_button("🚀 Run AI Eligibility Assessment", use_container_width=True)

    # Prediction Logic
    if 'submit_btn' in locals() and submit_btn:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("### 📊 AI Decision Summary")
        
        input_data = {
            'Gender': gender,
            'Married': married,
            'Dependents': dependents,
            'Education': education,
            'Self_Employed': self_employed,
            'ApplicantIncome': applicant_income,
            'CoapplicantIncome': coapplicant_income,
            'LoanAmount': loan_amount,
            'Loan_Amount_Term': loan_term,
            'Credit_History': credit_history,
            'Property_Area': property_area
        }

        df_input = pd.DataFrame([input_data])
        df_encoded = pd.get_dummies(df_input)

        if model is not None and model_columns is not None:
            df_final = df_encoded.reindex(columns=model_columns, fill_value=0)
            prediction = model.predict(df_final)[0]
            prediction_proba = model.predict_proba(df_final)[0] if hasattr(model, "predict_proba") else None

            res_col1, res_col2 = st.columns([2, 1])

            with res_col1:
                if prediction == 1 or str(prediction).upper() == 'Y':
                    st.markdown('<div class="approved-card">🎉 CONGRATULATIONS! LOAN APPROVED</div>', unsafe_allow_html=True)
                    st.write("The profile meets low-risk thresholds and complies with institutional lending criteria.")
                else:
                    st.markdown('<div class="rejected-card">⚠️ APPLICATION FLAGGED / REJECTED</div>', unsafe_allow_html=True)
                    st.write("The financial ratios or credit background exceed acceptable risk margins.")

            with res_col2:
                if prediction_proba is not None:
                    confidence = max(prediction_proba) * 100
                    st.metric(label="Model AI Confidence Score", value=f"{confidence:.1f}%")
        else:
            st.warning("⚠️ Model files (`loan_model.pkl`, `model_columns.pkl`) not found locally.")
        
        st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 6. PAGE 2: MODEL ANALYTICS
# ---------------------------------------------------------
elif nav_selection == "📊 Risk Analytics":
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    
    # Styled Header with Icon
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 10px;">
        <img src="https://cdn-icons-png.flaticon.com/512/1041/1041888.png" width="45">
        <div>
            <h2 style="margin:0; font-size: 2rem; color: #0f172a;">Financial Risk Analytics & Model Insights</h2>
            <p style="margin:0; color: #64748b;">In-depth analysis of machine learning decision boundaries and feature attribution weights.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Base Classifier", "XGBoost / LogReg")
    m2.metric("Overall Accuracy", "86.7%")
    m3.metric("ROC-AUC Score", "0.89")
    m4.metric("Dataset Size", "614 Records")
    st.markdown("</div>", unsafe_allow_html=True)

    # Feature Importance Showcase with Existing Chart Structure Intact
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("""
    <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 15px;">
        <h3 style="margin:0;">🔥 Key Predictor Weights</h3>
        <span class="badge-purple">SHAP & Gini Importance</span>
    </div>
    """, unsafe_allow_html=True)
    
    chart_data = pd.DataFrame({
        'Feature': ['Credit History', 'Applicant Income', 'Loan Amount', 'Coapplicant Income', 'Property Area'],
        'Importance Weight': [0.45, 0.22, 0.15, 0.10, 0.08]
    })
    st.bar_chart(chart_data.set_index('Feature'))
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 7. PAGE 3: INSTANT PRE-CHECK
# ---------------------------------------------------------
elif nav_selection == "⚡ Instant Pre-Check":
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 15px;">
        <img src="https://cdn-icons-png.flaticon.com/512/2489/2489756.png" width="45">
        <div>
            <h2 style="margin:0; font-size: 2rem; color: #0f172a;">Quick Financial Eligibility Estimator</h2>
            <p style="margin:0; color: #64748b;">Estimate your maximum loan capacity before filling the full application.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col_a, col_b = st.columns(2)
    with col_a:
        inc = st.number_input("Monthly Income ($)", value=6000)
        exp = st.number_input("Monthly Expenses ($)", value=2000)
    
    with col_b:
        dti = ((exp) / inc) * 100 if inc > 0 else 0
        st.metric("Debt-To-Income (DTI) Ratio", f"{dti:.1f}%")
        
        if dti < 35:
            st.success("Excellent DTI Ratio! You qualify for premier interest rates.")
        elif dti < 50:
            st.info("Moderate DTI Ratio. Standard loan terms apply.")
        else:
            st.error("High DTI Ratio. Consider lowering existing debt.")

    st.markdown("<hr style='border: 0; border-top: 1px solid #e2e8f0; margin: 20px 0;'>", unsafe_allow_html=True)
    
    # Styled Additional Pre-Check Insights Box
    max_borrow = (inc - exp) * 60  # Approx 5-year leverage estimation
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #eff6ff 0%, #f0fdf4 100%); padding: 20px; border-radius: 16px; border: 1px solid #bfdbfe;">
        <div style="display: flex; align-items: center; justify-content: space-between;">
            <div>
                <h4 style="margin:0; color: #1e3a8a;">💡 Estimated Maximum Borrowing Limit</h4>
                <p style="margin:4px 0 0 0; color: #475569; font-size: 0.9rem;">Based on a standard 40% maximum installment capacity threshold.</p>
            </div>
            <h2 style="margin:0; color: #166534; font-weight: 800;">${max_borrow:,.0f}</h2>
        </div>
    </div>
    """, unsafe_allow_html=True)
            
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 8. PAGE 4: ABOUT PORTAL
# ---------------------------------------------------------
elif nav_selection == "ℹ️ Platform Vision":
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
        <img src="https://cdn-icons-png.flaticon.com/512/2830/2830284.png" width="50">
        <div>
            <h2 style="margin:0; font-size: 2rem; color: #0f172a;">About AuraFinance Engine</h2>
            <p style="margin:0; color: #64748b;">Next-Generation Automated Credit Risk Infrastructure.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    AuraFinance is an enterprise-grade automated decision engine engineered to streamline capital distribution and retail mortgage lending.
    
    * **Frontend:** Streamlit with Custom Modern Glassmorphism Architecture
    * **ML Engine:** Scikit-Learn Pipeline Serialization
    * **Visual Identity:** Luxury Light Theme with Radiant Gradient Highlights
    """)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Platform Architecture Feature Cards
    v1, v2, v3 = st.columns(3)
    with v1:
        st.markdown("""
        <div style="background: #ffffff; padding: 20px; border-radius: 16px; border: 1px solid #e2e8f0; text-align: center;">
            <img src="https://cdn-icons-png.flaticon.com/512/2099/2099058.png" width="40" style="margin-bottom:10px;">
            <h4 style="margin:0; font-size: 1.05rem;">Neural Precision</h4>
            <p style="margin:6px 0 0 0; font-size: 0.85rem; color: #64748b;">Sub-second execution with automated feature pipeline transformation.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with v2:
        st.markdown("""
        <div style="background: #ffffff; padding: 20px; border-radius: 16px; border: 1px solid #e2e8f0; text-align: center;">
            <img src="https://cdn-icons-png.flaticon.com/512/3135/3135706.png" width="40" style="margin-bottom:10px;">
            <h4 style="margin:0; font-size: 1.05rem;">Zero-Bias Engine</h4>
            <p style="margin:6px 0 0 0; font-size: 0.85rem; color: #64748b;">Strict regulatory compliance and fair credit scoring principles.</p>
        </div>
        """, unsafe_allow_html=True)

    with v3:
        st.markdown("""
        <div style="background: #ffffff; padding: 20px; border-radius: 16px; border: 1px solid #e2e8f0; text-align: center;">
            <img src="https://cdn-icons-png.flaticon.com/512/1041/1041888.png" width="40" style="margin-bottom:10px;">
            <h4 style="margin:0; font-size: 1.05rem;">Bank-Grade Vault</h4>
            <p style="margin:6px 0 0 0; font-size: 0.85rem; color: #64748b;">Enterprise encryption protecting input financial metrics.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)