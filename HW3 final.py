# HW3
# REMINDER: The work in this assignment must be your own original work and must be completed alone.


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return "Node({})".format(self.value)

    __repr__ = __str__


#=============================================== Part I ==============================================

class Stack:
    '''
        >>> x=Stack()
        >>> x.pop()
        >>> x.push(2)
        >>> x.push(4)
        >>> x.push(6)
        >>> x
        Top:Node(6)
        Stack:
        6
        4
        2
        >>> x.pop()
        6
        >>> x
        Top:Node(4)
        Stack:
        4
        2
        >>> len(x)
        2
        >>> x.peek()
        4
    '''
    def __init__(self):
        self.top = None
        self.count=0
    
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__

    def isEmpty(self):
        # YOUR CODE STARTS HERE

        # Return True when its empty, False otherwise.
        return self.top == None

    def __len__(self): 
        # YOUR CODE STARTS HERE

        # return the number of items on the stack
        return self.count

    def push(self,value):
        # YOUR CODE STARTS HERE
        
        # set a new node
        new_node =  Node(value)

        # if the stack is empty, push to the stack and make it the top
        if self.isEmpty():
            self.top = new_node
            self.count += 1
        
        # if the stack is not empty, push the new node in and make it the top
        else:
            new_node.next = self.top
            self.top = new_node
            self.count += 1


    def pop(self):
        # YOUR CODE STARTS HERE
        
        # If the stack is not empty, delete the top and make the next the top.
        if not self.isEmpty():
            current = self.top

            top = current
            top1 = self.top.value

            current = current.next
            self.top = current
            top = None
            self.count -= 1
            return top1
        else:
            return

    def peek(self):
        # YOUR CODE STARTS HERE

        # return the value of the top
        if not self.isEmpty():
            return self.top.value

        else:
            return

#=============================================== Part II ==============================================

