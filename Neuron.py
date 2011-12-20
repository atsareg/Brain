""" Class Neuron represents a neuron model in the Brain Antenna theory
"""

from numpy import *
import random

class Neuron:

  def __init__(self,id):

    self.id = id
    self.level = 0.
    self.outNeurons = []
    self.inNeurons = []
    self.locked = False
    self.memory = []

  def lock(self):
    self.locked = True

  def unlock(self):
    self.locked = False

  def addInNeuron(self,neuron):

    if type(neuron) == type(self):
      self.inNeurons.append(neuron)
    else:
      print "invalid object type"

  def addOutNeuron(self,neuron):

    if type(neuron) == type(self):
      self.outNeurons.append(neuron)
    else:
      print "invalid object type"

  def setLevel(self,level):

    self.level = level

  def getInputLevel(self):

    if self.locked:
      return self.level,self.level

    inLevel = 0.
    for n in self.inNeurons:
      inLevel += n.level

    oldlevel = self.level
    self.level = inLevel/len(self.inNeurons)

    return oldlevel,self.level

  def addRandomMemory(self):

    marray = array([ random.random() for x in range(len(self.inNeurons)) ])
    self.memory.append(marray)

  def addInputToMemory(self):

    marray = array([ x.level for x in self.inNeurons])
    stddev = std(marray)
    if stddev > 0.1:
      #print ">>>",self.id,stddev,marray
      self.memory.append(marray)

  def getBestMatchToMemory(self):

    if self.locked:
      return self.level,self.level

    input = array([ x.level for x in self.inNeurons])
    mcorr = 0.
    for marray in self.memory:
      corr = corrcoef(marray,input)[1,0]
      if abs(mcorr) < abs(corr):
        mcorr = corr

    return self.level,mcorr