package main

import ("fmt"
"strings"
)

func main() {
	text:= "!!!Hello!!!"
	output:= strings.Trim(text, "!")
	fmt.Println(output)  
}