package timeutils

import (
	"fmt"
	"testing"
	"time"
)

func panicIf(t *testing.T, err error) {
	if err != nil {
		t.Fatal(err.Error())
	}
}

type equalDefined interface {
	float64 | float32 | int | uint | string
}

func assertEq[T equalDefined](t *testing.T, a T, b T) {
	if a != b {
		t.Fatalf("FAIL: expected %v == %v", a, b)
	}
}

func TestTime(t *testing.T) {
	loc, err := time.LoadLocation("Europe/Moscow")
	panicIf(t, err)
	dt := time.Now().In(loc).Format("15:04:05")
	fmt.Println("our time:" + dt)
	assertEq(t, dt, GetTime())
}
