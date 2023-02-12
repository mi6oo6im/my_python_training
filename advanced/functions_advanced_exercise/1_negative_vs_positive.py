numbers = [int(x) for x in input().split()]
positive = list(filter(lambda x: x > 0, numbers))
negative = list(filter(lambda x: x < 0, numbers))
sum_positive = sum(positive)
sum_negative = sum(negative)
print(sum_negative)
print(sum_positive)
print("The negatives are stronger than the positives" if abs(sum_negative) > abs(sum_positive) else
      "The positives are stronger than the negatives")
