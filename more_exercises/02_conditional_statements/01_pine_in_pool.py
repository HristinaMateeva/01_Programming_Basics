volume = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

full_pool = (p1 * h) + (p2 * h)
percentage_full = (full_pool / volume * 100)
pipe_1_percentage = (p1 * h /full_pool * 100)
pipe_2_percentage = (p2 * h /full_pool * 100)

if full_pool <= volume:
    print(f"The pool is {percentage_full:.2f}% full. Pipe 1: {pipe_1_percentage:.2f}%. Pipe 2: {pipe_2_percentage:.2f}%.")
else:
    overflow = full_pool - volume
    print(f"For {h} hours the pool overflows with {overflow:.2f} liters.")
