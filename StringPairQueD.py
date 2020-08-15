'''
String Pair
Problem Description

One person hands over the list of digits to Mr. String, But Mr. String understands only strings. Within strings also he understands only vowels. Mr. String needs your help to find the total number of pairs which add up to a certain digit D.

The rules to calculate digit D are as follow

Take all digits and convert them into their textual representation

Next, sum up the number of vowels i.e. {a, e, i, o, u} from all textual representation

This sum is digit D

Now, once digit D is known find out all unordered pairs of numbers in input whose sum is equal to D. Refer example section for better understanding.

Constraints

1 <= N <= 100

1 <= value of each element in second line of input <= 100

Number 100, if and when it appears in input should be converted to textual representation as hundred and not as one hundred. Hence number of vowels in number 100 should be 2 and not 4

Input

First line contains an integer N which represents number of elements to be processed as input

Second line contains N numbers separated by space

Output

Lower case representation of textual representation of number of pairs in input that sum up to digit D

Note: - (If the count exceeds 100 print "greater 100")

Time Limit

1


Examples

Example 1

Input

5

1 2 3 4 5

Output

one

Explanation

1 -> one -> o, e

2 -> two -> o

3 -> three -> e, e

4 -> four -> o, u

5 -> five - > i, e

Thus, count of vowels in textual representation of numbers in input = {2 + 1 + 2 + 2 + 2} = 9. Number 9 is the digit D referred to in section above.

Now from given list of number {1,2,3,4,5} -> find all pairs that sum up to 9.

Upon processing this we know that only a single unordered pair {4, 5} sum up to 9. Hence the answer is 1. However, output specification requires you to print textual representation of number 1 which is one. Hence output is one.

Note: - Pairs {4, 5} or {5, 4} both sum up to 9. But since we are asking to count only unordered pair, the number of unordered pair is this combination is only one.

Example 2

Input

3

7 4 2

Output

zero

Explanation

7 -> seven -> e, e

4 -> four -> o, u

2 -> two -> o

Thus, count of vowels in textual representation of numbers in input = {2 + 2 + 1} = 5. Number 5 is the digit D referred to in section above.

Since no pairs add up to 5, the answer is 0. Textual representation of 0 is zero. Hence output is zero.

'''


length = int(input())
arr = input().split()
D = 0
count = 0
for ch in arr:
    if ch == '1':
        D += 2
    elif ch == '2':
        D += 1
    elif ch == '3':
        D += 2
    elif ch == '4':
        D += 2
    elif ch == '5':
        D += 2
    elif ch == '6':
        D += 1
    elif ch == '7':
        D += 2
    elif ch == '8':
        D += 2
    elif ch == '9':
        D += 2
    elif ch == '0':
        D += 2
tup = [(int(a),int(b)) for a in arr for b in arr]

for el in tup:
    if sum(el) == D:
        count += 1
        
ans = int(count/2)

def NumToWords(num,join=True):
    '''words = {} convert an integer number into words'''
    units = ['','one','two','three','four','five','six','seven','eight','nine']
    teens = ['','eleven','twelve','thirteen','fourteen','fifteen','sixteen', \
             'seventeen','eighteen','nineteen']
    tens = ['','ten','twenty','thirty','forty','fifty','sixty','seventy', \
            'eighty','ninety']
    thousands = ['','thousand','million','billion','trillion','quadrillion', \
                 'quintillion','sextillion','septillion','octillion', \
                 'nonillion','decillion','undecillion','duodecillion', \
                 'tredecillion','quattuordecillion','sexdecillion', \
                 'septendecillion','octodecillion','novemdecillion', \
                 'vigintillion']
    words = []
    if num==0: words.append('zero')
    else:
        numStr = '%d'%num
        numStrLen = len(numStr)
        groups = int((numStrLen+2)/3)
        numStr = numStr.zfill(groups*3)
        for i in range(0,groups*3,3):
            h,t,u = int(numStr[i]),int(numStr[i+1]),int(numStr[i+2])
            g = groups-(i/3+1)
            if h>=1:
                words.append(units[h])
                words.append('hundred')
            if t>1:
                words.append(tens[t])
                if u>=1: words.append(units[u])
            elif t==1:
                if u>=1: words.append(teens[u])
                else: words.append(tens[t])
            else:
                if u>=1: words.append(units[u])
            if (g>=1) and ((h+t+u)>0): words.append(thousands[g]+',')
    if join: return ' '.join(words)
    return words

if ans > 100:
    print("greater 100")
else:
    print(NumToWords(ans))