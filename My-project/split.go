package main

import ("fmt"
"strings")

func main() {
text:= ("Apple,Ball,Cat,Dog")
output:= strings.Split(text, ",")
fmt.Println(output[0])
fmt.Println(output[1])
fmt.Println(output[3])
}