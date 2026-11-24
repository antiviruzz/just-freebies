package main

import ("fmt")

type individual struct {
	name	string
	age		int
	job		string
	salary	float64
}

func main() {
	var mem1 individual
	var mem2 individual

	mem1.name = 	"Unique"
	mem1.age = 		25
	mem1.job = 		"AI Engineer"
	mem1.salary = 	50000.45

	mem2.name = 	"Akanho"
	mem2.age = 		24
	mem2.job = 		"Prompt Engineer"
	mem2.salary = 	45000.50

	fmt.Println("Name:", 	mem1.name)
	fmt.Println("Age: ", 	mem1.age)
	fmt.Println("Job: ", 	mem1.job)
	fmt.Println("Salary: ", mem1.salary)

	fmt.Println("Name:", 	mem2.name)
	fmt.Println("Age: ", 	mem2.age)
	fmt.Println("Job: ", 	mem2.job)
	fmt.Println("Salary: ", mem2.salary)
}