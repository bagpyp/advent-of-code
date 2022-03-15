package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	for noun := 0; noun < 100; noun++ {
		for verb := 0; verb < 100; verb++ {
			program := getInput("input")
			program[1], program[2] = noun, verb
			programOutput := run(program)[0]
			if noun == 12 && verb == 2 {
				fmt.Println("a: ", programOutput)
			} else if programOutput == 19690720 {
				fmt.Println("b: ", noun * 100 + verb)
			}
		}
	}
}

func run(program []int) []int {
	i := 0
	for i < len(program) {
		if program[i] == 99 {
			return program
		}
		program = op(program, i)
		i += 4
	}
	return program
}

func op(program []int, pointer int) []int {
	opCode := program[pointer]
	p1 := program[program[pointer+1]]
	p2 := program[program[pointer+2]]
	outputAddress := program[pointer+3]
	var output int
	if opCode == 1 {
		output = p1 + p2 
	} else {
		output = p1 * p2
	}
	program[outputAddress] = output
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
