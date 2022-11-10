from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, CMakeDeps, cmake_layout


class CcUbloxConan(ConanFile):
    name = "cc-ublox"
    version = "2.0"
    requires = "cc-comms/[>=5.0.1]"

    # Optional metadata
    license = "None"
    author = "Alex Robenko <arobenko@gmail.com>"
    homepage = "https://commschamp.github.io"
    url = "https://github.com/commschamp/cc.commsdsl.commsdsl"
    description = "UBX protocol definition headers only library implemented using COMMS library from the CommsChampion Ecosystem. The UBX binary protocol is used by the u-blox GPS receivers."
    topics = ("comms-champion", "communication-protocol", "ublox")

    # Binary configuration
    settings = "compiler", "build_type"

    scm = {
        "type": "git",
        "url": "https://github.com/commschamp/cc.ublox.generated.git",
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

        deps = CMakeDeps(self)
        deps.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.set_property("cmake_file_name", "cc_ublox")
        self.cpp_info.set_property("cmake_target_name", "cc::ublox")
