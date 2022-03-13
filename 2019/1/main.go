package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	solve("a")
	solve("b")
}

func computeFuel(mass int) int {
	return mass/3 - 2
}

func computeFuelRecursively(mass int) int {
	var subTotalFuel int
	for mass > 8 {
		mass = computeFuel(mass)
		subTotalFuel += mass
	}
	return subTotalFuel
}

func solve(part string) {
	f, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
		return
	}
	defer f.Close()
	scanner := bufio.NewScanner(f)
	var totalFuel int
	for scanner.Scan() {
		mass, _ := strconv.Atoi(scanner.Text())
		if part == "a" {
			totalFuel += computeFuel(mass)
		} else if part == "b" {
			totalFuel += computeFuelRecursively(mass)
		}
	}
	fmt.Println(totalFuel)
}
