class PathUtils:
    @staticmethod
    def get_extension(filename):
        """Return a file extension (including the dot)"""
        return filename[filename.rfind("."):] if "." in filename else ""
    
    # TODO
    @staticmethod
    # Return the directory path without the file name
    def get_directory(path):
        pass
    # Return the file name from the directory path
    def get_basename(path):
        pass

# Use the class
print(PathUtils.get_extension("image.png"))
print(PathUtils.get_extension("1.txt"))
print(PathUtils.get_extension("test"))