# Miscellaneous

## Code quality

In order to lint the project there are `clippy` and `markdownlint`:

```bash
cargo clippy
markdownlint RUST.md README.md
```

### Examples

```bash
> cargo clippy
warning: field assignment outside of initializer for an instance created with Default::default()
  --> src/main.rs:27:5
   |
27 |     config.address = args.host.parse().unwrap();
   |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   |
note: consider initializing the variable with
`rocket::Config { 
    address: args.host.parse().unwrap(),
    port: args.port,
    ..Default::default() 
}` and removing relevant reassignments
  --> src/main.rs:26:5
   |
26 |     let mut config = Config::default();
   |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   = help: for further information visit 
   https://rust-lang.github.io/rust-clippy/master/index.html#field_reassign_with_default
   = note: `#[warn(clippy::field_reassign_with_default)]` on by default

warning: `app_rust` (bin "app_rust") generated 2 warnings
(run `cargo clippy --fix --bin "app_rust"` to apply 1 suggestion)
    Finished dev [unoptimized + debuginfo] target(s) in 0.07s
```

```bash
> markdownlint RUST.md README.md
RUST.md:23:81 MD013/line-length Line length [Expected: 80; Actual: 95]
RUST.md:32:81 MD013/line-length Line length [Expected: 80; Actual: 123]
```
