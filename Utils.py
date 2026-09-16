from States import States

def state_to_string(state: States) -> str:
	return state.name.replace("_", " ").title()
