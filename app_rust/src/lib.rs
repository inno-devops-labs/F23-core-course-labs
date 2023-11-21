use regex::Regex;
use std::error::Error;
use std::sync::{mpsc, Arc, Mutex};
use std::thread;
use std::{
    fs,
    io::{prelude::*, BufReader},
    net::TcpListener,
};

use std::panic::{self, AssertUnwindSafe};


use chrono::prelude::*;

pub struct ThreadPool {
    workers: Vec<Worker>,
    sender: Option<mpsc::Sender<Job>>,
}

impl ThreadPool {
    pub fn new(threads_num: usize) -> ThreadPool {
        assert!(threads_num > 0);
        let mut workers = Vec::with_capacity(threads_num);
        let (sender, receiver) = mpsc::channel();

        let rec = Arc::new(Mutex::new(receiver));
        for id in 0..threads_num {
            workers.push(Worker::new(id, Arc::clone(&rec)));
        }
        ThreadPool {
            workers,
            sender: Some(sender),
        }
    }
    pub fn execute<F>(&self, f: F)
    where
        F: FnOnce() + Send + 'static,
    {
        let job = Box::new(f);
        self.sender.as_ref().unwrap().send(job).unwrap();
    }
}
impl Drop for ThreadPool {
    fn drop(&mut self) {
        drop(self.sender.take());

        for worker in &mut self.workers {
            println!("Shutting down worker {}", worker.id);

            if let Some(thread) = worker.thread.take() {
                thread.join().unwrap();
            }
        }
    }
}

pub struct Worker {
    id: usize,
    thread: Option<thread::JoinHandle<()>>,
}

impl Worker {
    pub fn new(id: usize, receiver: Arc<Mutex<mpsc::Receiver<Job>>>) -> Worker {
        let thread = thread::spawn(move || loop {
            let message = receiver.lock().unwrap().recv();
            match message {
                Ok(job) => {
                    job();
                }
                Err(_) => {
                    break;
                }
            }
        });
        Worker {
            id,
            thread: Some(thread),
        }
    }
}

type Job = Box<dyn FnOnce() + Send + 'static>;

pub struct Webserver {
    address: String,
}

impl Webserver {
    pub fn build(ip: String, port: String) -> Result<Webserver, &'static str> {
        let re_ip = Regex::new(r"^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$").unwrap();
        match re_ip.captures(ip.as_str()) {
            Some(_) => Ok(Webserver {
                address: format!("{ip}:{port}"),
            }),
            None => Err("Invalid ip"),
        }
    }
}

pub fn run(web_server: Webserver) -> Result<(), Box<dyn Error>> {
    let listener = TcpListener::bind(web_server.address)?;

    let threads = ThreadPool::new(5);

    for stream in listener.incoming() {
        let stream = stream?;
        println!("Stream: {:?}", stream);

        threads.execute(|| {
            let result = panic::catch_unwind(AssertUnwindSafe(|| {
                if let Err(e) = handle_connection(stream) {
                    eprintln!("Error handling connection: {}", e);
                }
            }));

            if let Err(_) = result {
                eprintln!("Caught a panic while handling a connection.");
            }
        });
    }

    Ok(())
}

const PATH: &str = "src/volume/visits.txt";
fn read_visits() -> Result<String, Box<dyn Error>> {
    fs::read_to_string(PATH)
        .map_err(|e| e.into())
}

fn update_visits() -> Result<(), Box<dyn Error>>{
    let mut current_visits: i32 = read_visits()?.parse()?;
    current_visits += 1;
    fs::write(PATH, current_visits.to_string()).map_err(|e| e.into())
}
fn handle_connection(mut stream: std::net::TcpStream) -> Result<(), Box<dyn Error>> {
    let buf_reader = BufReader::new(&mut stream);
    let req_line = buf_reader.lines().next().ok_or("Request line not found")??;

    let response = match req_line.as_str() {
        "GET / HTTP/1.1" => {
            let utc_now = Utc::now();
            let moscow_time = utc_now.with_timezone(&FixedOffset::east_opt(3 * 3600).unwrap());
            let moscow_time_str = moscow_time.format("%H:%M:%S").to_string();
            update_visits()?;
            let content = format!("<h1>Time in Moscow is: {}</h1>", moscow_time_str);
            format!("HTTP/1.1 200 OK\r\nContent-Length: {}\r\n\r\n{}", content.len(), content)
        }
        "GET /visits HTTP/1.1" => {
            match read_visits() {
                Ok(visits) => format!("HTTP/1.1 200 OK\r\nContent-Length: {}\r\n\r\n{}", visits.len(), visits),
                Err(e) => {
                    eprintln!("Error reading visits: {}", e);
                    format!("HTTP/1.1 500 INTERNAL SERVER ERROR\r\n\r\nInternal Server Error")
                }
            }
        }
        _ => {
            let content = fs::read_to_string("error.html").unwrap_or_else(|_| String::from("404 Not Found"));
            format!("HTTP/1.1 404 NOT FOUND\r\nContent-Length: {}\r\n\r\n{}", content.len(), content)
        }
    };

    stream.write_all(response.as_bytes())?;
    stream.flush()?;
    Ok(())
}


#[cfg(test)]
mod tests {
    #[test]
    fn test_handle_connection() {
        print!("Testing is working");
    }
}
