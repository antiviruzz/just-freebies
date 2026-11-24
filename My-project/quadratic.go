package main

import (
	"fmt"
	"math"
)

func main() {
	var a, b, c float64
	fmt.Println("Enter a:")
	_, err := fmt.Scan(&a)
	if err != nil {
		fmt.Println("Invalid Input!")
		return
	}
	if a == 0 {
		fmt.Println("A cannot be zero. This is quadratic equation!")
		return
	}
	fmt.Println("Enter b:")
	_, err = fmt.Scan(&b)
	if err != nil {
		fmt.Println("Invalid input!")
		return
	}

	fmt.Println("Enter c:")
	_, err = fmt.Scan(&c)
	if err != nil {
		fmt.Println("Invalid input!")
		return
	}

	det := b*b - 4*a*c
	if det < 0 {
		fmt.Println("Potential output error!")
	} else {
		root1 := (-b + math.Sqrt(det)) / (2 * a)
		root2 := (-b - math.Sqrt(det)) / (2 * a)

		fmt.Printf("%.2f\n", root1)
		fmt.Printf("%.2f\n", root2)
	}
}
