#[macro_use]
extern crate rocket;
use chrono::{DateTime, FixedOffset, Local};
use clap::Parser;
use rocket::Config;
use prometheus::gather;


pub fn current_time() -> DateTime<Local>  {
    let msk_timezone = FixedOffset::east_opt(3 * 3600).unwrap();
    let utc_now = Local::now().naive_utc();
    DateTime::<Local>::from_naive_utc_and_offset(utc_now, msk_timezone)
}

#[get("/")]
fn time() -> String {
    current_time().to_rfc3339()
}

#[get("/health")]
fn healthcheck() -> &'static str {
    "OK"
}

#[get("/metrics")]
fn metrics() -> String {
    let encoder = prometheus::TextEncoder::new();

    match encoder.encode_to_string(&gather()) {
        Ok(data) => {
            data
        },
        Err(e) => {
            e.to_string()
        }
    }
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

    rocket::build().configure(config).mount("/", routes![time, healthcheck, metrics])
}


#[cfg(test)]
mod tests {
    use super::{current_time, rocket};

    use chrono::{Duration, DateTime};
    use rocket::local::blocking::Client;

    #[test]
    fn test_current_time() {
        let dt1 = current_time();
        let dt2 = current_time();
        assert!(dt2 - dt1 < Duration::seconds(10))
    }

    #[test]
    fn test_endpoint() {
        let client = Client::tracked(rocket()).unwrap();
        let resp1 = client.get("/").dispatch();
        let resp2 = client.get("/").dispatch();

        let dt1 = resp1.into_string().unwrap();
        let dt2 = resp2.into_string().unwrap();

        let dt1 = DateTime::parse_from_rfc3339(&dt1).unwrap();
        let dt2 = DateTime::parse_from_rfc3339(&dt2).unwrap();

        assert!(dt2 - dt1 < Duration::seconds(10))
    }
}
