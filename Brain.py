""" Class Brain represents a set of Neurons on the Brain Antenna theory
"""

import random
from Neuron import Neuron

random.seed('Andrei')

class Brain:

  nNeuronOutputs = 10

  def __init__(self):

    self.neuronCounter = 0
    self.neurons = []

  def generateNeuronSet(self,nNeurons):

    for i in range(nNeurons):
      self.neuronCounter += 1
      self.neurons.append(Neuron(self.neuronCounter))

  def generateNeuronLinks(self,neurons=None):

    nDict = {}
    if not neurons:
      neurons = self.neurons
    for n in neurons:
      nDict[n.id] = n

    ids = [ n.id for n in neurons ]
    for n in neurons:
      random.shuffle(ids)
      for i in range(self.nNeuronOutputs):
        n.addOutNeuron(nDict[ids[i]])
        nDict[ids[i]].addInNeuron(n)

  def update(self):

    delta = 0.
    for n in self.neurons:
      oldlevel,newlevel = n.getBestMatchToMemory()
      if newlevel < 0.1:
        oldlevel,newlevel = n.getInputLevel()
      else:
        n.setLevel(newlevel)

      #print ">>>",n.id,oldlevel,newlevel,[x.level for x in n.inNeurons],n.memory

      delta += abs(newlevel-oldlevel)

    print "Total update delta", delta

  def memorize(self):

    for n in self.neurons:
      n.addInputToMemory()

  def dumpState(self):

    print "number of Neurons:", self.neuronCounter
    for n in self.neurons:
      print "ID: %d Level: %s" % (n.id,n.level)
      outIDs = [ str(x.id) for x in n.outNeurons]
      print "out neurons:",','.join(outIDs)
      inIDs = [ str(x.id) for x in n.inNeurons]
      print "in neurons:",','.join(inIDs)
      print "memory length", len(n.memory)
