import streamlit as st
import pandas as pd

# 1. System Page Configuration & Global Theme Styling
st.set_page_config(
    page_title="Spacez Review Intelligence Control", 
    layout="wide", 
    page_icon="🏨"
)

# Custom CSS injector to give it a premium enterprise app look (Clean cards, sharp metrics)
st.markdown("""
<style>
    .metric-card {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 8px;
        border-left: 5px solid #6c757d;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        margin-bottom: 15px;
    }
    .metric-card-alert {
        background-color: #fff5f5;
        padding: 20px;
        border-radius: 8px;
        border-left: 5px solid #e03131;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        margin-bottom: 15px;
    }
    .badge-red {
        background-color: #ffe3e3;
        color: #c92a2a;
        padding: 4px 8px;
        border-radius: 4px;
        font-weight: bold;
        font-size: 12px;
    }
    .badge-orange {
        background-color: #fff0f6;
        color: #d6336c;
        padding: 4px 8px;
        border-radius: 4px;
        font-weight: bold;
        font-size: 12px;
    }
    .badge-blue {
        background-color: #e7f5ff;
        color: #1c7ed6;
        padding: 4px 8px;
        border-radius: 4px;
        font-weight: bold;
        font-size: 12px;
    }
</style>
""", unsafe_allow_html=True)

# 2. Main Executive Header Block
st.markdown("# 🏨 Spacez AI Review Intelligence Engine")
st.markdown("### `Operations Control Center | Regional Performance Workspace`")
st.markdown("---")

# 3. High-Fidelity KPI Executive Metrics Panel
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="metric-card">
        <p style="color: #666; font-size: 14px; margin-bottom: 5px; font-weight: 600;">PORTFOLIO OPERATIONAL INDEX</p>
        <h2 style="color: #212529; margin: 0; font-size: 36px;">2.39 <span style="font-size: 18px; color: #868e96;">/ 5.0 Baseline</span></h2>
        <p style="color: #fa5252; font-size: 13px; margin-top: 5px; font-weight: 500;">📉 Critical Target Zone Threshold</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card-alert">
        <p style="color: #c92a2a; font-size: 14px; margin-bottom: 5px; font-weight: 700;">🚨 SYSTEMIC OPERATIONAL THREAT</p>
        <h2 style="color: #c92a2a; margin: 0; font-size: 26px;">Cross-Property SLA Delays</h2>
        <p style="color: #fa5252; font-size: 13px; margin-top: 8px; font-weight: 500;"><b>Impact Delta:</b> -1.42 Score Drag on Portfolio</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <p style="color: #666; font-size: 14px; margin-bottom: 5px; font-weight: 600;">INGESTION STREAM STATUS</p>
        <h2 style="color: #2b8a3e; margin: 0; font-size: 36px;">Active Connected</h2>
        <p style="color: #868e96; font-size: 13px; margin-top: 5px; font-weight: 500;">Channels: Airbnb, Booking.com, Google Reviews</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 4. Core Analytical Split Panel (Root Cause Discovered)
st.markdown("## 🕵️‍♂️ AI Entity Linker & Cross-Reference Explorer")
st.markdown("*The system runs automated cross-reference checks mapping unstructured guest complaints to underlying operational dimensions (Staff vs Asset Hardware).*")

panel_col1, panel_col2 = st.columns(2)

with panel_col1:
    st.subheader("⚠️ Behavioral Entity Analysis: Staff & Caretakers")
    st.markdown("""
    The system extracted recurring operational bottlenecks that follow specific personnel schedules across independent properties.
    """)
    
    # Structured Table for Staff Analysis
    staff_data = {
        "Entity": ["Lokesh Gowda", "Lokesh Gowda"],
        "Assigned Property": ["Misty Estate", "Coorg Canopy"],
        "Extracted Friction Issue": ["Check-in process delayed by 90 minutes. Guests left waiting in rain.", "Check-in process delayed by over 1 hour. Caretaker completely unreachable."],
        "Root Cause Severity": ["High Severity SLA Breach", "High Severity SLA Breach"]
    }
    df_staff = pd.DataFrame(staff_data)
    st.table(df_staff)
    
    st.info("💡 **AI Operations Recommendation:** The operational breakdown follows the caretaker's calendar, not the properties. This is a route-optimization or scheduling deficit. Do not issue a property management layout penalty.")

