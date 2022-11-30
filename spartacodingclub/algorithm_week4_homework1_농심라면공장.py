import heapq

def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    answer = 0
    last_added_date_index = 0 #공장이 멈추지 않는 한 가장 마지막에 넣은 날짜의 인덱스
    max_heap = []

    while stock <= k: #현재 재고가 남은 날짜 보다 많게!
        while last_added_date_index < len(dates) and dates[last_added_date_index] <= stock: #루프를 돌다가 공장이 멈추지 않는 선에서 탈출
            heapq.heappush(max_heap, -supplies[last_added_date_index]) #-를 붙여야 max heap이 됨
            last_added_date_index += 1
            
        answer += 1
        heappop = heapq.heappop(max_heap) #최대값 뽑기
        stock += -heappop            

    return answer