#![allow(non_snake_case)]  // Disable non_snake_case warnings for the entire file

use std::fs;
use std::time::Instant;

const TEST: &str = "3   4
4   3
2   5
1   3
3   9
3   3";

fn main() {
    let input = fs::read_to_string("../input.txt").expect("Something went wrong reading the file");
    assert_eq!(part_one(TEST), 11);
    println!("Part 1: {}", part_one(&input));
    assert_eq!(part_two(TEST), 31);
    println!("Part 1: {}", part_two(&input));
}

fn part_one(data: &str) -> u32 {
    let start = Instant::now();

    let lines = data.lines();
    let mut sx: Vec<i32> = vec![];
    let mut dx: Vec<i32> = vec![];
    for line in lines {
        let nums: Vec<i32> = line.split("   ").filter_map(|x| x.parse().ok()).collect();
        sx.push(nums[0]);
        dx.push(nums[1]);
    }

    sx.sort();
    dx.sort();

    let mut res = 0;

    for (s, d) in sx.iter().zip(dx.iter()){
        res += (s-d).abs();
    }
    
    
    let duration = start.elapsed();
    println!("Time taken: {:?}", duration);
    
    return res.try_into().unwrap();

}


fn part_two(data: &str) -> u32 {
    let start = Instant::now();
    
    let lines = data.lines();
    let mut sx: Vec<i32> = vec![];
    let mut dx: Vec<i32> = vec![];
    for line in lines {
        let nums: Vec<i32> = line.split("   ").filter_map(|x| x.parse().ok()).collect();
        sx.push(nums[0]);
        dx.push(nums[1]);
    }

    sx.sort();
    dx.sort();

    let mut res = 0;

    for s in sx{
        res += s* (dx.iter().filter(|x| **x == s)).count() as i32;
    }

    let duration = start.elapsed();
    println!("Time taken: {:?}", duration);
    
    return res.try_into().unwrap();
}
