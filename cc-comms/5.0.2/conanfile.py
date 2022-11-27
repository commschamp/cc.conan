from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout


class CcCommsConan(ConanFile):
    name = "cc-comms"
    version = "5.0.2"

    # Optional metadata
    license = "MPL-2.0"
    author = "Alex Robenko <arobenko@gmail.com>"
    homepage = "https://commschamp.github.io"
    url = "https://github.com/commschamp/comms"
    description = "Headers only library to implement binary communication protocols."
    topics = ("comms", "comms-champion", "communication-protocol")

    # Binary configuration
    settings = "compiler", "build_type"

    scm = {
        "type": "git",
        "url": "https://github.com/commschamp/comms.git",
        "revision": "v" + version
    }

    def validate(self):
        if self.settings.compiler.get_safe("cppstd"):
            tools.check_min_cppstd(self, "11")

    def package_id(self):
        self.info.header_only()

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.set_property("cmake_file_name", "LibComms")
        self.cpp_info.set_property("cmake_target_name", "cc::comms")