class Calculator:
    def __init__(self):
        self.__expr = None


    @property
    def getExpr(self):
        return self.__expr

    def setExpr(self, new_expr):
        if isinstance(new_expr, str):
            self.__expr=new_expr
        else:
            print('setExpr error: Invalid expression')
            return None

    def _isNumber(self, txt):
        '''
            >>> x=Calculator()
            >>> x._isNumber(' 2.560 ')
            True
            >>> x._isNumber('7 56')
            False
            >>> x._isNumber('2.56p')
            False
        '''
        try:
            float(txt)
        except ValueError:
            return False
        return True


    def _getPostfix(self, txt):
        '''
            Required: _getPostfix must create and use a Stack for expression processing
            >>> x=Calculator()
            >>> x._getPostfix('     2 ^       4')
            '2.0 4.0 ^'
            >>> x._getPostfix('          2 ')
            '2.0'
            >>> x._getPostfix('2.1        * 5        + 3       ^ 2 +         1 +             4.45')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.45 +'
            >>> x._getPostfix('2*5.34+3^2+1+4')
            '2.0 5.34 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('( .5 )')
            '0.5'
            >>> x._getPostfix ('( ( 2 ) )')
            '2.0'
            >>> x._getPostfix ('2 * (           ( 5 +-3 ) ^ 2 + (1 + 4 ))')
            '2.0 5.0 -3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('(2 * ( ( 5 + 3) ^ 2 + (1 + 4 )))')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('((2 *((5 + 3  ) ^ 2 + (1 +4 ))    ))')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix('2* (       -5 + 3 ) ^2+ ( 1 +4 )')
            '2.0 -5.0 3.0 + 2.0 ^ * 1.0 4.0 + +'

            # In invalid expressions, you might print an error message, adjust doctest accordingly
            # If you are veryfing the expression in calculate before passing to postfix, this cases are not necessary

            >>> x._getPostfix('2 * 5 + 3 ^ + -2 + 1 + 4')
            >>> x._getPostfix('     2 * 5 + 3  ^ * 2 + 1 + 4')
            >>> x._getPostfix('2    5')
            >>> x._getPostfix('25 +')
            >>> x._getPostfix(' 2 * ( 5      + 3 ) ^ 2 + ( 1 +4 ')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^  2 + ) 1 + 4 (')
            >>> x._getPostfix('2 *      5% + 3       ^ + -2 +1 +4')
        '''
        # YOUR CODE STARTS HERE
        postfixStack = Stack()  # method must use postfixStack to compute the postfix expression

        #Define nessesary variables
        postfix = ""

        operators_lst = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}

        invalid_lst = []
        
        open_bracket, close_bracket, numb, operator = 0, 0, 0, 0

        for i in txt.split(): #loop through every char in txt and append it to the lst to check for invalid txt entry
            invalid_lst.append(i)
            

        for i in range(len(invalid_lst)-1):# checks if the lst ends with a operator if so return none
            if invalid_lst[i] in '+-*/^':
              if invalid_lst[i+-1] in '+-*/^':
                return None

        for i in range(len(invalid_lst)): #checks for specific operators in the appended list and increment values based on operator type
            if invalid_lst[i] == '(':
                open_bracket +=1
            elif invalid_lst[i] == ')':
                close_bracket +=1
            elif self._isNumber(invalid_lst[i]): #check if the value is a number then increment after
                numb += 1
            elif invalid_lst[i] in '+-*/^':
                operator += 1

        if open_bracket != close_bracket or numb != operator+1:
            return None

        for i in txt.split(): #loop through and check for numbers in the txt then append into postfix
            if self._isNumber(i):
                postfix += str(float(i)) + " "
            elif i == "(": #if the element is a bracket then push down and become top of stack
                postfixStack.push(i)
            elif i == ")":
                while not postfixStack.isEmpty() and postfixStack.peek() != "(": #while loop for when the stack is not empty and the top of the stack is not a open bracket remove it 
                    postfix += str(postfixStack.pop()) + " " 
                postfixStack.pop()
            else:
                if i not in operators_lst: #if there's no operators in the operator list return none
                    return None
                if not postfixStack.isEmpty() and i == "^" and postfixStack.peek() == "^": #if the stack is not empty and there is an exponent, move it to the top of the stack and push stakc down
                    postfixStack.push(i)
                else:
                    while not postfixStack.isEmpty() and postfixStack.peek() != "(" and operators_lst[i] <= operators_lst[postfixStack.peek()] : #while loop for when the stack is not empty and the top is not a bracket and the operator list is the same or less than the top of the stack
                        postfix += str(postfixStack.pop()) + " " #remove and push stack down
                    postfixStack.push(i)
        while not postfixStack.isEmpty(): #while the stack is not empty 
            if postfixStack.peek() in "()": #if the top of the stack contains a bracket return none 
                return None
            postfix += str(postfixStack.pop()) + " " #removve the bracket 
        return postfix.rstrip() #retunr the strng no white spaces



    @property
    def calculate(self):
        '''
            calculate must call _getPostfix
            calculate must create and use a Stack to compute the final result as shown in the video lecture
            
            >>> x=Calculator()
            >>> x.setExpr('4        + 3 -       2')
            >>> x.calculate
            5.0
            >>> x.setExpr('-2 +          3.5')
            >>> x.calculate
            1.5
            >>> x.setExpr('      4 +           3.65  - 2        / 2')
            >>> x.calculate
            6.65
            >>> x.setExpr('23 / 12 - 223 + 5.25      * 4 * 3423')
            >>> x.calculate
            71661.91666666667
            >>> x.setExpr('2-3*4')
            >>> x.calculate
            -10.0
            >>> x.setExpr('7^2^3')
            >>> x.calculate
            5764801.0
            >>> x.setExpr(' 3 * ((( 10 - 2*3 )) )')
            >>> x.calculate
            12.0
            >>> x.setExpr('      8 / 4 * (3 - 2.45 * ( 4   - 2 ^ 3 )       ) + 3')
            >>> x.calculate
            28.6
            >>> x.setExpr('2 * ( 4 +        2 * (         5 - 3 ^ 2 ) + 1 ) + 4')
            >>> x.calculate
            -2.0
            >>> x.setExpr(' 2.5 +         3 * (2 + ( 3.0) * ( 5^2-2 * 3 ^ ( 2 )         ) * ( 4 ) ) * ( 2 / 8 + 2 * ( 3 - 1 /3 ) ) - 2 / 3^ 2')
            >>> x.calculate
            1442.7777777777778
            

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            >>> x.setExpr(" 4 ++ 3+ 2") 
            >>> x.calculate
            >>> x.setExpr("4  3 +2")
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 *( 2 - 3 * 2 ) )')
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * / ( 2 - 3 * 2 )')
            >>> x.calculate
            >>> x.setExpr(' ) 2 ( *10 - 3 * ( 2 - 3 * 2 ) ')
            >>> x.calculate
            >>> x.setExpr('(    3.5 ) ( 15 )') 
            >>> x.calculate
            >>> x.setExpr('3 ( 5) - 15 + 85 ( 12)') 
            >>> x.calculate
            >>> x.setExpr("( -2/6) + ( 5 ( ( 9.4 )))") 
            >>> x.calculate
        '''


        if not isinstance(self.__expr,str) or len(self.__expr)<=0:
            print("Argument error in calculate")
            return None

        calcStack = Stack()   # method must use calcStack to compute the  expression

        post = self._getPostfix(self.__expr) 
        
        #check if the string is empty if so return none
        if post == None:
            return None

        for i in post.split(): #for loop to loop through  the elements if the elemens is a number then push stack down
            if self._isNumber(i):
                calcStack.push(i)
            else:
                num1 = calcStack.pop() #remove number
                num2 = calcStack.pop()
                if i == "+": #perform operation based on operators
                    calcStack.push(float(num2) + float(num1))
                elif i == "-":
                    calcStack.push(float(num2) - float(num1))
                elif i == "*":
                    calcStack.push(float(num2) * float(num1))
                elif i == "/":
                    calcStack.push(float(num2) / float(num1))
                elif i == "^":
                    calcStack.push(float(num2) ** float(num1))
        return calcStack.pop()

