package main

import (
	"fmt"
)

func main() {
	sl1 := []int{67, 45, 12, 98, 76, 54, 87, 88, 11, 4, 5, 7}
	sl1 = insertionSort(sl1)
	fmt.Println(sl1)
}
func insertionSort(lst []int) []int {
	for in, el := range lst[1:] {
		tempVal := el
		ipos := in
		for ipos >= 0 && lst[ipos] > tempVal {
			lst[ipos+1] = lst[ipos]
			ipos--
		}
		lst[ipos+1] = tempVal
	}
	return lst
}
