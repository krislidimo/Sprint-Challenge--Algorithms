'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_helper(count, word):
	index = word.find('th')

	if index == -1:
		return count
	else:
		count += 1
		return count_helper(count, word[index+2:])

	return count

def count_th(word):
    count = 0
    count = count_helper(count, word)

    return count