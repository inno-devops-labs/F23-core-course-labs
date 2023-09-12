#[macro_use]
extern crate rocket;
use chrono::{DateTime, FixedOffset, Local};
use clap::Parser;
use rocket::Config;

#[get("/")]
fn time() -> String {
    let msk_timezone = FixedOffset::east_opt(3 * 3600).unwrap();
    let utc_now = Local::now().naive_utc();
    DateTime::<Local>::from_naive_utc_and_offset(utc_now, msk_timezone).to_rfc3339()
}

#[get("/health")]
fn healthcheck() -> &'static str {
    return "OK"
}

#[derive(Parser, Debug)]
#[command(author, version, about, long_about = None)]
struct Args {
    #[arg(default_value = "0.0.0.0")]
    host: String,
    #[arg(default_value_t = 8000)]
    port: u16,
}

#[launch]
fn rocket() -> _ {
    let args = Args::parse();
    let config = Config{
        address: args.host.parse().unwrap(),
        port: args.port,
        ..Default::default()
    };

    rocket::build().configure(config).mount("/", routes![time, healthcheck])
}
