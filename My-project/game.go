package main

import ("fmt")

func main() {
	var choice string
	var fstCh string
	var secCh string
	fmt.Println("left or right?")
	fmt.Scan(&choice)
	if choice == "right" {
		fmt.Println("Fall into a hole. Game Over.")
	} else if choice == "left" {
		fmt.Println("swim or wait?")
		fmt.Scan(&fstCh)
		if fstCh == "swim" {
			fmt.Println("Attacked by trout. Game Over.")
		} else if fstCh == "wait" {
			fmt.Println("Which door? red, blue, or yellow?")
			fmt.Scan(&secCh)
			if secCh == "red" {
				fmt.Println("Burned by fire. Game Over.")
			} else if secCh == "blue" {
				fmt.Println("Eaten by beasts. Game Over.")
			} else if secCh == "yellow" {
				fmt.Println("You found the treasure! You Win!")
			} else {
				fmt.Println("Game Over.")
			}
		} else {
			fmt.Println("Try again")
		}
	} else {
		fmt.Println("Game fucking over!")
	}
}
