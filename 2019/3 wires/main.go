package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func main() {
	input := getInput("input")
	output := run(input)
	fmt.Println(output)
}

func run(input []string) int {
	path1, path2 := recordPath(input[0]), recordPath(input[1])
	intersections := resolveIntersections(path1, path2)
	smallestDistance := computeSmallestDistance(intersections)
	return smallestDistance
}

// takes "U1,R3,D2,....'
// returns [[0,1], [1,1],[2,1],[3,1], [3,0],[3,-1], ...]
func recordPath(stepString string) [][]int {
	var path = [][]int{{0, 0}} // {x,y}
	steps := strings.Split(stepString, ",")
	for _, s := range steps {
		direction := string(s[0])
		magnitude, _ := strconv.Atoi(s[1:])
		for i := 1; i <= magnitude; i++ {
			switch direction {
			case "R":
				nextStep := []int{path[len(path)-1][0] + 1, path[len(path)-1][1]}
				path = append(path, nextStep)
			case "D":
				nextStep := []int{path[len(path)-1][0], path[len(path)-1][1] - 1}
				path = append(path, nextStep)
			case "L":
				nextStep := []int{path[len(path)-1][0] - 1, path[len(path)-1][1]}
				path = append(path, nextStep)
			case "U":
				nextStep := []int{path[len(path)-1][0], path[len(path)-1][1] + 1}
				path = append(path, nextStep)
			}
		}
	}
	return path[1:]
}

// takes
//	- [[0,1], [1,1],[2,1]*,[3,1], [3,0]*,[3,-1], ...]
//	- [[1,0],[2,0],[3,0]*, [3,1],[3,2], [2,2], [2,1]*,[2,0], ...]
// returns [[3,0],[2,1],...]
func resolveIntersections(path1, path2 [][]int) [][]int {
	var intersections [][]int
	for _, step1 := range path1 {
		for _, step2 := range path2 {
			if step1[0] == step2[0] && step1[1] == step2[1] {
				intersections = append(intersections, step1)
			}
		}
	}
	return intersections
}

// takes [[3,2],[5,5],[9,-4],...]
// returns 5
func computeSmallestDistance(intersections [][]int) int {
	var distances []int
	for _, intersection := range intersections {
		distance := 0
		for _, d := range intersection {
			distance += int(math.Abs(float64(d)))
		}
		distances = append(distances, distance)
	}
	smallestDistance := distances[0]
	for _, distance := range distances {
		if distance < smallestDistance {
			smallestDistance = distance
		}
	}
	return smallestDistance
}

// takes "input"
// returns ["U1,D2,...", "R1,L3,..."]
func getInput(fileName string) []string {
	data, _ := os.ReadFile(fileName)
	dataString := string(data)
	wiresString := strings.Split(dataString, "\n")
	return wiresString
}
