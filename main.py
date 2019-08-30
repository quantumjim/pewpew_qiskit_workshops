from aether import *
import pew

pew.init()
screen = pew.Pix()

pew.show(screen)

qc = QuantumCircuit(2,2)

change = QuantumCircuit(2,2)

meas = QuantumCircuit(2,2)
meas.measure(0,0)
meas.measure(1,1)

# here we turn on a set of pixels, to provide a frame around results from our qubits
for (X,Y) in [(1,2),(6,2),(1,4),(6,4)]:
  for dX in [+1,0,-1]:
    for dY in [+1,0,-1]:
      screen.pixel(X+dX,Y+dY,1)
  screen.pixel(X,Y,0)
pew.show(screen)

line = {'Z':2,'X':4}
basis = ['Z','Z']

while True:

  change.data.clear()

  # we use button presses to implement x gates
  keys = pew.keys()
  if keys==pew.K_UP:
    qc.h(0)
  elif keys==pew.K_DOWN:
    qc.h(1)
  if keys==pew.K_LEFT:
    qc.cx(0,1)
  elif keys==pew.K_RIGHT:
    qc.cx(1,0)
  if keys==pew.K_X:
    if basis[0]=='Z':
      basis[0] = 'X'
    else:
      basis[0] = 'Z'
  elif keys==pew.K_O:
    if basis[1]=='Z':
      basis[1] = 'X'
    else:
      basis[1] = 'Z'

  if basis[0]=='X':
    change.h(0)
  if basis[1]=='X':
    change.h(1)

  out = execute(qc+change+meas,shots=1,get='memory')[0]  

  screen.pixel(1,2,1)
  screen.pixel(6,2,1)
  screen.pixel(1,4,1)
  screen.pixel(6,4,1)

  if out=='00':
    screen.pixel(1,line[basis[1]],0)
    screen.pixel(6,line[basis[0]],0)
  elif out=='01':
    screen.pixel(1,line[basis[1]],0)
    screen.pixel(6,line[basis[0]],3)
  elif out=='10':
    screen.pixel(1,line[basis[1]],3)
    screen.pixel(6,line[basis[0]],0)
  elif out=='11':
    screen.pixel(1,line[basis[1]],3)
    screen.pixel(6,line[basis[0]],3)


  pew.show(screen)
  pew.tick(1/6)