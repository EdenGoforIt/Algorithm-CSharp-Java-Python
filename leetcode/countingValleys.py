def countingValleys(steps, path):
    step_count = 0
    valley_count = 0
    valley_started = False
    for step in path:
        if step == "U":
            step_count += 1
        else:
            step_count -= 1
        if step_count < 0:
            valley_started = True
        if step_count == 0 and valley_started:
            valley_count += 1
            valley_started = False

    return valley_count


if __name__ == '__main__':
    print(countingValleys(8, 'UDDDUDUU'))
