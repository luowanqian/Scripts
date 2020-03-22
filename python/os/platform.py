import sys


def identify_platform():
    platform = sys.platform
    if platform.startswith("freebsd"):
        return "freebsd"
    elif platform.startswith("linux"):
        return "linux"
    elif platform.startswith("aix"):
        return "aix"
    elif platform.startswith("win"):
        return "windows"
    elif platform.startswith("darwin"):
        return "macos"
    else:
        return "unknown"


if __name__ == "__main__":
    print(f"Platform: {identify_platform()}")
