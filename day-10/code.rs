use std::io;

fn main() {
    let mut m = String::new();
    io::stdin().read_line(&mut m).expect("Failed to read input");
    let m: i32 = m.trim().parse().expect("Please enter a valid integer");
    let mut count = 0;

    for a in 2..m - 3 {
        for b in 2..m - 3 {
            for c in 2..m - 3 {
                for d in 2..m - 3 {
                    for e in 2..m - 3 {
                        count += (a + b + c + d + e == m) as i32
                    }
                }
            }
        }
    }

    println!("{}", count);
}
