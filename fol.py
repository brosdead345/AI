from pyDatalog import pyDatalog

# Define the PyDatalog facts for the given atomic sentences
pyDatalog.create_terms('has_leg, likes, brother_of, X, Y, Z')

# John has a leg
+ has_leg('John')

# Raju likes fish
+ likes('Raju', 'fish')

# Raju is the brother of Rani
+ brother_of('Raju', 'Rani')

# Query the facts and print the results
print(has_leg(X))  # Query if someone has a leg
print(likes('Raju', Y))  # Query if Raju likes something and get the result in Y
print(brother_of('Raju', Z))  # Query if Raju is the brother of someone and get the result in Z



from pyDatalog import pyDatalog

# Define some facts
pyDatalog.create_terms('employee, salary')
+ employee('Alice', 50000)
+ employee('Bob', 60000)

# Query data
print(employee(X, Y))  # Query all employees and their salaries


from pyDatalog import pyDatalog

# Define facts and rules
pyDatalog.create_terms('parent, ancestor, X, Y, Z')
+ parent('alex', 'sharon')
+ parent('sharon', 'Charlie')
ancestor(X, Y) <= parent(X, Y)
ancestor(X, Y) <= (parent(X, Z) & ancestor(Z, Y))

# Query for ancestors
print(ancestor(X, 'Charlie'))

from pyDatalog import pyDatalog

# Define some facts
pyDatalog.create_terms('parent1, grandparent')
+ parent1('Alan', 'Bobby')
+ parent1('Bobby', 'ange')
+ parent1('ange', 'Danny')
# Define a rule
grandparent(X, Y) <= (parent1(X, Z) & parent1(Z, Y))
# Query for all grandparents
result = grandparent(X, Y)
print(result)

from pyDatalog import pyDatalog

# Define some facts
pyDatalog.create_terms('age, citizen,can_vote,X,A')
+ age('Alice', 20)
+ citizen('Alice', 'USA')
+ age('JOHN', 10)
+ citizen('Alice', 'USA')

can_vote(X) <= (age(X, A) & citizen(X, 'USA') & (A > 18))
result = can_vote(X)
print(result)
from pyDatalog import pyDatalog

# Define some facts
pyDatalog.create_terms('age, citizen,can_vote,X,A')
+ age('Alice', 20)
+ citizen('Alice', 'USA')
+ age('JOHN', 10)
+ citizen('Alice', 'USA')

can_vote(X) <= (age(X, A) & citizen(X, 'USA') & (A > 18))
result = can_vote(X)
print(result)
from pyDatalog import pyDatalog

# Define the domain of individuals
pyDatalog.create_terms('king, greedy, evil, X')

# Define the set of individuals who are kings and greedy
+ king('john')
+ greedy('john')
+ king('jack')
+ greedy('jack')
+ king('tom')

evil(X) <= (king(X) & greedy(X))

# Query to find individuals who are both kings and greedy
result = evil(X)
print(result)
