package checkpoint

func CamelToSnakeCase(s string) string {
	output := []byte{}
	for i := 0; i < len(s); i++ {
		isUpper := s[i] >= 'A' && s[i] <= 'Z'
		isLower := s[i] >= 'a' && s[i] <= 'z'

		if !isUpper && !isLower {
			return s
		}
		if isUpper {
			if i == len(s)-1 {
				return s
			}
			if i > 0 {
				prv := s[i-1] >= 'A' && s[i-1] <= 'Z'
				if prv {
					return s
				}
			}
			if i > 0 {
				output = append(output, '_')
			}
		}
		output = append(output, s[i])
	}
	return string(output)
}
