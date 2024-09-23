#!/usr/bin/env python3

"""
skeleton-cli-py

A generic CLI tool skeleton that demonstrates Python3 best practices.

Usage:
    skeleton-cli-py <command> [options]

Available commands:
    command-a    Execute command A
    command-b    Execute command B
    command-c    Execute command C (list, add, or remove items)
    command-d    Execute command D

For more information on each command, use:
    skeleton-cli-py <command> --help
"""

import argparse
import sys
import logging
from typing import List, Optional
from dataclasses import dataclass
from abc import ABC, abstractmethod

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Custom exception
class SkeletonCliError(Exception):
    """Base exception for skeleton-cli-py"""

@dataclass
class CommandResult:
    """Dataclass to store command execution results"""
    success: bool
    message: str

class Command(ABC):
    """Abstract base class for commands"""

    @abstractmethod
    def execute(self, args: argparse.Namespace) -> CommandResult:
        """Execute the command"""
        pass

class CommandA(Command):
    def execute(self, args: argparse.Namespace) -> CommandResult:
        logger.info(f"Executing Command A with option: {args.option}")
        return CommandResult(success=True, message=f"Command A executed with option: {args.option}")

class CommandB(Command):
    def execute(self, args: argparse.Namespace) -> CommandResult:
        logger.info(f"Executing Command B with flag: {args.flag}")
        return CommandResult(success=True, message=f"Command B executed with flag: {args.flag}")

class CommandC(Command):
    def execute(self, args: argparse.Namespace) -> CommandResult:
        if args.list:
            logger.info("Listing items")
            return CommandResult(success=True, message="Items listed")
        elif args.add:
            logger.info(f"Adding items: {args.add}")
            return CommandResult(success=True, message=f"Items added: {args.add}")
        elif args.remove:
            logger.info(f"Removing items: {args.remove}")
            return CommandResult(success=True, message=f"Items removed: {args.remove}")
        else:
            return CommandResult(success=False, message="Invalid subcommand for Command C")

class CommandD(Command):
    def execute(self, args: argparse.Namespace) -> CommandResult:
        logger.info(f"Executing Command D with name: {args.name}")
        return CommandResult(success=True, message=f"Command D executed with name: {args.name}")

def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description='skeleton-cli-py: A generic CLI tool skeleton',
        epilog='For more information, see the inline documentation.'
    )
    subparsers = parser.add_subparsers(help='Available commands', title='commands', dest='command')

    # Command A parser
    parser_a = subparsers.add_parser('command-a', help='Execute command A')
    parser_a.add_argument('--option', type=str, required=True, help='Option for command A')

    # Command B parser
    parser_b = subparsers.add_parser('command-b', help='Execute command B')
    parser_b.add_argument('--flag', action='store_true', help='Flag for command B')

    # Command C parser
    parser_c = subparsers.add_parser('command-c', help='Execute command C')
    group_c = parser_c.add_mutually_exclusive_group(required=True)
    group_c.add_argument('--list', action='store_true', help='List items')
    group_c.add_argument('--add', nargs="+", metavar='item', help='Add items')
    group_c.add_argument('--remove', nargs="+", metavar='item', help='Remove items')

    # Command D parser
    parser_d = subparsers.add_parser('command-d', help='Execute command D')
    parser_d.add_argument('--name', metavar='name', required=True, help='Specify a name for command D')

    return parser

def main() -> None:
    parser = create_parser()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    command_map = {
        'command-a': CommandA(),
        'command-b': CommandB(),
        'command-c': CommandC(),
        'command-d': CommandD(),
    }

    try:
        command = command_map[args.command]
        result = command.execute(args)
        if result.success:
            logger.info(result.message)
        else:
            logger.error(result.message)
            sys.exit(1)
    except SkeletonCliError as e:
        logger.error(f"An error occurred: {str(e)}")
        sys.exit(1)
    except Exception as e:
        logger.exception(f"An unexpected error occurred: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    main()
