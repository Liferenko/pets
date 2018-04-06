N = 9
name = ['paul', 'fedor', 'makar', 'sanya', 'alex', 'egor', 'stepan', 'igor', 'artem', 'maksim', 'genadij']

square = [ i for i in range(N) ]

round = ( i for i in range(N) )

curly = { i for i in range(N) }

double_dots = { name[i]: i for i in range(N) }

print( "1) Square - {} \n --- \n2) Round - {} \n --- \n Curly - {} \n --- \n Double dots - {}".format(square, round, curly, double_dots) )
