use std::fs;

fn main() {
    let input = fs::read_to_string("../../input.txt").expect("Something went wrong reading the file");
    println!("Part 1: {}", part_one(&input));
    println!("Part 1: {}", part_two(&input));
}

fn part_one(data: &str) -> u32 {

    let mut elfs: Vec<u32> = Vec::new();

    let mut sum = 0;

    for line  in data.lines() {
        if line.is_empty() {
            elfs.push(sum);
            sum = 0;
        }
        else {
            sum += line.parse::<u32>().unwrap();
        }
    }
    elfs.push(sum);

    elfs.iter().max().unwrap().clone()
}


fn part_two(data: &str) -> u32 {

    let mut elfs: Vec<u32> = Vec::new();

    let mut sum = 0;

    for line  in data.lines() {
        if line.is_empty() {
            elfs.push(sum);
            sum = 0;
        }
        else {
            sum += line.parse::<u32>().unwrap();
        }
    }
    elfs.push(sum);

    //sort elfs
    elfs.sort();
    //take the top 3
    elfs[elfs.len()-3..].iter().sum()
}


#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_part_one() {
        let test = "1000
2000
3000

4000

5000
6000

7000
8000
9000

10000";
        assert_eq!(part_one(test), 24000);
    }

    #[test]
    fn test_part_two() {
        let test = "1000
2000
3000

4000

5000
6000

7000
8000
9000

10000";
        assert_eq!(part_two(test), 45000);
    }
}
