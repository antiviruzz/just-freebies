package main

import (
	"fmt"
	"os"
	//"strings"
)

func main() {
	if len(os.Args) != 2 {

	fmt.Println("Follow the rule!")
	os.Exit(1)
	return 
	
	}
	content:= os.Args[1]
	file, err := os.ReadFile(content)
	if err != nil {
		os.Exit(1)
	}
	newFile:= string(file)
	
	wordSliced := strings.Fields(newFile)
	for i:= 0, i < len(wordSliced); i++ {
		switch wordSliced[i] {
		case "(cap)" :
			fmt.Println("am cap at index ", i)
		}
	}
}