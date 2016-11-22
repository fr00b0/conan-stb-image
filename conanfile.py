from conans import ConanFile
from conans.tools import download, check_sha256

class StbImageConan(ConanFile):
    name = "stb_image"
    version = "2.12"
    settings = "os", "compiler", "build_type", "arch"
    url = "https://github.com/fr00b0/conan-stb_image"

    header_file = "stb_image.h"
    download_url = "https://raw.githubusercontent.com/nothings/stb/fdca443892d0ce3c8680e6f38f196c61e95c7de3/stb_image.h"
    sha256_hash = "c9812cbd6c6d9152d7af30e164728bc0c4dcfe0181d1860ecba9ba5ab5d203cc"

    def source(self):
        download(self.download_url, self.header_file)
        check_sha256(self.header_file, self.sha256_hash)

    def build(self):
        pass  # Header only library

    def package(self):
        self.copy(self.header_file, dst="include/stb", src=".")

    def package_info(self):
        pass  # Header only library
