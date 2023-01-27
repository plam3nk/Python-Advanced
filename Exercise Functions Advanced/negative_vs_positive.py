def negative_positive(*args):

    positive = 0
    negative = 0

    for number in args:
        if int(number) < 0:
            negative += int(number)
        else:
            positive += int(number)
    print(negative)
    print(positive)
    if abs(positive) > abs(negative):
        print("The positives are stronger than the negatives")

    elif abs(positive) < abs(negative):
        print("The negatives are stronger than the positives")


input_line = input().split()
negative_positive(*input_line)
