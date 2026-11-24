package main

import ("fmt")

func main() {
	for i:=0; i <= 50; i+=2 {
		if i == 34 || i == 40 {
			continue
		}
		if i == 42 || i == 44 {
			break
		}
		fmt.Println(i)
	}
}