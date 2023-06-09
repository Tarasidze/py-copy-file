def copy_file(command: str) -> None:
    command_list = command.split(" ")

    if len(command_list) < 3:
        return

    cmd = command_list[0]
    file_name_in = command_list[1]
    file_name_out = command_list[2]

    if file_name_in == file_name_out or cmd != "cp":
        return

    with (open(file_name_in, "r") as file_in,
          open(file_name_out, "w") as file_out):
        file_content = file_in.read()
        file_out.write(file_content)

    return
