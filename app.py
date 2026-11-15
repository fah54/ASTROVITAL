import streamlit as st
import pandas as pd
import plotly.express as px
from health_engine import assess_health

st.set_page_config(page_title="ASTROVITAL", page_icon="🛰️", layout="wide")
st.title("🛰️ ASTROVITAL")
st.caption("Astronaut Health Intelligence and Early Warning System")
st.info("Prototype only. Not a medical device, diagnosis, or clinically validated monitoring system.")

with st.sidebar:
    st.header("Mission profile")
    astronaut_id = st.text_input("Astronaut ID", "ASTRO-001")
    mission = st.text_input("Mission", "Demo mission")
    st.caption("Demo inputs are manually entered; no live wearable connection is implemented.")

st.subheader("Health indicators")
c1, c2, c3 = st.columns(3)
heart_rate = c1.number_input("Heart rate (bpm)", 30, 200, 72)
spo2 = c2.number_input("SpO₂ (%)", 70, 100, 98)
temperature = c3.number_input("Body temperature (°C)", 34.0, 42.0, 36.8, step=0.1)
c4, c5, c6 = st.columns(3)
sleep = c4.number_input("Sleep (hours)", 0.0, 24.0, 7.5, step=0.5)
stress = c5.slider("Stress (demo scale)", 1, 10, 3)
fatigue = c6.slider("Fatigue (demo scale)", 1, 10, 3)

if st.button("Analyse health", type="primary"):
    result = assess_health(heart_rate, spo2, temperature, sleep, stress, fatigue)
    st.subheader(f"Assessment: {result['status']}")
    st.write(f"**Astronaut:** {astronaut_id}  |  **Mission:** {mission}")
    st.metric("Indicators flagged", len(result["alerts"]))
    if result["alerts"]:
        for alert in result["alerts"]:
            st.warning(alert)
    else:
        st.success("No indicators were flagged by the illustrative demo rules.")
    st.subheader("Suggested actions")
    for item in result["recommendations"]:
        st.write("• " + item)

st.divider()
st.subheader("Example 7-day trend (synthetic demo data)")
df = pd.DataFrame({
    "Day": ["D-6", "D-5", "D-4", "D-3", "D-2", "D-1", "Today"],
    "Heart rate (bpm)": [70, 72, 74, 71, 73, 75, 72],
    "SpO₂ (%)": [98, 98, 97, 98, 97, 98, 98],
})
metric = st.selectbox("Choose trend", ["Heart rate (bpm)", "SpO₂ (%)"])
fig = px.line(df, x="Day", y=metric, markers=True, title=metric)
st.plotly_chart(fig, use_container_width=True)
st.caption("All chart values above are synthetic examples, not real astronaut measurements.")

st.subheader("NASA research links")
st.markdown("- [NASA Open Science Data Repository](https://osdr.nasa.gov/)")
st.markdown("- [NASA Human Research Program](https://www.nasa.gov/hrp/)")
st.caption("Use actual NASA datasets only after verifying their study population, units, and limitations.")
