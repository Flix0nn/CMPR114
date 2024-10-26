total = 0

for i in range(5):
    day = int(input('how many bugs wer collected on day ' + str(i + 1) + "? "))
    total += day

print('Total number of bugs collected: ' + str(total))