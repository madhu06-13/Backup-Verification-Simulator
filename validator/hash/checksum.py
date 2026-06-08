import hashlib


def calculate_checksum(file_path):

    with open(file_path, "rb") as file:

        file_content = file.read()

    return hashlib.md5(
        file_content
    ).hexdigest()