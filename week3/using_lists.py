states = ["Washington", "Montana", "California"]

'''
print(states[-1])
print(states[-2])
print(states[-3])
'''

states[2] = "Arizona"
# print(states)

states.append("New York")
print(states)

states.pop()
print(states)