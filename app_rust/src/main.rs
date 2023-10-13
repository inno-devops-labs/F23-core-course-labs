use std::process;
use web_server::{run, Webserver};

fn main() {
    let web_server = Webserver::build(String::from("127.0.0.1"), String::from("8080"))
        .unwrap_or_else(|err| {
            eprintln!("Problem parsing the ip: {err}");
            process::exit(1);
        });

    if let Err(e) = run(web_server) {
        eprintln!("Error while running the application: {e}");
        process::exit(1);
    }
}
