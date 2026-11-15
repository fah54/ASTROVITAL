# ASTROVITAL

Astronaut Health Intelligence and Early Warning System — beginner-friendly demo prototype.

## Run on Windows
1. Install Python.
2. Extract this ZIP.
3. Open the extracted folder in VS Code.
4. Open Terminal > New Terminal.
5. Run:
   ```bash
   python -m pip install -r requirements.txt
   python -m streamlit run app.py
   ```

## Important limitations
- This is a prototype, not a medical device or diagnostic tool.
- Thresholds in `health_engine.py` are illustrative demo rules, not clinical guidance or NASA operational limits.
- No live wearable or spacecraft sensor connection is implemented.
- The trend chart uses synthetic example data and must be labelled as such.
- Do not describe demo data as real astronaut measurements.
- Verify NASA dataset study populations, variables, units, permissions, and limitations before using them.
