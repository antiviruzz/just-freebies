package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	text := "The number 1011 (bin) and FF (hex) will not yield 100. 111 (bin) is also not 1E (hex)."
	words := strings.Fields(text)

	for i := 0; i < len(words); i++ {
		if words[i] == "(bin)" && i > 0 {
			num, err := strconv.ParseInt(words[i-1], 2, 64)
			if err == nil {
				words[i-1] = strconv.FormatInt(num, 10)
			}
		}
		if words[i] == "(hex)" && i > 0 {
			num, err := strconv.ParseInt(words[i-1], 16, 64)
			if err == nil {
				words[i-1] = strconv.FormatInt(num, 10)
			}
		}
	}

	var finalWords []string
	for _, w := range words {
		if w != "(bin)" && w != "(hex)" {
			finalWords = append(finalWords, w)
		}
	}

	finalText := strings.Join(finalWords, " ")
	fmt.Println(finalText)
}