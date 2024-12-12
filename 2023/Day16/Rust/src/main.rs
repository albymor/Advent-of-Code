#![allow(non_snake_case)] // Disable non_snake_case warnings for the entire file
extern crate queues;
use queues::*;
use std::collections::HashSet;
use std::fs;
use std::time::Instant;

const TEST: &str = ".|...\\....
|.-.\\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|....";

#[derive(Clone, Hash, Eq, PartialEq, Debug, Copy)]
enum Direction {
    Up,
    Down,
    Left,
    Right,
}
#[derive(Clone, Hash, Eq, PartialEq, Debug, Copy)]
struct Beam {
    x: i32,
    y: i32,
    direction: Direction,
}

pub trait Navigate {
    fn navigate(&mut self);
}

impl Navigate for Beam {
    fn navigate(&mut self) {
        match self.direction {
            Direction::Down => {
                self.y = self.y + 1;
            }
            Direction::Up => {
                self.y = self.y - 1;
            }
            Direction::Right => {
                //->
                self.x = self.x + 1;
            }
            Direction::Left => {
                // <-
                self.x = self.x - 1;
            }
        }
    }
}

fn main() {
    assert_eq!(part_one(TEST), 46);
    let input = fs::read_to_string("../input.txt").expect("Something went wrong reading the file");
    println!("Part 1: {}", part_one(&input));
    assert_eq!(part_two(TEST), 51);
    println!("Part 1: {}", part_two(&input));
}

fn part_two(data: &str) -> u32 {
    let start = Instant::now();

    let lines = data.lines();
    let map: Vec<Vec<char>> = lines.map(|line| line.chars().collect()).collect();
    let y_max = map.len() as i32;
    let x_mas = map[0].len() as i32;

    let mut results: Vec<u32> = Vec::new();

    let mut starts: Vec<Beam> = Vec::new();

    for i in 0..x_mas - 1 {
        let b = Beam {
            x: i,
            y: 0,
            direction: Direction::Down,
        };
        starts.push(b);
        let b = Beam {
            x: i,
            y: y_max - 1,
            direction: Direction::Up,
        };
        starts.push(b);
    }

    for i in 0..y_max - 1 {
        let b = Beam {
            x: 0,
            y: i,
            direction: Direction::Right,
        };
        starts.push(b);
        let b = Beam {
            x: x_mas - 1,
            y: i,
            direction: Direction::Left,
        };
        starts.push(b);
    }

    for beam in starts {
        let mut q: Queue<Beam> = queue![];
        q.add(beam).unwrap();
        let mut visited: HashSet<Beam> = HashSet::new();
        let mut energized = HashSet::new();

        while q.size() > 0 {
            let mut b = q.remove().unwrap();

            if visited.contains(&b) {
                // already been there, no need to recompute
                continue;
            }

            let x = b.x;
            let y = b.y;
            let direction = b.direction;

            //println!("{} {} {:?}", x, y, direction);

            if x < 0 || x > x_mas - 1 || y < 0 || y > y_max - 1 {
                continue;
            }

            visited.insert(b);
            energized.insert((x, y));

            let c = map[y as usize][x as usize];

            match direction {
                Direction::Down => match c {
                    '.' => {
                        b.navigate();
                        q.add(b).unwrap();
                    }
                    '|' => {
                        b.navigate();
                        q.add(b).unwrap();
                    }
                    '-' => {
                        b.direction = Direction::Left;
                        let mut b1 = b.clone();
                        b.navigate();
                        q.add(b).unwrap();
                        b1.direction = Direction::Right;
                        b1.navigate();
                        q.add(b1).unwrap();
                    }
                    '\\' => {
                        b.direction = Direction::Right;
                        b.navigate();
                        q.add(b).unwrap();
                    }
                    '/' => {
                        b.direction = Direction::Left;
                        b.navigate();
                        q.add(b).unwrap();
                    }
                    _ => {
                        panic!("Unknown char")
                    }
                },
                Direction::Up => match c {
                    '.' => {
                        b.navigate();
                        q.add(b).unwrap();
                    }
                    '|' => {
                        b.navigate();
                        q.add(b).unwrap();
                    }
                    '-' => {
                        b.direction = Direction::Left;
                        let mut b1 = b.clone();
                        b.navigate();
                        q.add(b).unwrap();
                        b1.direction = Direction::Right;
                        b1.navigate();
                        q.add(b1).unwrap();
                    }
                    '\\' => {
                        b.direction = Direction::Left;
                        b.navigate();
                        q.add(b).unwrap();
                    }
                    '/' => {
                        b.direction = Direction::Right;
                        b.navigate();
                        q.add(b).unwrap();
                    }
                    _ => {
                        panic!("Unknown char")
                    }
                },
                Direction::Right => {
                    //->
                    match c {
                        '.' => {
                            b.navigate();
                            q.add(b).unwrap();
                        }
                        '|' => {
                            b.direction = Direction::Up;
                            let mut b1 = b.clone();
                            b.navigate();
                            q.add(b).unwrap();
                            b1.direction = Direction::Down;
                            b1.navigate();
                            q.add(b1).unwrap();
                        }
                        '-' => {
                            b.navigate();
                            q.add(b).unwrap();
                        }
                        '\\' => {
                            b.direction = Direction::Down;
                            b.navigate();
                            q.add(b).unwrap();
                        }
                        '/' => {
                            b.direction = Direction::Up;
                            b.navigate();
                            q.add(b).unwrap();
                        }
                        _ => {
                            panic!("Unknown char")
                        }
                    }
                }
                Direction::Left => {
                    // <-
                    match c {
                        '.' => {
                            b.navigate();
                            q.add(b).unwrap();
                        }
                        '|' => {
                            b.direction = Direction::Up;
                            let mut b1 = b.clone();
                            b.navigate();
                            q.add(b).unwrap();
                            b1.direction = Direction::Down;
                            b1.navigate();
                            q.add(b1).unwrap();
                        }
                        '-' => {
                            b.navigate();
                            q.add(b).unwrap();
                        }
                        '\\' => {
                            b.direction = Direction::Up;
                            b.navigate();
                            q.add(b).unwrap();
                        }
                        '/' => {
                            b.direction = Direction::Down;
                            b.navigate();
                            q.add(b).unwrap();
                        }
                        _ => {
                            panic!("Unknown char")
                        }
                    }
                }
            }

            //println!("Queue size {}", q.size());
        }

        results.push(energized.len() as u32);
    }

    let duration = start.elapsed();
    println!("Time taken: {:?}", duration);

    return results.iter().max().unwrap().clone();
}

