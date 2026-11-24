package main

import ("fmt"
"os"
"strings")

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Wrong input")
		return
	}
	text:= os.Args[1]
	fmt.Print(printASCII(text))
}

func printASCII(text string) string {
	textfile, err := os.ReadFile("standard.txt")
	if err != nil {
		fmt.Println("Sope mio ri file yen", err)
		return " "
	}
	content:= strings.ReplaceAll(string(textfile), "\r\n", "\n")
	textfile_line:= strings.Split(content, "\n")

	text = strings.ReplaceAll((text), "\\n", "\n")
	if text == " " {
		return " "
	}
	if strings.Trim(text, "\n") == " " {
		return  text
	}
	words:= strings.Split(text, "\n")
	result:= " "
	for _, line := range words {
		if line == " " {
			if len(words) > 1 {
				result += "\n"
			}
			continue
		}
		for i := 0; i < 8; i++ {
			for _, char := range line {
				if char >= ' ' && char <= '~' {
					result += textfile_line[int(char-' ')*9+1+i]
				}
			}
			result += "\n"
		}
	}
	return result
}