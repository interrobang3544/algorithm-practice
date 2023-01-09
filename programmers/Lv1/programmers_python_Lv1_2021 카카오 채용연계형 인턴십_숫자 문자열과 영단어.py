def solution(s):
    word_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for word in word_list:
        if word in s:
            s = s.replace(word, str(word_list.index(word)))
    answer = int(s)
    return answer