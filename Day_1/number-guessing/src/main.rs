extern crate rand;
use rand::Rng;
use std::io::stdin;
use std::io::{self, Write};

fn main() {
    let mut attempts = 3;
    let win = randrange(1, 10); // The winner number

    loop {
        match attempts {
            0 => {
                println!("You lost, the correct answer was : {}", win);
                break;
            }
            x => {
                ask_number(x);
            }
        }

        let mut input = String::new();

        stdin().read_line(&mut input).unwrap();

        let input = match input.trim().parse::<u8>() {
            Ok(f) => f,
            Err(_e) => {
                println!("You entered invalid number !");
                continue;
            }
        };

        if input > win {
            println!("You number is too big :(\n");
            attempts -= 1;
        } else if input < win {
            println!("Your number is too small\n");
            attempts -= 1;
        } else {
            println!("\nCongratulations !! {} is the right number", win);
            break;
        }
    }
}

fn randrange(start: u8, end: u8) -> u8 {
    /* Generate random number between start and end */
    rand::thread_rng().gen_range(start..=end)
}

fn ask_number(attempts: i32) -> () {
    print!(
        "Guess the number between 1 and 10 ({} attempts remain) : ",
        attempts
    );
    io::stdout().flush().unwrap();
}
