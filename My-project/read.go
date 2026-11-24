package main

import (
	"fmt"
	"os"
)

func main() {
	content, err := os.ReadFile("input.txt")
	if err != nil {
		fmt.Println("File not found")
		return
	}
	fmt.Println(string(content))
}