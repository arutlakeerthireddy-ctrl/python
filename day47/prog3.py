#Print an inverted right triangle.
for i in range(6,0,-1):
    print("* "*i)

"""output
* * * * * * 
* * * * * 
* * * *
* * *
* *
*     """

#Print a left-aligned triangle with spaces.
n=6
for i in range(1,n):
    print(" "*(n-i)+"* "*i)
"""output
     *
    * *
   * * *
  * * * *
 * * * * *  """

#Right-Aligned Triangle
n=6
for i in range(1,n):
    print(" " * (n-i) + "* " * i)

"""output

     *
    * * 
   * * *
  * * * *
 * * * * *   """


