use std::fs::read_to_string;

fn main() {
    let data = read_to_string("input.txt").unwrap();
    let contents: Vec<&str> = data.split('\n').collect();

    let mut calories: Vec<i32> = Vec::new();
    let mut current = 0;

    for line in contents {
        if line == "" {
            calories.push(current);
            current = 0;
        } else {
            current += line.parse::<i32>().unwrap();
        }
    }

    calories.sort_by(|a, b| b.cmp(a));
    let top3: i32 = calories.iter().take(3).sum();

    println!("{}", top3);
}
