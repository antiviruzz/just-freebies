package main

import (
	"fmt"
	"strings"
)

func capitalize(word string) string {

	if len(word) == 0 {
		return word
	}

	first := strings.ToUpper(string(word[0]))
	rest := strings.ToLower(word[1:])

	return first + rest
}

func main() {

	text := "welcome (up) to (up) the Brooklyn bridge (cap) but then, WE (low) are not DOOM (low) in the end (cap)"

	words := strings.Fields(text)

	for i := 0; i < len(words); i++ {

		if words[i] == "(up)" && i > 0 {
			words[i-1] = strings.ToUpper(words[i-1])
		}

		if words[i] == "(low)" && i > 0 {
			words[i-1] = strings.ToLower(words[i-1])
		}

		if words[i] == "(cap)" && i > 0 {
			words[i-1] = capitalize(words[i-1])
		}

	}

	fmt.Println(words)

}