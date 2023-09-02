import os

def set_working_directory(new_directory):
    """
    Set the working directory to the specified path.

    :param new_directory: The path to the desired working directory.
    """
    try:
        # Set the new working directory
        os.chdir(new_directory)
        print("Working directory set to:", new_directory)
    except Exception as e:
        print("Error:", str(e))
