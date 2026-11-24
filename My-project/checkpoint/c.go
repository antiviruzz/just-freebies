package checkpoint

func CamelToSnakeCase(s string)string {
result:= []byte{}
for i:= 0; i < len(s); i++ {
	isUpper:= s[i] >= 'A' && s[i] <= 'Z'
	isLower:= s[i] >= 'a' && s[i] <= 'z'
	if !isUpper && !isLower {
		return s
	}
	if isUpper {
		if i== len(s)-1 {
			return s
		}
		if i > 0 {
		pvsIsUpper:= s[i-1] >= 'A' && s[i-1] <= 'Z'
		if pvsIsUpper{
			return s
		}
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

func CamelToSnakeCase(s string)string{
	result:= []byte{}
	for i:= 0; i < len(s); i++ {
		isUpper:= s[i] >= 'A' && s[i] <= 'Z'
		isLower:= s[i] >= 'a' && s[i] <= 'z'

		if !isUpper && !isLower {
			return s
		}
		if isUpper {
			if i == len(s) - 1 {
				return s
			}
			if i > 0 {
				pvsUpper:= s[i-1] >= 'A' && s[i-1] <= 'Z'
				if pvsUpper {
					return s
				}
			}
			if i > 0 {
			result = append(result, '_')
		}
		}
		result = append(result, s[i])
	}
	return string(result)
}