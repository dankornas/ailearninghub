---
title: Case Statements
hide:
  - path
  - navigation
---

# Bash Scripting: Case Statements

=== "Learning Material"

    <iframe
        src="https://www.youtube.com/embed/2Gg6Seob5Mg"
        frameborder="0"
        allow="autoplay; encrypted-media"
        allowfullscreen
        >
    </iframe>

    ## What is a Case Statement?

    The `case` statement is used in Bash to perform pattern matching against a single value. It is similar to the `switch` statement in other languages, such as C or Java. The `case` statement can match strings, but it can't directly compare numeric values. However, it can be combined with other constructs to do numeric comparisons.

    The `case` statement is useful when you need to make complex decisions in your scripts. It can make your code cleaner and easier to read.

    ## Syntax

    The syntax of a Bash case statement is:

    ```bash
    case expression in
        pattern1)
            commands
            ;;
        pattern2)
            commands
            ;;
        pattern3)
            commands
            ;;
        *)
            commands
            ;;
    esac
    ```

    * `expression`: This is the value that you are trying to match against.
    * `pattern1, pattern2, pattern3`: These are the patterns that you are trying to match. The patterns can be literal strings or wildcard expressions.
    * `commands`: These are the commands that will be executed if the pattern matches.
    * `;;`: This is used to terminate each case.
    * `*)`: This is a catch-all case that will match any value. It is optional but is usually included as the last case. It is similar to the `default` case in a `switch` statement in other languages.
    * `esac`: This is used to end the case statement.


    ## Basic Case Statement

    ```bash
    #!/bin/bash

    read -p "Enter a fruit: " fruit

    case $fruit in
        "apple")
            echo "Apple is tasty."
            ;;
        "banana")
            echo "Banana is sweet."
            ;;
        "orange")
            echo "Orange is sour."
            ;;
        *)
            echo "I don't know about that fruit."
            ;;
    esac
    ```

    In this script, you are prompted to enter a fruit. The script then checks the entered fruit against the cases and outputs a message depending on the fruit entered.

    ## Case Statement with Wildcard Patterns

    ```bash
    #!/bin/bash

    read -p "Enter a filename: " filename

    case $filename in
        *.txt)
            echo "This is a text file."
            ;;
        *.sh)
            echo "This is a shell script."
            ;;
        *.py)
            echo "This is a Python script."
            ;;
        *)
            echo "Unknown file type."
            ;;
    esac
    ```

    In this script, you are prompted to enter a filename. The script then checks the file extension against the cases and outputs a message depending on the file type.

    ## Case Statement with Multiple Patterns

    ```bash
    #!/bin/bash

    read -p "Enter a day: " day

    case $day in
        "Monday"|"Tuesday"|"Wednesday"|"Thursday"|"Friday")
            echo "It's a weekday."
            ;;
        "Saturday"|"Sunday")
            echo "It's a weekend."
            ;;
        *)
            echo "Invalid day."
            ;;
    esac
    ```

    In this script, you are prompted to enter a day. The script then checks the entered day against the cases and outputs a message depending on the day entered.

    ## Conclusion

    The `case` statement is a powerful tool in Bash that allows you to perform complex decisions based on pattern matching. It can be used to match literal strings or wildcard patterns, and it can be combined with other constructs to perform numeric comparisons.

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