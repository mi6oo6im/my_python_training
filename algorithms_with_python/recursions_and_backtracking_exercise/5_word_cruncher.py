def find_all_solutions(idx, target_word, words_by_idx, words_count, used_words):
    if idx >= len(target_word):
        print(' '.join(used_words))
        return

    if idx not in words_by_idx:
        return

    for word in words_by_idx[idx]:
        if words_count[word] <= 0:
            continue
        # pre-recursion call
        used_words.append(word)
        words_count[word] -= 1

        find_all_solutions(idx + len(word), target_word, words_by_idx, words_count, used_words)
        # post-recursion call
        used_words.pop()
        words_count[word] += 1


words = input().split(', ')
target = input()

words_by_idx = {}
words_count = {}

for word in words:
    if word not in words_count:
        words_count[word] = 0
    words_count[word] += 1

    try:
        idx = 0
        while True:
            idx = target.index(word, idx)
            if idx not in words_by_idx:
                words_by_idx[idx] = set()
            words_by_idx[idx].add(word)
            idx += len(word)

    except ValueError:
        pass

find_all_solutions(0, target, words_by_idx, words_count, [])
