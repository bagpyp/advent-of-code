package main

import (
	"testing"
)

func Test_computeFuel(t *testing.T) {
	type args struct {
		mass int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "simple",
			args: args{
				mass: 1969,
			},
			want: 654,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := computeFuel(tt.args.mass); got != tt.want {
				t.Errorf("computeFuel() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_computeFuelRecursively(t *testing.T) {
	type args struct {
		mass int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "simple",
			args: args{
				mass: 1969,
			},
			want: 966,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := computeFuelRecursively(tt.args.mass); got != tt.want {
				t.Errorf("computeFuelRecursively() = %v, want %v", got, tt.want)
			}
		})
	}
}
