def distributeCandies(candies, num_people):
    distribution = [0 for i in range(num_people)]
    count = 1
    while candies != 0:
        for index, person in enumerate(distribution):
            if candies > count:
                distribution[index] += count
                candies -= count
                count += 1
            else:
                distribution[index] += candies
                candies = 0
    return distribution


distributeCandies(10, 3)
