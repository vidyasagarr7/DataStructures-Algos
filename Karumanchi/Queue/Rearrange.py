from Karumanchi.Queue import Queue

def rearrange(input_que):
    temp_que = Queue.Queue1()
    is_length_odd = True if input_que.size%2 ==1 else False
    mid = input_que.size//2
    for i in range(mid):
        temp_que.enqueue(input_que.dequeue())
    while not temp_que.is_empty():
        input_que.enqueue(temp_que.dequeue())
        input_que.enqueue(input_que.dequeue())
    if is_length_odd:
        input_que.enqueue(input_que.dequeue())
    return input_que

if __name__=="__main__":
    que = Queue.Queue1()
    for i in range(11,22):
        que.enqueue(i)
    rearrange(que)
    while not que.is_empty():
        print(que.dequeue())