use std::fs::read_to_string;

fn main() {
    let data = read_to_string("input.txt").unwrap();
    let contents: Vec<&str> = data.split('\n').collect();

    let mut overlaps = 0;

    for line in contents {
        let elf_data: Vec<&str> = line //
            .split(',')
            .collect();

        let elf1: Vec<i32> = elf_data[0] //
            .split('-')
            .map(|x| x.parse().unwrap())
            .collect();
        let elf2: Vec<i32> = elf_data[1] //
            .split('-')
            .map(|x| x.parse().unwrap())
            .collect();

        if elf1[0] >= elf2[0] && elf1[1] <= elf2[1] {
            overlaps += 1;
        } else if elf1[0] <= elf2[0] && elf1[1] >= elf2[1] {
            overlaps += 1;
        }
    }

    println!("{}", overlaps);
}
