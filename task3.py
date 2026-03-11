count = 6
def increment():
    global count
    count += 12
    print(f"count inside the function: {count}")
    
increment()


print(f"count inside the function: {count}")