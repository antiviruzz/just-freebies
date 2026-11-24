package main

import "fmt"

func main() {
	boys:= [3]string{"Taiwo", "Olu", "Ola"}
	girls:= [3]string{"Kenny", "Bolu", "Bola"}

	for i:= 0; i < len(boys); i++ {
		for j:= 0; j < len(girls); j++ {
			fmt.Println(boys[i], girls[j])
		}
	}
}