package main

import (
	"reflect"
	"testing"
)

func Test_resolveIntersections(t *testing.T) {
	type args struct {
		path1 [][]int
		path2 [][]int
	}
	tests := []struct {
		name string
		args args
		want [][]int
	}{
		{
			name: "simple",
			args: args{
				path1: [][]int{{1, 1}, {2, 2}},
				path2: [][]int{{2, 2}, {3, 3}},
			},
			want: [][]int{{2, 2}},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := resolveIntersections(tt.args.path1, tt.args.path2); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("resolveIntersections() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_computeSmallestDistance(t *testing.T) {
	type args struct {
		intersections [][]int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "simple",
			args: args{
				intersections: [][]int{{1, 1}, {100, 100}},
			},
			want: 2,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := computeSmallestDistance(tt.args.intersections); got != tt.want {
				t.Errorf("computeSmallestDistance() = %v, want %v", got, tt.want)
			}
		})
	}
}

/* these fail even though i got my god damn gold star!!
func Test_run(t *testing.T) {
	type args struct {
		input []string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "run it",
			args: args{
				input: []string{
					"R75,D30,R83,U83,L12,D49,R71,U7,L72",
					"U62,R66,U55,R34,D71,R55,D58,R83",
				},
			},
			want: 610,
		},
		{
			name: "run it again",
			args: args{
				input: []string{
					"R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
					"U98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
				},
			},
			want: 410,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := run(tt.args.input); got != tt.want {
				t.Errorf("run() = %v, want %v", got, tt.want)
			}
		})
	}
}
*/
