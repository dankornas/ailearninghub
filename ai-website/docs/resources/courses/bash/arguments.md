---
title: Arguments
hide:
  - path
  - navigation
---

# Bash Scripting: Arguments

=== "Learning Material"

    <!-- <iframe
        src="https://www.youtube.com/embed/2Gg6Seob5Mg"
        frameborder="0"
        allow="autoplay; encrypted-media"
        allowfullscreen
        >
    </iframe> -->

    ## Bash Script Arguments 

    In Bash scripting, arguments are the inputs passed to a script at the time of its execution. They enable scripts to be more flexible and reusable, as they can perform different operations based on the provided arguments.

    ## How to Pass Arguments to a Bash Script

    Arguments are passed to a Bash script after the script name, separated by spaces.

    For example, let's say we have a script called `myscript.sh`, and we want to pass three arguments to it (`arg1`, `arg2`, and `arg3`). We would do so as follows:

    ```bash
    ./myscript.sh arg1 arg2 arg3
    ```

    In the script, these arguments are accessed as `$1`, `$2`, `$3`, etc., where the number corresponds to the position of the argument. Here's an example script that prints the first three arguments:

    ```bash
    #!/bin/bash
    echo "First argument: $1"
    echo "Second argument: $2"
    echo "Third argument: $3"
    ```

    ## Special Variables for Arguments

    There are several special variables you can use when dealing with arguments in a Bash script:

    * `$0`: The name of the script itself.
    * `$1` to `$9`: The first 9 arguments to the script. `$1` is the first argument and so on.
    * `${10}` to `${N}`: The tenth argument and beyond. Note the use of curly braces for accessing arguments with a number greater than 9.
    * `$#`: The number of arguments passed to the script.
    * `$@`: All arguments passed to the script as a list of separate words.
    * `$*`: All arguments passed to the script as a single word.
    * `$$`: The process ID (PID) of the current script.
    * `$?`: The exit status of the last command executed in the script.

    For instance, if we update our script as follows:

    ```bash
    #!/bin/bash
    echo "Script name: $0"
    echo "Number of arguments: $#"
    echo "All arguments with \$@: $@"
    echo "All arguments with \$*: $*"
    ```

    And run it with `./myscript.sh arg1 arg2 arg3`, it would output:

    ```javascript
    Script name: ./myscript.sh
    Number of arguments: 3
    All arguments with $@: arg1 arg2 arg3
    All arguments with $*: arg1 arg2 arg3
    ```

    ## Shift Command

    The `shift` command in Bash allows you to "shift" the positional parameters of your script. This is useful when you want to iterate over each argument in a loop.

    When you call `shift`, all positional parameters move one position to the left. `$2` becomes `$1`, `$3` becomes `$2`, and so on. `$0` (the script name) is unaffected.

    Here's an example script that uses `shift` to print all arguments:

    ```bash
    #!/bin/bash
    while (( $# )); do
    echo "Argument: $1"
    shift
    done
    ```

    ## Getopts Command

    For more complex scripts where arguments might have options associated with them, the `getopts` command is useful. It allows you to handle arguments with options in a more organized way.

    Here's an example of how to use `getopts`:

    ```bash
    #!/bin/bash

    while getopts ":a:b:c:" opt; do
    case ${opt} in
        a ) echo "Option -a has value $OPTARG"
        ;;
        b ) echo "Option -b has value $OPTARG"
        ;;
        c ) echo "Option -c has value $OPTARG"
        ;;
        \? ) echo "Invalid Option: -$OPTARG"
        ;;
        : ) echo "Option -$OPTARG requires an argument"
        ;;
    esac
    done
    ```

    In this script, the `getopts` command is used in a `while` loop to iterate over the options. The options are defined in the `getopts` command itself: `:a:b:c:`. This means the script expects options `-a`, `-b`, and `-c`, and each of these options requires a value.

    `$OPTARG` holds the value of the current option, and `$opt` is the current option itself. The `case` command is used to handle each option separately.

    ## Conclusion

    Bash script arguments are a powerful tool for making your scripts flexible and reusable. They allow your scripts to accept inputs directly from the command line, enabling them to perform different tasks depending on those inputs.

    By understanding and using these features, you can write more adaptable and powerful Bash scripts. Keep practicing and exploring different use cases to strengthen your command over Bash script arguments.

=== "All Lessons"
    {nav}

---

!!! note "Version 1.0"

    This is currently an early version of the learning material and it will be updated over time with more detailed information.

    A video will be provided with the learning material as well.

    Be sure to subscribe to stay up-to-date with the latest updates.

<div style="padding: 20px; color: white; background-color: #0f1624; border-radius: 10px; margin: 10px 0 20px 0; text-align: center;">
    <h2 style="color: white;">Need help mastering Machine Learning?</h2>
    <p style="font-size: 16px;">Don't just follow along — join me!
    Get exclusive access to me, your instructor, who can help answer any of your questions. Additionally, get access to a private learning group where you can learn together and support each other on your AI journey.
    </p><br>
    <div style="text-align: center; margin-bottom: 20px;">
        <button style="display: inline-block; padding: 10px 20px; font-size: 20px; color: white; background: #1018A8; border: none; border-radius: 5px;">
            <a href="/subscribe" style="color: white; text-decoration: none;">Subscribe Now</a>
        </button>
    </div>
</div>