total = 0
def add (num):
    global total
    total += num

def display():
    print(f"total_sum:{total}")    

add(7)    
add(14)
display()