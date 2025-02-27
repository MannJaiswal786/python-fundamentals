state_capitals = {"Washington": "Olympia", "Arizona": "Phoenix", "California": "Sacramento"}
#print(len(state_capitals))
print(state_capitals["Arizona"])
state_capitals["Arizona"] = "Tucson"
state_capitals["Texas"] = "Houston"
del state_capitals["Washington"]
removed_capital = state_capitals.pop("Arizona")
print(state_capitals)