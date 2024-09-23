# skeleton-cli-py

`skeleton-cli-py` is a skeleton for building Python3-based command line applications.

## Features

- Modular command structure using object-oriented programming
- Logging for debugging and error tracking
- Error handling with custom exceptions
- Use of argparse for flexible command-line argument parsing

## Requirements

- Python 3.7+

## Usage

The basic syntax for using `skeleton-cli-py` is:

```
$ ./skeleton-cli-py <command> [options]
```

Available commands:

- `command-a`: Execute command A
- `command-b`: Execute command B
- `command-c`: Execute command C (list, add, or remove items)
- `command-d`: Execute command D

For more information on each command, use:

```
$ ./skeleton-cli-py <command> --help
```

### Examples

1. Execute Command A:
   ```
   $ ./skeleton-cli-py command-a --option "example"
   ```

2. Execute Command B:
   ```
   $ ./skeleton-cli-py command-b --flag
   ```

3. Execute Command C (list items):
   ```
   $ ./skeleton-cli-py command-c --list
   ```

4. Execute Command C (add items):
   ```
   $ ./skeleton-cli-py command-c --add item1 item2 item3
   ```

5. Execute Command D:
   ```
   $ ./skeleton-cli-py command-d --name "John Doe"
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/license/mit) for details.
