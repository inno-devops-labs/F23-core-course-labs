use regex::Regex;
use std::error::Error;
use std::sync::{mpsc, Arc, Mutex};
use std::thread;
use std::{
    fs,
    io::{prelude::*, BufReader},
    net::TcpListener,
};

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

    for stream in listener.incoming() {
        let stream = stream?;
        println!("Stream: {:?}", stream);

        let threads = ThreadPool::new(5);

        threads.execute(|| handle_connection(stream));
    }

    Ok(())
}

fn handle_connection(mut stream: std::net::TcpStream) {
    let buf_reader = BufReader::new(&mut stream);
    let req = buf_reader.lines().next().unwrap().unwrap();

    let utc_now = Utc::now();

    // Convert the UTC time to Moscow time
    let moscow_time = utc_now.with_timezone(&FixedOffset::east_opt(3 * 3600).unwrap());
    let moscow_time = moscow_time.format("%H:%M:%S");

    let moscow_time_str = moscow_time.to_string();

    let (res_code, content) = if req == "GET / HTTP/1.1" {
        let response = format!("<h1>Time in moscow is:  {} </h1>", moscow_time_str);
        (String::from("HTTP/1.1 200 OK"), response)
    } else {
        (
            String::from("HTTP/1.1 404 NOT FOUND"),
            fs::read_to_string("error.html").unwrap(),
        )
    };

    let length = content.len();

    let res = format!("{res_code}\r\nContent-Length: {length}\r\n\r\n{content}");

    stream.write_all(res.as_bytes()).unwrap();
    stream.flush().unwrap();
}

#[cfg(test)]
mod tests {

    #[test]
    fn test_handle_connection() {
        print!("Testing is working");
    }
}
