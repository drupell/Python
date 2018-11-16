'''
Programmer: David Rupell
Date: 11/16/2018
Description: Ackermann function example using recursion and an object
oriented approach.
**Warning: AckermanFct(3, 6) appears to be the highest calculatable value
  so far.
'''



class AckermannFct:
    def __init__(self, m, n):
        if m > 0 and n > 0:
            
            '''
            Mutator: ack(m,n) takes the two passed integers and computes the
            solution to the Ackermann function recursively.
            Preconditions: if one of the integers passed are negative, the
            function will never even be defined.
            Postconditions: computes and returns the solution recursively.
            '''
            def ack(m, n):
                if m == 0:
                    return n + 1
                elif n == 0:
                    return ack(m-1, 1);
                else:
                    return ack(m-1, ack(m, n-1))
            #self.m = int(m)
            #self.n = int(n)
            print("When the numbers " + str(m) + " and " + str(n)
                  + " are plugged into the Ackermann Function,\n"
                  + "We get: [" + str(ack(m, n)) + "]")
        else:
            print("Error: Integers entered must be positive.\n"
                    +"Cannot compute solution to Ackermann function.")

def main():
    AckermannFct(1,6)

main()
