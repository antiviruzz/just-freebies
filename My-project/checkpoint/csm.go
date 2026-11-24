package main

import ("fmt")

func camelToSnake(s string)string{
	result:= []byte{}
	for i:= 0; i < len(s); i++ {
		if s[i] < 'A' || (s[i]>'Z' && s[i] < 'a') || s[i] > 'z'{
			return s
		}
		if s[i] >= 'A' && s[i] <= 'Z' {
			if i == len(s)-1 || (i > 0 && s[i-1] >= 'A' && s[i-1] <= 'Z'){
				return s
			}
			if i > 0 {
				result = append(result, '_')
			}
		}
		result = append(result, s[i]) 
	}
	return string(result)
}


package main

func CamelToSnakeCase(s string) string {

	result := []byte{}

	for i := 0; i < len(s); i++ {

		// check if character is a letter
		isUpper := s[i] >= 'A' && s[i] <= 'Z'
		isLower := s[i] >= 'a' && s[i] <= 'z'

		if !isUpper && !isLower {
			return s
		}


		// handle uppercase letters
		if isUpper {

			// cannot end with uppercase
			if i == len(s)-1 {
				return s
			}

			// cannot have two capitals together
			if i > 0 {
				previousIsUpper := s[i-1] >= 'A' && s[i-1] <= 'Z'

				if previousIsUpper {
					return s
				}
			}


			// add underscore before capital letter
			if i > 0 {
				result = append(result, '_')
			}
		}


		result = append(result, s[i])
	}


	return string(result)
}