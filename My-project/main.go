package main

import (
	"fmt"
	"strings"
)

func main() {
	text := "hello (up) world (cap) GO (low)"
	result := processText(text)
	fmt.Println(result)
}

func processText(text string) string {
	words := strings.Fields(text)

	for i := 0; i < len(words); i++ {
		if words[i] == "(up)" && i > 0 {
			words[i-1] = strings.ToUpper(words[i-1])
			words[i] = ""
		}

		if words[i] == "(low)" && i > 0 {
			words[i-1] = strings.ToLower(words[i-1])
			words[i] = ""
		}

		if words[i] == "(cap)" && i > 0 {
			words[i-1] = strings.Title(words[i-1])
			words[i] = ""
		}
	}

	return strings.Join(words, " ")
}