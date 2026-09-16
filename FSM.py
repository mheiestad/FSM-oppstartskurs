from States import States


class Feedback:
	"""feedback received before each decision"""

	def __init__(
		self,
		connected: bool = False,
		armed: bool = False,
		ready_to_fly: bool = False,
		airborne: bool = False,
		landed: bool = False,
		disarmed: bool = False,
		battery_percent: float = 100
	) -> None:
		self.connected = connected
		self.armed = armed
		self.ready_to_fly = ready_to_fly
		self.airborne = airborne
		self.landed = landed
		self.disarmed = disarmed
		self.battery_percent = battery_percent

class FSM:
	"""class for fsm driven by feedback"""

	TRANSITIONS = {
		States.DISARMED: States.ARMING,
		States.ARMING: States.TAKEOFF,
		States.TAKEOFF: States.HOVER,
		States.HOVER: States.FLYING,
		States.FLYING: States.LANDING,
		States.LANDING: States.LANDED,
		States.LANDED: States.DISARMED,
	}

	def __init__(self) -> None:
		self.state = States.DISARMED

	def transition_to(self, next_state: States) -> None:
		"""Move to an allowed state, or explain why the move is unsafe."""
		self.state = next_state


	def decide_next_state(self, feedback: Feedback) -> States:
		"""Choose the next state from current state and drone feedback."""
		next_state = self.TRANSITIONS[self.state]

		if not 0 <= feedback.battery_percent <= 100:
			raise ValueError("Battery must be between 0 and 100 percent")
    
		if self.state == States.DISARMED:
			if (feedback.connected):
				return next_state
			
		if self.state == States.ARMING:
			if (feedback.armed):
				return next_state
			
		if self.state == States.TAKEOFF:
			if (feedback.airborne):
				return next_state
			
		if self.state == States.HOVER:
			if (feedback.ready_to_fly):
				return next_state
			
		if self.state == States.FLYING:
			if (feedback.battery_percent<40):
				return next_state
			
		if self.state == States.LANDING:
			if (feedback.landed):
				return next_state
			
		if self.state == States.LANDED:
			if (feedback.disarmed):
				return next_state
			
		return self.state


	def step(self, feedback: Feedback) -> States:
		"""ask for feedback and apply"""
		next_state = self.decide_next_state(feedback)
		if next_state != self.state:
			self.transition_to(next_state)
		return self.state