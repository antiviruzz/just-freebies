package main

import("fmt"
"strings")

func main() {
	text:= "  go,is,awesome  "
	trimmed:= strings.Trim(text, " ")
	split:= strings.Split(trimmed, ",")
	upper:= strings.ToUpper(split[0])
	lower:= strings.ToLower(upper)

	fmt.Println(text)
	fmt.Println(trimmed)
	fmt.Println(split[0])
	fmt.Println(split[1])
	fmt.Println(split[2])
	fmt.Println(upper)
	fmt.Println(lower)
}