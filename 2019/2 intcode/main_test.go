package main

import (
	"reflect"
	"testing"
)

func Test_run(t *testing.T) {
	type args struct {
		program []int
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
		{
			name: "testOp0",
			args: args{
				program: []int{1, 0, 0, 0, 99},
			},
			want: []int{2, 0, 0, 0, 99},
		},
		{
			name: "testOp1",
			args: args{
				program: []int{2, 3, 0, 3, 99},
			},
			want: []int{2, 3, 0, 6, 99},
		},
		{
			name: "testOp2",
			args: args{
				program: []int{2, 4, 4, 5, 99, 0},
			},
			want: []int{2, 4, 4, 5, 99, 9801},
		},
		{
			name: "testOp3",
			args: args{
				program: []int{1, 1, 1, 4, 99, 5, 6, 0, 99},
			},
			want: []int{30, 1, 1, 4, 2, 5, 6, 0, 99},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := run(tt.args.program); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("run() = %v, want %v", got, tt.want)
			}
		})
	}
}
