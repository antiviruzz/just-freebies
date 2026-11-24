package main

import ("fmt"
		"strings"
	)

func cap(word string) string {
	if len(word) == 0 {
		return word
	}
	return strings.ToUpper(string(word[0])) + strings.ToLower(word[1:])
}

func main() {
	text:= "taiwo"
	fmt.Println(cap(text))
}