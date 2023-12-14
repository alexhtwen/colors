def set_color(text: str, fg_color: tuple[int, int, int] = None, bg_color: tuple[int, int, int] = None) -> str:
    """
    Returns a string with ANSI escape sequences to set text and/or background color.

    :param text: The text to colorize.
    :param fg_color: A tuple (r, g, b) for the foreground color.
    :param bg_color: A tuple (r, g, b) for the background color.
    :return: A string with ANSI escape sequences.
    """
    escape_sequence = "\033["

    if fg_color:
        escape_sequence += f"38;2;{fg_color[0]};{fg_color[1]};{fg_color[2]}"
        if bg_color:
            escape_sequence += ";"

    if bg_color:
        escape_sequence += f"48;2;{bg_color[0]};{bg_color[1]};{bg_color[2]}"

    print(escape_sequence + "m" + text + "\033[0m")
    print(escape_sequence)
    print("\033[0m")
    return escape_sequence + "m" + text + "\033[0m"  # Reset to default after the text

# Example Usage
# set_color("Hello, World!", fg_color=(255, 0, 0), bg_color=(0, 255, 0))
print(set_color("Hello, World!", fg_color=(255, 0, 0), bg_color=(0, 255, 0)))  # Red text on green background
