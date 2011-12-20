from Brain import Brain

brain = Brain()
brain.generateNeuronSet(100)
brain.generateNeuronLinks()

for i in range(10):
  if i % 2:
    brain.neurons[i].level = 0.5
  else:
    brain.neurons[i].level = -0.5
  brain.neurons[i].lock()

brain.neurons[89].level = 0.99
brain.neurons[89].lock()
brain.neurons[90].level = -0.99
brain.neurons[90].lock()

for i in range(100):
  brain.update()

brain.dumpState()

#brain.memorize()
brain.neurons[89].addInputToMemory()
brain.neurons[90].addInputToMemory()

brain.neurons[89].unlock()
brain.neurons[90].unlock()
for i in range(10,100,1):
  brain.neurons[i].level = 0.


#brain.neurons[0].level = 0.3
#brain.neurons[1].level = 0.4
#brain.neurons[2].level = 0.5
#brain.neurons[3].level = 0.
#brain.neurons[4].level = 0.3
#brain.neurons[5].level = 0.4
#brain.neurons[6].level = 0.5
#brain.neurons[7].level = -0.3
#brain.neurons[8].level = -0.4
#brain.neurons[9].level = -0.5

for i in range(10):
  if i % 2:
    brain.neurons[i].level = -0.1
  else:
    brain.neurons[i].level = -0.4

#for i in range(10):
#  brain.neurons[i].level = 0.

for i in range(100):
  brain.update()

brain.dumpState()