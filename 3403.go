package main

func answerString(word string, numFriends int) string {
	if numFriends == 1 {
		return word
	}
	
	largestChar := 'a'
	ans := ""

	for _, c := range(word) {
		if c > largestChar {
			largestChar = c
		}
	}

	n := len(word)

	if numFriends == n {
		return string(largestChar)
	}

	maxLen := n - numFriends + 1

	for i := 0; i < n; i++ {
		if word[i] == byte(largestChar) {
            end := i + maxLen
            if end > n {
                end = n
            }
			
            possible := word[i:end]
            if possible > ans {
                ans = possible
            }
        }
	}
	return ans
}

func main() {
	answerString("aann", 2)
}