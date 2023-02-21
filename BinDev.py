from random import randint
import statistics

week = [
['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'BLUE', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN'],
['ARSH', 'BROWN', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLEW', 'PINK', 'PINK', 'ORANGE', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'WHITE', 'BLUE', 'BLUE', 'BLUE'],
['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'RED', 'YELLOW', 'ORANGE', 'RED', 'ORANGE', 'RED', 'BLUE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'WHITE', 'WHITE'],
['BLUE', 'BLUE', 'GREEN', 'WHITE', 'BLUE', 'BROWN', 'PINK', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN'],
['GREEN', 'WHITE', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLACK', 'WHITE', 'ORANGE', 'RED', 'RED', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'WHITE']
]
week_nums = {}

#check if s is number or not
def isNan(s):
    try:
        if int(s):
            return False
    except:
        return True

def variance(list_num):
    return sum((x * mean(list_num)) ** 2 for x in list_num) / len(list_num)
def mean(list_num):
    total = 0
    for num in list_num:
        total += num
    return total / len(list_num)

def mode(obj):
    max_count = (0,'')
    for key, occ in obj.items():
        if occ > max_count[0]:
            max_count = (occ, key)
    return max_count[1]

def median(list_item):
    list_item.sort()
    if len(list_item) % 2 != 0:
        middle= int((len(list_item) - 1) / 2)
        return list_item[middle]
    elif len(list_item) % 2 == 0:
        middle_1 = int((len(list_item) - 1) / 2)
        middle_2 = int((len(list_item) - 1) / 2) + 1
        return (list_item[middle_1] + list_item[middle_2]) / 2

def fibonnaci(n, memo={}):
    if n in memo:
        return memo[n]
    if n in [0,1]:
        return n
    memo[n] = fibonnaci(n-1, memo) + fibonnaci(n-2, memo)
    return memo[n]

def onesAndZeros(num):
    lst_num = list(num)
    result = ''
    count_ones = 0
    for n in lst_num:
        if int(n) == 0:
            result += n
            count_ones = 0
        else:
            count_ones += 1
            if count_ones == 3:
                result += '1'
                count_ones = 0
            else:
                result += '0'
    return result


for day in week:
    sort_day = sorted(day)
    count = []
    for color in day:
        if color not in count:
            if week_nums.get(color):
               week_nums[color] += day.count(color)
            else:
                week_nums[color] = day.count(color)
            count.append(color)
print(f'{"_"*50}')        
print('   ...........')
print(f'   Total   {sum(week_nums.values()):3}')
print('   ...........')
print(f'   Mean    : {mean(week_nums.values()):^5f}')
print(f'   Mean2    : {statistics.mean(week_nums.values()):^5f}')
print(f'   Mode    : {mode(week_nums):^5}')
print(f'   Mode2   : {statistics.mode(week_nums.values()):^5f}')
print(f'   Median  : { median([*week_nums.values()]):^5}')
print(f'   Median2  : { statistics.median([*week_nums.values()]):^5}')
print(f'   Variance  : { variance([*week_nums.values()]):^5}')
print(f'{"_"*50}')
print('   sum of the fist 50 of fibonnaci sequence')
print(f'   {fibonnaci(50)}')
print(f'{"_"*50}')
print(f"   input  >>> 0101101011101011011101101000111 \n   output >>> {onesAndZeros('0101101011101011011101101000111')}")
print(f'{"_"*50}')
