def latest(scores):
	order = sorted(scores)

	if min(order) == 0:
		return order[1]

	else:
   		return min(scores)


def personal_best(scores):
   	return max(scores)


def personal_top_three(scores):
    order=sorted(scores,reverse=True)
    return order[0:3]
