package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	program := getInput("input")
	program = sabatoge(program)
	res := solve(program)
	fmt.Println(res)
}

func solve(program []int) []int {
	for i := range program {
		if i%4 == 0 {
			if program[i] == 99 {
				return program
			} else {
				program = op(program, i)
			}
		}
	}
	return program
}

func getInput(fileName string) []int {
	var res []int
	data, _ := os.ReadFile(fileName)
	dataString := string(data)
	resultsString := strings.Split(dataString, ",")
	for _, s := range resultsString {
		i, _ := strconv.Atoi(s)
		res = append(res, i)
	}
	return res
}

func op(program []int, pos int) []int {
	var out []int
	for i := range program {
		out = append(out, program[i])
	}

	fmt.Println(out)
	val := computation(program[program[pos+1]], program[program[pos+2]], program[pos])
	out[program[pos+3]] = val

	return out
}

func computation(a, b, computationType int) int {
	if computationType == 1 {
		return a + b
	} else if computationType == 2 {
		return a * b
	} else {
		return 0
	}
}

func sabatoge(array []int) []int {
	array[1] = 12
	array[2] = 2
	return array
}
