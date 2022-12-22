use std::io::{self, stdin, Write};

fn main() {
    //let _board = Vec::<Vec<&str>>::new();
    let mut tb = Table::new();
    println!("{}", tb.pretty_print());
    let game = Game::new();
}

pub struct Table {
    table: &Vec<Vec<&str>>,
}

impl Table {
    pub fn new() -> Table {
        Table {
            table: vec![vec!(" "; 3); 3],
        }
    }

    pub fn reset(&mut self) -> () {
        /* Reset the 3x3 gameboard */
        self.table = vec![vec!(" "; 3); 3];
    }

    pub fn pretty_print(self) -> String {
        /* Return the gameboard with pretty output */
        let mut board = "".to_owned();
        let line: &str = "+---+---+---+";

        for y in self.table {
            board += &(line.to_owned() + "\n");
            for x in y {
                board += &("| ".to_owned() + x + " ");
            }
            board += &("|\n");
        }
        board += &(line.to_owned() + "\n");
        board
    }
}

struct Game {
    finished: bool,
    turn: u8,
    players: Players,
}

#[derive(Debug)]
struct Players {
    p_1: char,
    p_2: char,
}

impl Game {
    pub fn new() -> Game {
        Game {
            finished: false,
            turn: 1,
            players: Players { p_1: 'x', p_2: 'o' },
        }
    }

    pub fn game_loop(&self) -> () {
        loop {
            if self.finished {
                break;
            }
        }
    }

    pub fn _check_win(&mut self) -> () {
        self.finished = false; // TODO: Implement Win condition
    }

    pub fn get_coordinates(self) -> (u8, u8) {
        /* Get coordinates from the input */
        let mut x = String::new();
        let mut y = String::new();

        print!("Enter the value of x: ");
        io::stdout().flush().unwrap();
        stdin().read_line(&mut x).unwrap();

        print!("Enter the value of y: ");
        io::stdout().flush().unwrap();
        stdin().read_line(&mut y).unwrap();

        (
            x.trim().parse::<u8>().unwrap(),
            y.trim().parse::<u8>().unwrap(),
        )
    }
}
