#![allow(non_snake_case)] // Disable non_snake_case warnings for the entire file

use std::fs;
use std::time::Instant;

const TEST: &str = "7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9";

fn main() {
    assert_eq!(part_one(TEST), 2);
    let input = fs::read_to_string("../input.txt").expect("Something went wrong reading the file");
    println!("Part 1: {}", part_one(&input));
    assert_eq!(part_two(TEST), 4);
    println!("Part 1: {}", part_two(&input));
}

fn diff(data: &Vec<i32>) -> Vec<i32> {
    let d: Vec<i32> = data.windows(2).map(|w| w[1] - w[0]).collect();
    return d;
}

fn part_one(data: &str) -> u32 {
    let start = Instant::now();
    let mut res = 0;

    let lines = data.lines();
    for line in lines {
        let inter: Vec<&str> = line.split(' ').collect(); // get the vec of str
        let parsed: Vec<i32> = inter.iter().filter_map(|x| x.parse().ok()).collect(); //get the Vec of i32
        let d = diff(&parsed);
        let in_range = d.iter().all(|&x| -3 <= x && x <= -1) || d.iter().all(|&x| 1 <= x && x <= 3);
        if in_range {
            res += 1;
        }
    }

    let duration = start.elapsed();
    println!("Time taken: {:?}", duration);

    return res.try_into().unwrap();
}

fn part_two(data: &str) -> u32 {
    let start = Instant::now();

    let mut res = 0;

    let lines = data.lines();
    for line in lines {
        let inter: Vec<&str> = line.split(' ').collect(); // get the vec of str
        let parsed: Vec<i32> = inter.iter().filter_map(|x| x.parse().ok()).collect(); //get the Vec of i32
        for i in 0..parsed.len() {
            let mut new = Vec::new();
            new.extend_from_slice(&parsed[..i]); // Add elements before index i
            new.extend_from_slice(&parsed[i + 1..]); // Add elements after index i
            let d = diff(&new);
            let in_range =
                d.iter().all(|&x| -3 <= x && x <= -1) || d.iter().all(|&x| 1 <= x && x <= 3);
            if in_range {
                res += 1;
                break;
            }
        }
    }

    let duration = start.elapsed();
    println!("Time taken: {:?}", duration);

    return res.try_into().unwrap();
}
