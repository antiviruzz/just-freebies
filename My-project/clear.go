package main

import (
	"fmt"
	"strings"
)

func main() {

	text := "this (cap) is a test (up) hello WORLD (low) welcome (cap) to go (up) and we are BEAST (low)"

	words := strings.Fields(text)

	var result []string

	for i := 0; i < len(words); i++ {

		if words[i] == "(up)" {
			result[len(result)-1] = strings.ToUpper(result[len(result)-1])
			continue
		}

		if words[i] == "(low)" {
			result[len(result)-1] = strings.ToLower(result[len(result)-1])
			continue
		}

		if words[i] == "(cap)" {
			word := result[len(result)-1]
			result[len(result)-1] =
				strings.ToUpper(string(word[0])) + strings.ToLower(word[1:])
			continue
		}

		result = append(result, words[i])
	}

	fmt.Println(strings.Join(result, " "))
}