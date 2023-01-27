def printer(positive, negative):

    print(negative)
    print(positive)
    if abs(positive) > abs(negative):
        print("The positives are stronger than the negatives")

    elif abs(positive) < abs(negative):
        print("The negatives are stronger than the positives")


positive_numbers = 0
negative_numbers = 0

for number in input().split():
    if int(number) < 0:
        negative_numbers += int(number)
    else:
        positive_numbers += int(number)

printer(positive_numbers, negative_numbers)

