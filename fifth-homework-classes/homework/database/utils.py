from os import path


def confirm_overwrite(filename):
    if not path.exists(filename):
        return True

    response = input(
        f"{filename} already exists and will be overwritten! Are you sure you want to continue? (y/n): "
    )
    return response.lower() == "y"
