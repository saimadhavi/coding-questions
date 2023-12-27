Conversion to a special number

Special numbers are those numbers which can be represented as sum of any two distinct single digit odd prime numbers with each of the two prime number having positive power.
Your task is to convert the given number into a special number in minimum cost. For making a non special number a special number, two operations can be done. First operation is that the current number can be increased by 1 and the associated cost with this operation is IncreasingCost and second operation is that the current number can be decreased by 1 and the associated cost with this is known as DecreasingCost.

Input format
First line: t (number of test cases)
For each test case:
• First line: It contains the number which needs to be converted into special number.
• Second line: DecreasingCost
• Third line: IncreasingCost

Output format
For each test case, print in a new line the minimum cost to convert the number into a special number.
Constraints
1 ≤ t ≤3*105
1<Number < 109
1≤ IncreasingCost ≤ 10°
1 < DecreasingCost ≤ 10

sample input :
1
4
7
8
sample output:
32
To make 4 a special number we can Increment the number 4 times to make it 8.8 is a special numbr since it can be represented as 3*1 + 5*1.Increment cost is 8 so total cost is 8+8+8+8=32
