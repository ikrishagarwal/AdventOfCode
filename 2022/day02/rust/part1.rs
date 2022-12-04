use std::{collections::HashMap, fs::read_to_string};

fn main() {
    let data = read_to_string("input.txt").unwrap();
    let contents: Vec<&str> = data.split('\n').collect();

    let mut score = 0;

    let mut score_board = HashMap::new();

    score_board.insert('A', ScoreBoard { x: 4, y: 8, z: 3 });

    score_board.insert('B', ScoreBoard { x: 1, y: 5, z: 9 });

    score_board.insert('C', ScoreBoard { x: 7, y: 2, z: 6 });

    for line in contents {
        let moves: Vec<char> = line //
            .split(' ')
            .map(|a| a.chars().nth(0).unwrap())
            .collect();

        score += score_board.get(&moves[0]).unwrap().get(&moves[1]);
    }

    println!("{}", score);
}

struct ScoreBoard {
    x: i32,
    y: i32,
    z: i32,
}

impl ScoreBoard {
    fn get(&self, key: &char) -> i32 {
        match key {
            'X' => self.x,
            'Y' => self.y,
            'Z' => self.z,
            _ => 0,
        }
    }
}
