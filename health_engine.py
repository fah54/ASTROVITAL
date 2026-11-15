def assess_health(heart_rate, spo2, temperature, sleep_hours, stress, fatigue):
    """Illustrative, explainable demo rules; not clinical or NASA operational thresholds."""
    alerts = []
    recommendations = []

    if spo2 < 95:
        alerts.append(f"SpO₂ is {spo2}% (below the illustrative demo threshold of 95%).")
        recommendations.append("Review the reading and follow the mission's approved medical protocol.")
    if heart_rate < 50 or heart_rate > 100:
        alerts.append(f"Heart rate is {heart_rate} bpm (outside the illustrative demo range of 50–100 bpm).")
        recommendations.append("Recheck the measurement and review it with qualified medical support.")
    if temperature < 36 or temperature > 38:
        alerts.append(f"Temperature is {temperature}°C (outside the illustrative demo range of 36–38°C).")
        recommendations.append("Confirm the temperature reading and follow the approved medical protocol.")
    if sleep_hours < 6:
        alerts.append(f"Sleep duration is {sleep_hours} hours (low in this demo).")
        recommendations.append("Review sleep opportunity, workload, and fatigue-management procedures.")
    if stress >= 7:
        alerts.append(f"Stress score is {stress}/10 (high on the demo scale).")
        recommendations.append("Consider a wellbeing check-in and approved stress-management support.")
    if fatigue >= 7:
        alerts.append(f"Fatigue score is {fatigue}/10 (high on the demo scale).")
        recommendations.append("Review workload and schedule an appropriate rest opportunity.")

    vital_alert = any("SpO₂" in a or "Heart rate" in a or "Temperature" in a for a in alerts)
    status = "Attention" if vital_alert else ("Monitor" if alerts else "Within demo rules")
    if not recommendations:
        recommendations.append("Continue routine monitoring under the mission's approved procedures.")
    return {"status": status, "alerts": alerts, "recommendations": recommendations}
