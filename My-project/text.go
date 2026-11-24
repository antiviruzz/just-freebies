package main

import ("fmt"
"strings"
)

func main() {
	text:= "Ready to GO (low) and smash It (low) THROUGHOUT (low)"
	words:= strings.Fields(text)
	for i:= 0; i < len(words); i++ {
		if words [i] == "(low)" && i>0 {
			words [i-1] = strings.ToLower(words[i-1])
		}
	}
	fmt.Println(words)
}