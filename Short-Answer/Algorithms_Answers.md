#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)

		a = 0                 		O(1)
    while (a < n * n * n):    O(n)
      a = a + n * n  					O(1)

		Iteratve example:
		  n=1 - 1 time
		  0 < 1
		  1 < 1 stop

		  n=2 - 2 times
		  0 < 8
		  4 < 8
		  8 < 8 stop

		  n=3 - 3 times
		  0 < 27
		  9 < 27
		  18 < 27
		  27 < 27 stop

		Big O calulation:
		  O(1) + O(n)*O(1) =
		  O(1) + O(1n) ~=
		  O(n)

		Exercise I(a) scales linearly with respect to n, O(n).


b)

		sum = 0               O(1)
    for i in range(n):    O(n)
      j = 1               O(1)
      while j < n:        O(n)
        j *= 2            O(1)
        sum += 1          O(1)

		Big O calulation:
		  O(1) + O(n)*(O(1) + O(n)*(O(1) + O(1))) =
		  O(1) + O(1n) + O(2n^2) ~=
		  O(n^2)

		Exercise I(b) scales quadraticly with respect to n, O(n^2).


c)

		def bunnyEars(bunnies):
      if bunnies == 0:                  O(1)
        return 0                        O(1)

      return 2 + bunnyEars(bunnies-1)   O(n)

		Big O calulation:
		  O(1)*O(1) + O(n) =
		  O(1) + O(n) ~=
		  O(n)

		Exercise I(c) scales linearly with respect to bunnies, O(n).

## Exercise II

		Step one:
		  Test the middle floor, f/2
		Step two:
		  If the egg breaks:
		    devide the building into two parts and move to the middle of the lower floors
		  if the egg doesn't break 
		    devide the building into two parts and move to the middle of the upper floors
		Step three:
		  repeat step two until your left with one floor

		This method is also known as  binary searh and has a time complexity of O(log n)