#=============================================== Part III ==============================================

class AdvancedCalculator:
    '''
        >>> C = AdvancedCalculator()
        >>> C.states == {}
        True
        >>> C.setExpression('a = 5;b = 7 + a;a = 7;c = a + b;c = a * 0;return c')
        >>> C.calculateExpressions() == {'a = 5': {'a': 5.0}, 'b = 7 + a': {'a': 5.0, 'b': 12.0}, 'a = 7': {'a': 7.0, 'b': 12.0}, 'c = a + b': {'a': 7.0, 'b': 12.0, 'c': 19.0}, 'c = a * 0': {'a': 7.0, 'b': 12.0, 'c': 0.0}, '_return_': 0.0}
        True
        >>> C.states == {'a': 7.0, 'b': 12.0, 'c': 0.0}
        True
        >>> C.setExpression('x1 = 5;x2 = 7 * ( x1 - 1 );x1 = x2 - x1;return x2 + x1 ^ 3')
        >>> C.states == {}
        True
        >>> C.calculateExpressions() == {'x1 = 5': {'x1': 5.0}, 'x2 = 7 * ( x1 - 1 )': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        True
        >>> print(C.calculateExpressions())
        {'x1 = 5': {'x1': 5.0}, 'x2 = 7 * ( x1 - 1 )': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        >>> C.states == {'x1': 23.0, 'x2': 28.0}
        True
        >>> C.setExpression('x1 = 5 * 5 + 97;x2 = 7 * ( x1 / 2 );x1 = x2 * 7 / x1;return x1 * ( x2 - 5 )')
        >>> C.calculateExpressions() == {'x1 = 5 * 5 + 97': {'x1': 122.0}, 'x2 = 7 * ( x1 / 2 )': {'x1': 122.0, 'x2': 427.0}, 'x1 = x2 * 7 / x1': {'x1': 24.5, 'x2': 427.0}, '_return_': 10339.0}
        True
        >>> C.states == {'x1': 24.5, 'x2': 427.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;C = A + B;A = 20;D = A + B + C;return D - A')
        >>> C.calculateExpressions() == {'A = 1': {'A': 1.0}, 'B = A + 9': {'A': 1.0, 'B': 10.0}, 'C = A + B': {'A': 1.0, 'B': 10.0, 'C': 11.0}, 'A = 20': {'A': 20.0, 'B': 10.0, 'C': 11.0}, 'D = A + B + C': {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}, '_return_': 21.0}
        True
        >>> C.states == {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;2C = A + B;A = 20;D = A + B + C;return D + A')
        >>> C.calculateExpressions() is None
        True
        >>> C.states == {}
        True
    '''

    def __init__(self):
        self.expressions = ''
        self.states = {}

    def setExpression(self, expression):
        self.expressions = expression
        self.states = {}

    def _isVariable(self, word):
        '''
            >>> C = AdvancedCalculator()
            >>> C._isVariable('volume')
            True
            >>> C._isVariable('4volume')
            False
            >>> C._isVariable('volume2')
            True
            >>> C._isVariable('vol%2')
            False
        '''
        if isinstance(word, str) and len(word) > 0:
            if word[0].isalpha() and word.isalnum():
                return True
        return False


    def _replaceVariables(self, expr):
        '''
            >>> C = AdvancedCalculator()
            >>> C.states = {'x1': 23.0, 'x2': 28.0}
            >>> C._replaceVariables('1')
            '1'
            >>> C._replaceVariables('105 + x')
            >>> C._replaceVariables('7 * ( x1 - 1 )')
            '7 * ( 23.0 - 1 )'
            >>> C._replaceVariables('x2 - x1')
            '28.0 - 23.0'
        '''
        replaced = expr.split()
        for x in range(len(replaced)): #for loop for each x in split
            if self._isVariable(replaced[x]): #if the variable is x and is in states then replace x with number otherwise return none
                if replaced[x] in self.states:
                    replaced[x] = str(self.states[replaced[x]])
                else:
                    return None
        return " ".join(replaced) #return the replaced variable


    def calculateExpressions(self):
        self.states = {}
        calc = Calculator() #call calculator class
        d = {}
        expression = self.expressions.strip().split(";") #strip and split the expression
        for x in expression[:-1]: #for loop starting from the back
            var = x.split("=")[0].strip() #remove the = operator
            calc.setExpr(str(self._replaceVariables(x.split("=")[1])))#send the value with = removed
            if calc.calculate != None: # if calculate class did not return none 
                self.states[var] = float(calc.calculate) # append as variable into the dictionary 
            else:
                self.states = {} #empty the dictionary
                return None
            d[x] = self.states.copy() #copy the dictonary 
        calc.setExpr(str(self._replaceVariables(expression[-1].split('return')[1])))
        d['_return_'] = float(calc.calculate)
        return d
if __name__ == "__main__":
    import doctest
    doctest.testmod()