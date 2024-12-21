def damerau_levenshtein_distance(word1, word2):
    len1, len2 = len(word1), len(word2)
    dp = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]

    # Initialize the matrix
    for i in range(len1 + 1):
        dp[i][0] = i
    for j in range(len2 + 1):
        dp[0][j] = j

    # Compute distances
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            cost = 0 if word1[i - 1] == word2[j - 1] else 1

            dp[i][j] = min(dp[i - 1][j] + 1,     #! Deletion
                           dp[i][j - 1] + 1,     #! Insertion
                           dp[i - 1][j - 1] + cost)  #! Substitution
            if i > 1 and j > 1 and word1[i - 1] == word2[j - 2] and word1[i - 2] == word2[j - 1]:
                dp[i][j] = min(dp[i][j], dp[i - 2][j - 2] + 1)

    return dp[len1][len2]
def find_closest_match(input_word, vocab):
    min_distance = float('inf')
    closest_word = None

    for word in vocab:
        distance = damerau_levenshtein_distance(input_word, word)
        if distance < min_distance:
            min_distance = distance
            closest_word = word
             
    return closest_word, min_distance