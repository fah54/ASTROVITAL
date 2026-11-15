
def assess_health(heart_rate, spo2, temperature,
                  sleep_hours, stress, fatigue):

    issues = []
    recommendations = []

    if spo2 < 95:
        issues.append("Low oxygen level")
        recommendations.append(
            "Review oxygen readings and follow mission medical protocols."
        )

    if heart_rate < 50 or heart_rate > 100:
        issues.append("Heart rate outside demo range")
        recommendations.append(
            "Review heart rate and monitor changes."
        )

    if temperature < 36 or temperature > 38:
        issues.append("Temperature outside demo range")
        recommendations.append(
            "Review body temperature readings."
        )

    if sleep_hours < 6:
        issues.append("Insufficient sleep")
        recommendations.append(
            "Review sleep schedule and recovery."
        )

    if stress >= 7:
        issues.append("High stress level")
        recommendations.append(
            "Consider stress-management support."
        )

    if fatigue >= 7:
        issues.append("High fatigue level")
        recommendations.append(
            "Review workload and recovery time."
        )

    critical_issues = [
        "Low oxygen level",
        "Heart rate outside demo range",
        "Temperature outside demo range"
    ]

    if any(issue in critical_issues for issue in issues):
        risk_level = "ATTENTION REQUIRED"

    elif issues:
        risk_level = "MONITOR HEALTH"

    else:
        risk_level = "WITHIN DEMO RULES"

    if not recommendations:
        recommendations.append(
            "Continue routine health monitoring."
        )

    return {
        "risk_level": risk_level,
        "issues": issues,
        "recommendations": recommendations
    }
