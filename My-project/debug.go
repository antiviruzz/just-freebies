package main

import "fmt"

func main() {
    accountName := "Ahmed Ridwan Taiye"
    accountNumber := 3109046588
    balance := 673457125.32542

    fmt.Println("============================")
    fmt.Println("       BANK STATEMENT       ")
    fmt.Println("============================")
    fmt.Printf("Account:    %s\n", accountName)
    fmt.Printf("Number:     %d\n", accountNumber)
    fmt.Printf("Balance:    $%.2f\n", balance)
    fmt.Println("============================")
    fmt.Print("Status: GOOD")
    fmt.Println("❤️")
}