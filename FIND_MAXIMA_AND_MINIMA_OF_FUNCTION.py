# PROGRAM WILL BE SOON UPDATED 
# FOR FURTHER ENQUIRY YOU CAN DIRECT CONTACT ME





import sympy as smp

# Importing sympy library of python is done



x,y=smp.symbols('x y',real=True)
f=x**3+3*x*y**2-3*x**2-3*y**2+4
# f=sympify(input("Give equation in form of ax**3+b*x*y**2+c*x**2+d*y**2+e\n"))
    # above is used to take expression as input  
# print(f)
    # print the expression
def run():
    
    #for calculating first order derivative 

    x=smp.symbols('x',real=True)
    dfdx=smp.diff(f,x)          # first derivative wrt x keeping y constant
    y=smp.symbols('y',real=True)
    dfdy=smp.diff(f,y)          # first derivative wrt y keeping x constant 
    print("Derivative wrt x is ",dfdx)
    print("Derivative wrt y is ",dfdy)
    

    #for calculating second order derivative 

    x=smp.symbols('x',real=True)
    d2fx2=smp.diff(f,x,2)       #second derivative wrt x keeping y constant
    y=smp.symbols('y',real=True)
    d2fy2=smp.diff(f,y,2)       #second derivative wrt y keeping x constant
    print("Second Derivative wrt x is ",d2fx2)
    print("Second Derivative wrt x is ",d2fy2)
    

    #for calculating derivative of first order derivartive by using alternate variable 

    x=smp.symbols('x',real=True)
    d2fdxdy=smp.diff(f,x,y)         # finding derivative wrt y of dfdx
    y=smp.symbols('y',real=True)
    d2fdydx=smp.diff(f,y,x)         # finding derivative wrt x of dfdy 
    print("Derivative wrt x is ",d2fdxdy)
    print("Derivative wrt y is ",d2fdydx)

    


    # here putting dfdx=0 and dfdy=0 and finding cordinate as per need is not done 




    #a= #value if first obtained bracket which will be inserted in place of x 
    #b= #value if first obtained bracket which will be inserted in place of y
    # We have to update that value later to check another obtained point

    r=d2fx2.subs([(x,a),(y,b)]).evalf()
    s=d2fdxdy.subs([(x,a),(y,b)]).evalf()
    t=d2fy2.subs([(x,a),(y,b)]).evalf()
    # from this you will get substituted value of r,s and t respectively



    # Checking of given conditions and printing as per it is done below

    if r*t-s**2>0 and r<0:
        print(f"Function is Maximum at point ({a},{b})")
    elif r*t-s**2>0 and r>0:
        print(f"Function is Minimum at point ({a},{b})")
    elif r*t-s**2<0:
        print("Function is neither maximum nor minimum")
    else:
        print("There is an error")

    # finally you will get the respective information below

run()

# PROGRAM WILL BE SOON UPDATED 
# FOR FURTHER ENQUIRY YOU CAN DIRECT CONTACT ME 
# AVAIBLE ON LINKEDIN
# FOLLOW ON GITHUB AND LINKED FOR MORE INTERESTING CODES












# dfdx_f=smp.lambdify((x,a,b,c),dfdx) #convert numeric function for plotting 
# print(dfdx_f)


# x=np.linspace(1,2,100) #define x and y array using hte numerical function above
# print(x)
# y=dfdx_f(x,a=1,b=2,c=3)
# print(y)

#plotting of points on graph
# plt.plot(x,y)
# plt.ylabel('$d^4 f/ dx^4$', fontsize=24)
# plt.xlabel('$*$', fontsize=24)

