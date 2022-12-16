def solution(numbers):
    numbers_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for num, num_en in enumerate(numbers_list): 
        numbers =  str(num).join(numbers.split(num_en))
    answer = int(numbers)
    return answer