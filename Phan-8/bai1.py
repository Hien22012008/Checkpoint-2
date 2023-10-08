high_scores = [67, 78, 99 , 100]
print(high_scores)

high_scores.append(int(input('Input score:')))

high_score = high_scores.copy()

high_score.sort(reverse = True)
print(high_score)