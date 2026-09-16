from FSM import FSM, Feedback
from States import States
from Utils import state_to_string


def ask_yes_no(question: str) -> bool:
	while True:
		answer = input(f"{question} [y/n] ").strip().lower()
		if answer in {"y", "yes"}:
			return True
		if answer in {"n", "no"}:
			return False
		print("Please answer y or n.")


def main():
	drone = FSM()
	print("Feedback-driven drone mission")
	while True:
		if drone.state == States.DISARMED:
			feedback = Feedback(connected=ask_yes_no("Is the drone connected?"))
		elif drone.state == States.ARMING:
			feedback = Feedback(armed=ask_yes_no("Is the drone armed?"))
		elif drone.state == States.TAKEOFF:
			feedback = Feedback(airborne=ask_yes_no("Has the drone taken off?"))
		elif drone.state == States.HOVER:
			feedback = Feedback(ready_to_fly=ask_yes_no("Is the drone ready to fly?"))
		elif drone.state == States.FLYING:
			battery = float(input("Battery percentage: "))
			feedback = Feedback(battery_percent=battery)
		elif drone.state == States.LANDING:
			feedback = Feedback(landed=ask_yes_no("Has the drone landed?"))
		else:
			feedback = Feedback(disarmed=ask_yes_no("Is the drone disarmed?"))

		old_state = drone.state
		state = drone.step(feedback)
		print(f"{state_to_string(old_state)} -> {state_to_string(state)}")
		if state == old_state:
			print("No transition yet; waiting for suitable feedback.")
		if old_state == States.LANDED and state == States.DISARMED:
			break


if __name__ == "__main__":
	main()
