use std::fs::read_to_string;

fn main() {
    let data = read_to_string("input.txt").unwrap();
    let contents: Vec<&str> = data.split('\n').collect();

    let mut score = 0;

    for i in (0..contents.len()).step_by(3) {
        let elf1 = contents[i];
        let elf2 = contents[i + 1];
        let elf3 = contents[i + 2];

        for c in elf1.chars() {
            if elf2.contains(c) && elf3.contains(c) {
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
