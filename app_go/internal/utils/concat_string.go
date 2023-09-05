package utils

import (
	"bytes"
)

// ConcatString function that constructs multiple string in the most effective way
func ConcatString(strs ...string) string {
	buf := bytes.NewBufferString("")
	for _, el := range strs {
		buf.WriteString(el)
	}
	return buf.String()
}
