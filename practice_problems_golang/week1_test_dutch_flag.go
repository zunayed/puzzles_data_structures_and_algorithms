package main

func dutchFlagSort(balls []string) {
	if len(balls) <= 1 {
		return
	}

	/*
		Maintain 4 regions
		0 -  r1 -> R values
		r1 - r2 -> G values
		r2 - r3 -> unsorted part of array
		r3 - end -> B values
	*/
	r1, r2, r3 := 0, 0, len(balls)-1

	for r2 <= r3 {
		//swap into X region and increment
		if balls[r2] == "R" {
			// swap
			balls[r2], balls[r1] = balls[r1], balls[r2]
			r1++
			r2++
		} else if balls[r2] == "G" {
			r2++
		} else if balls[r2] == "B" {
			// swap
			balls[r2], balls[r3] = balls[r3], balls[r2]
			r3--
		}
	}
}