fn part_one(data: &str) -> u32 {
    let start = Instant::now();

    let lines = data.lines();
    let map: Vec<Vec<char>> = lines.map(|line| line.chars().collect()).collect();
    let y_max = map.len() as i32;
    let x_mas = map[0].len() as i32;

    let mut q: Queue<Beam> = queue![];

    let mut visited: HashSet<Beam> = HashSet::new();
    let mut energized = HashSet::new();

    let beam: Beam = Beam {
        x: 0,
        y: 0,
        direction: Direction::Right,
    };

    q.add(beam).unwrap();

    while q.size() > 0 {
        let mut b = q.remove().unwrap();

        if visited.contains(&b) {
            // already been there, no need to recompute
            continue;
        }

        let x = b.x;
        let y = b.y;
        let direction = b.direction;

        //println!("{} {} {:?}", x, y, direction);

        if x < 0 || x > x_mas - 1 || y < 0 || y > y_max - 1 {
            continue;
        }

        visited.insert(b);
        energized.insert((x, y));

        let c = map[y as usize][x as usize];

        match direction {
            Direction::Down => match c {
                '.' => {
                    b.navigate();
                    q.add(b).unwrap();
                }
                '|' => {
                    b.navigate();
                    q.add(b).unwrap();
                }
                '-' => {
                    b.direction = Direction::Left;
                    let mut b1 = b.clone();
                    b.navigate();
                    q.add(b).unwrap();
                    b1.direction = Direction::Right;
                    b1.navigate();
                    q.add(b1).unwrap();
                }
                '\\' => {
                    b.direction = Direction::Right;
                    b.navigate();
                    q.add(b).unwrap();
                }
                '/' => {
                    b.direction = Direction::Left;
                    b.navigate();
                    q.add(b).unwrap();
                }
                _ => {
                    panic!("Unknown char")
                }
            },
            Direction::Up => match c {
                '.' => {
                    b.navigate();
                    q.add(b).unwrap();
                }
                '|' => {
                    b.navigate();
                    q.add(b).unwrap();
                }
                '-' => {
                    b.direction = Direction::Left;
                    let mut b1 = b.clone();
                    b.navigate();
                    q.add(b).unwrap();
                    b1.direction = Direction::Right;
                    b1.navigate();
                    q.add(b1).unwrap();
                }
                '\\' => {
                    b.direction = Direction::Left;
                    b.navigate();
                    q.add(b).unwrap();
                }
                '/' => {
                    b.direction = Direction::Right;
                    b.navigate();
                    q.add(b).unwrap();
                }
                _ => {
                    panic!("Unknown char")
                }
            },
            Direction::Right => {
                //->
                match c {
                    '.' => {
                        b.navigate();
                        q.add(b).unwrap();
                    }
                    '|' => {
                        b.direction = Direction::Up;
                        let mut b1 = b.clone();
                        b.navigate();
                        q.add(b).unwrap();
                        b1.direction = Direction::Down;
                        b1.navigate();
                        q.add(b1).unwrap();
                    }
                    '-' => {
                        b.navigate();
                        q.add(b).unwrap();
                    }
                    '\\' => {
                        b.direction = Direction::Down;
                        b.navigate();
                        q.add(b).unwrap();
                    }
                    '/' => {
                        b.direction = Direction::Up;
                        b.navigate();
                        q.add(b).unwrap();
                    }
                    _ => {
                        panic!("Unknown char")
                    }
                }
            }
            Direction::Left => {
                // <-
                match c {
                    '.' => {
                        b.navigate();
                        q.add(b).unwrap();
                    }
                    '|' => {
                        b.direction = Direction::Up;
                        let mut b1 = b.clone();
                        b.navigate();
                        q.add(b).unwrap();
                        b1.direction = Direction::Down;
                        b1.navigate();
                        q.add(b1).unwrap();
                    }
                    '-' => {
                        b.navigate();
                        q.add(b).unwrap();
                    }
                    '\\' => {
                        b.direction = Direction::Up;
                        b.navigate();
                        q.add(b).unwrap();
                    }
                    '/' => {
                        b.direction = Direction::Down;
                        b.navigate();
                        q.add(b).unwrap();
                    }
                    _ => {
                        panic!("Unknown char")
                    }
                }
            }
        }

        //println!("Queue size {}", q.size());
    }

    let duration = start.elapsed();
    println!("Time taken: {:?}", duration);

    return energized.len() as u32;
}
