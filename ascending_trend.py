import sys
import statistics


if len(sys.argv) < 2:
    sys.exit('This program needs exactly one argument: "INT_STRING"')

try:
    int(sys.argv[1])
except ValueError as e:
    print(f'{e} Invalid INT_STRING')
    sys.exit(1)

int_string = sys.argv[1]
str_segments = ['' for i in range(len(int_string))]
segment_index = 0
str_segments[segment_index] += int_string[0]
counter = 1

for i in range(len(int_string)):
    if counter == len(int_string):
        break
    counter += 1
    if int(int_string[i+1]) > int(int_string[i]):
        str_segments[segment_index] += int_string[i+1]
    else:
        segment_index += 1
        str_segments[segment_index] += int_string[i+1]

longest = max(str_segments, key=len)
average = statistics.mean([int(i) for i in list(longest)])

print(
    f'Longest substring in numeric ascending order is: {longest} Average: '
    f'{average:.2f}'
    )
