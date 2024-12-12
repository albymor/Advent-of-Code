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
    assert_eq!(part_one(TEST), 0);
    let input = fs::read_to_string("../input.txt").expect("Something went wrong reading the file");
    println!("Part 1: {}", part_one(&input));
    assert_eq!(part_two(TEST), 0);
    println!("Part 1: {}", part_two(&input));
}

fn part_one(data: &str) -> u32 {
    let start = Instant::now();

    let mut res = 0;
    
    let duration = start.elapsed();
    println!("Time taken: {:?}", duration);
    
    return res.try_into().unwrap();

}


fn part_two(data: &str) -> u32 {
    let start = Instant::now();
    
    let mut res = 0;

    let duration = start.elapsed();
    println!("Time taken: {:?}", duration);
    
    return res.try_into().unwrap();
}
