import argparse
import crew as crew
import pyperclip as pc
import questionary
import asyncio
import time 
import sys

GenC_output = " "

def copy_to_clipboard(abc):
    try:
        pc.copy(abc)
        return "Successfully copied"
    except Exception as e:
        return e

def two_choice(command):
    choice1 = "Copy command to clipboard"
    choice2 = "re-generate"
    choice = questionary.select(
        f"command: {command}",
        choices=[choice1,choice2,"exit"]
    ).ask()
    if choice == choice1:
        print()
        copy_to_clipboard(command)
        print(f"{command} copied to clipboard")
        return 
    elif choice == choice2:
        RegC = crew.regenerate(command)
        print("Regenerating command")
        sys.stdout.write("")
        sys.stdout.flush()
        two_choice(RegC)
    else:
        print("Bye....")

async def GenC(command):
    result = await asyncio.to_thread(crew.GenC, command)
    return result

async def loading(message):
    while True:
        for char in '|/-\\':
            print(f'\r {message} {char}', end='', flush=True)
            await asyncio.sleep(0.1)

async def main():
    # Create the parser
    parser = argparse.ArgumentParser(description="Command Line Interface Example")
    # Add mandatory argument
    parser.add_argument('-c', '--command', help='Mandatory string argument')
    # Add optional string arguments
    parser.add_argument('-e', '--explain', action='store_true', help='Optional string argument')
    # Add optional flags, which are boolean and don't require additional values
    parser.add_argument('-is', '--install', help='Launch interactive shell')
    parser.add_argument('-rg', '--regenerate', action='store_true', help='Regenerate data')
    # parser.add_argument('-ep', '--explain-previous', action='store_true', help='Execute in parallel')
    # parser.add_argument('-rgp', '--regenerate-previous', action='store_true', help='Regenerate plots')
    # parser.add_argument('-lib', '--library', action='store_true', help='Use specific library')
    # Parse arguments
    args = parser.parse_args()
    # Use the arguments
    if args.command:
        print(f"user query: {args.command}")
        loading_task = asyncio.create_task(loading("fetching command"))
        result = await GenC(args.command)
        loading_task.cancel()
        try:
            await loading_task
        except asyncio.CancelledError:
            pass
        print("\r")
        await asyncio.to_thread(two_choice,result)
        

        if args.explain:
            ExC = crew.ExC(GenC)
            print(f"Explanation for {GenC}")
            print(ExC)
        if args.regenerate:
            RegC = crew.regenerate(GenC)
            print(f"re-generated command for {GenC}")
            print(RegC)
    if args.install:
        # print(args.install0)
        InS = crew.installer(args.install)
        print(InS)
        

if __name__ == "__main__":
    asyncio.run(main())