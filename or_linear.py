#Google OR-tools linear optimization

from ortools.linear_solver import pywraplp

#linear optimization problem 1
#0<=x<=1,0<=y<=2, x+y<=2, 3x+y=max
def lp1():
    #create linear solver
    solver = pywraplp.Solver('simple_lp_program',pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
    
    #create viarables
    x = solver.NumVar(0,1,'x')
    y = solver.NumVar(0,2,'y')
    
    #constrains
    ct = solver.Constraint(0,2,'ct')
    ct.SetCoefficient(x,1)
    ct.SetCoefficient(y,1)
    
    #objective
    objective = solver.Objective()
    objective.SetCoefficient(x,3)
    objective.SetCoefficient(y,1)
    objective.SetMaximization()
    
    solver.Solve()
    
    print('Solutoin:')
    print('x = %.2f\ny = %.2f' %(x.solution_value(),y.solution_value()))
    print('Objective value = %.2f' %(objective.Value()))

#linear optimization problem 1
#3x-y>=0,x-y<=2, x+2y<=14, 3x+4y=max
def lp2():
    #create linear solver
    solver = pywraplp.Solver('1',pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
    
    #create viarables
    x = solver.NumVar(-solver.infinity(),solver.infinity(),'x')
    y = solver.NumVar(-solver.infinity(),solver.infinity(),'y')

    #constrains
    ct0 = solver.Constraint(0,solver.infinity())
    ct0.SetCoefficient(x,3)
    ct0.SetCoefficient(y,-1)
    
    #constrains
    ct1 = solver.Constraint(-solver.infinity(),2)
    ct1.SetCoefficient(x,1)
    ct1.SetCoefficient(y,-1)
    
    #constrains
    ct2 = solver.Constraint(-solver.infinity(),14)
    ct2.SetCoefficient(x,1)
    ct2.SetCoefficient(y,2)
    
    #objective
    objective = solver.Objective()
    objective.SetCoefficient(x,3)
    objective.SetCoefficient(y,4)
    objective.SetMaximization()
    
    solver.Solve()
    
    print('Solutoin:')
    print('x = %.2f\ny = %.2f' %(x.solution_value(),y.solution_value()))
    print('Objective value = %.2f' %(objective.Value()))  
lp2()