use std::fs::read_to_string;

fn main() {
    let data = read_to_string("input.txt").unwrap();
    let contents: Vec<&str> = data.split('\n').collect();

    let mut score = 0;

    for line in contents {
        let part1 = &line[..(line.len() / 2)];
        let part2 = &line[(line.len() / 2)..];

        for c in part1.chars() {
            if part2.contains(c) {
                score += get_points(c);
                break;
            }
        }
    }

    println!("{}", score);
}

fn get_points(letter: char) -> i32 {
    let point = letter as i32;
    if point < 91 {
        return point - 64 + 26;
    }
    return point - 96;
}
