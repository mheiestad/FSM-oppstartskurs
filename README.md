# Feedback-driven drone FSM

The FSM asks for feedback before every transition:

`Disarmed --connected--> Arming --armed--> Takeoff --airborne--> Hover`

`Hover --ready to fly--> Flying --battery < 50%--> Landing`

`Landing --landed--> Landed --disarmed--> Disarmed`

Run the code with:

```bash
python3 main.py
```

# Your task

Fill out the code to complete the logic
