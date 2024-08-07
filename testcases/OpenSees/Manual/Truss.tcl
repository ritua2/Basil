# OpenSees -- Open System for Earthquake Engineering Simulation
# Pacific Earthquake Engineering Research Center
# http://opensees.berkeley.edu/
#
# Basic Truss Example
# ----------------------
#  2d 3 Element Elastic Truss
#  Single Nodal Load, Static Analysis
# 
# Example Objectives
# -----------------
#  Simple Introduction to OpenSees
# 
# Units: kips, in, sec
# Written: fmk
# Date: January 2001

# ------------------------------
# Start of model generation
# ------------------------------

# Remove existing model
wipe

# Create ModelBuilder (with two-dimensions and 2 DOF/node)
model BasicBuilder -ndm 2 -ndf 2

# Create nodes
# ------------
    
# Create nodes & add to Domain - command: node nodeId xCrd yCrd
node 1   0.0  0.0
node 2 144.0  0.0
node 3 168.0  0.0
node 4  72.0 96.0

# Set the boundary conditions - command: fix nodeID xResrnt? yRestrnt?
fix 1 1 1 
fix 2 1 1
fix 3 1 1

# Define materials for truss elements
# -----------------------------------

# Create Elastic material prototype - command: uniaxialMaterial Elastic matID E
uniaxialMaterial Elastic 1 3000

# Define elements
# ---------------

# Create truss elements - command: element truss trussID node1 node2 A matID
element Truss 1 1 4 10.0 1
element Truss 2 2 4  5.0 1
element Truss 3 3 4  5.0 1
    
# Define loads
# ------------

#create a Linear TimeSeries (load factor varies linearly with time): command timeSeries Linear $tag
timeSeries Linear 1

# Create a Plain load pattern with a linear TimeSeries: command pattern Plain $tag $timeSeriesTag { $loads }
pattern Plain 1 1 {
    
    # Create the nodal load - command: load nodeID xForce yForce
    load 4 100 -50
}
    
# ------------------------------
# Start of analysis generation
# ------------------------------

# Create the system of equation, a SPD using a band storage scheme
system BandSPD

# Create the DOF numberer, the reverse Cuthill-McKee algorithm
numberer RCM

# Create the constraint handler, a Plain handler is used as homo constraints
constraints Plain

# Create the integration scheme, the LoadControl scheme using steps of 1.0
integrator LoadControl 1.0

# Create the solution algorithm, a Linear algorithm is created
algorithm Linear

# create the analysis object 
analysis Static 

# ------------------------------
# Start of recorder generation
# ------------------------------

# create a Recorder object for the nodal displacements at node 4
recorder Node -file example.out -time -node 4 -dof 1 2 disp

# Create a recorder for element forces, one in global and the other local system
recorder Element -file eleGlobal.out -time -ele 1 2 3 forces
recorder Element -file eleLocal.out -time -ele 1 2 3  basicForces

# ------------------------------
# Finally perform the analysis
# ------------------------------

# Perform the analysis
analyze 1

# ------------------------------
# Print Stuff to Screen
# ------------------------------

# Print the current state at node 4 and at all elements
puts "node 4 displacement: [nodeDisp 4]"
print node 4
print ele

