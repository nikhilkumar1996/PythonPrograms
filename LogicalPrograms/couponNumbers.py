import random
""" Program 2: Given N distinct Coupon Numbers, how many random numbers do you
need to generate distinct coupon number? This program simulates this random
process.
"""


def coupon(range_of_num):
	"""
	coupon numbers generator
	:param range_of_num: Size od Coupon
	:return: Coupon
	"""

	num = '0123456789'
	coupon_no = ''   # empty string
	for i in range(0, range_of_num):
		rand = random.randint(0, len(num) - 1)  # will generate 6 random numbers
		coupon_no += str(rand)   # append numbers in coupon_no
	return coupon_no


if __name__ == "__main__":
	print(coupon(6))
