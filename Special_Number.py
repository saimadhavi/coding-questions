SPECIAL_NUMBERS = set(3**p + 5**q for p in range(1, 10) for q in range(1, 10)) | \
                  set(3**p + 7**q for p in range(1, 10) for q in range(1, 10)) | \
                  set(5**p + 7**q for p in range(1, 10) for q in range(1, 10))
spcl_list= sorted(SPECIAL_NUMBERS)     
print(spcl_list)
def is_special_number(number):
    return number in SPECIAL_NUMBERS

def min_cost_to_special(number, decreasing_cost, increasing_cost):
    if number < spcl_list[0]:
        c=spcl_list[0]-number
        return increasing_cost *c
    else:
        #for i in range(len(spcl_list
        i = 0
        len_spcl_list = len(spcl_list)
        while (number > spcl_list[i] and i < len_spcl_list):
            i=i+1
        increasing_cost= increasing_cost * (spcl_list[i]-number)
        decreasing_cost= decreasing_cost * (number- spcl_list[i-1])
        return min(increasing_cost,decreasing_cost)

    
t = int(input())
for _ in range(t):
    number = int(input())
    decreasing_cost = int(input())
    increasing_cost = int(input())
    print(min_cost_to_special(number, decreasing_cost, increasing_cost))
