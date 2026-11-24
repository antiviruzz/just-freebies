package checkpoint

func cAlphabet(str string) bool {
	for _, char := range str {
		if (char < 'a' || char > 'z') && (char < 'A' || char > 'Z') {
			return false
		}
	}
	return true
}

func isUpper(s rune) bool {
	return s>= 'A' && s<= 'Z'
}

func camelToSnake(s string) string {
	result:= " "
	if len(s) == 0 && !cAlphabet(s) {
		return s
	}
	for i := 0; i < len(s); i++ {
		if i != 0 && isUpper(rune(s[i])) && i+1 <len(s) && !isUpper(rune(s[i+1])) {
			result+= "_"
			result+= string(s[i])
		} esle if !isUpper(rune(s[i])) || (i == 0 && isUpper(rune(s[i]))) {
			result+= string(s[i])
		} else {
			return s
		}
	}
	return result
}