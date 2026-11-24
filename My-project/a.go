package main

import("fmt"
"strings"
)

func main() {
	text:= "2bHello2b"
	fmt.Println(strings.Trim(text, "2b"))
	border:= "hjHelooohj"
	fmt.Println(strings.Trim(border, "hj"))
}