with panel_col2:
    st.subheader("🛠️ Structural Entity Analysis: Property Assets")
    st.markdown("""
    The system isolated negative sentiment driven by physical infrastructure faults. Local caretakers are cleared of operational failure protocols.
    """)
    
    # Structured Table for Asset Analysis
    asset_data = {
        "Property Asset": ["Serenity Villa", "Cliffside Retreat"],
        "Platform History": ["Multi-Channel (Airbnb, Booking, Google)", "Airbnb & Google Streams"],
        "Identified Infrastructure Deficit": ["Continuous complaints regarding unmaintained, murky swimming pool water.", "Broken room heating systems during peak sub-zero winter stays."],
        "Capital Allocation Status": ["Dispatched to Vendor Queue", "Routed to Urgently Needed CapEx Queue"]
    }
    df_asset = pd.DataFrame(asset_data)
    st.table(df_asset)
    
    st.error("🚨 **AI Operations Recommendation:** These issues require immediate local vendor dispatch or asset improvement budget allocation. Local host metrics have been shielded from penalty metrics.")

st.markdown("---")

# 5. Automated Triage and Ticket Queue
st.markdown("## 📬 Live Automated Workflow & Ticket Dispatch Queue")
st.markdown("*Real-time pipeline actions executed by the Review Agent based on semantic mapping parameters.*")

# Ticket 1
with st.expander("🚨 TICKET LOG: RV011 — Property: Misty Estate [Score: 3.0/5.0 Baseline Normalization]"):
    col_t1_a, col_t1_b = st.columns([3, 1])
    with col_t1_a:
        st.markdown("**Raw Ingested Guest Review Feedback:**")
        st.markdown("*\"Stunning estate views. But check-in was an absolute mess - the caretaker arrived 90 minutes late and we were left waiting outside in the rain.\"*")
    with col_t1_b:
        st.markdown("<span class="badge-orange">⏰ STAFF SLA BREACH</span>", unsafe_allow_html=True)
        st.markdown("<br>**Automated Routing:**<br>`Operations Routing: Caretaker Schedule Optimizer Profile`", unsafe_allow_html=True)

# Ticket 2
with st.expander("🚨 TICKET LOG: RV002 — Property: Serenity Villa [Score: 3.0/5.0 Baseline Normalization]"):
    col_t2_a, col_t2_b = st.columns([3, 1])
    with col_t2_a:
        st.markdown("**Raw Ingested Guest Review Feedback:**")
        st.markdown("*\"Lovely property but the swimming pool was completely unmaintained - murky green water the whole duration of our stay.\"*")
    with col_t2_b:
        st.markdown("<span class="badge-red">🛠️ ASSET MAINTENANCE</span>", unsafe_allow_html=True)
        st.markdown("<br>**Automated Routing:**<br>`Operations Routing: Third-Party Vendor Penalty Queue`", unsafe_allow_html=True)

# Ticket 3
with st.expander("🚨 TICKET LOG: RV020 — Property: Cliffside Retreat [Score: 2.0/5.0 Baseline Normalization]"):
    col_t3_a, col_t3_b = st.columns([3, 1])
    with col_t3_a:
        st.markdown("**Raw Ingested Guest Review Feedback:**")
        st.markdown("*\"The heating didn't work properly and Kasauli in December is freezing. Cold all night despite telling host.\"*")
    with col_t3_b:
        st.markdown("<span class="badge-red">🛠️ CAPEX INFRASTRUCTURE</span>", unsafe_allow_html=True)
        st.markdown("<br>**Automated Routing:**<br>`Operations Routing: Urgent Capital Asset Procurement Queue`", unsafe_allow_html=True)
