from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, CMakeDeps, cmake_layout


class CcCommsdslConan(ConanFile):
    name = "cc-commsdsl"
    version = "5.1.3"
    requires = "libxml2/[>=2.9]"

    # Optional metadata
    license = "Apache-2.0"
    author = "Alex Robenko <arobenko@gmail.com>"
    homepage = "https://commschamp.github.io"
    url = "https://github.com/commschamp/commsdsl"
    description = "Code generators for CommsChampion Ecosystem."
    topics = ("comms-champion", "communication-protocol")

    # Binary configuration
    settings = "os", "arch", "compiler", "build_type"

    scm = {
        "type": "git",
        "url": "https://github.com/commschamp/commsdsl.git",
        "revision": "v" + version
    }

    default_options = {
        "warn_as_err": True,
        "use_ccache": True,
        "install_lib": False,
        "commsdsl2comms": True,
        "commsdsl2test": False,
        "commsdsl2tools_qt": False,
        "commsdsl2swig": False,
    }

    options = {name: [True, False] for name in default_options.keys()}

    def validate(self):
        if self.settings.compiler.get_safe("cppstd"):
            tools.check_min_cppstd(self, "17")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.variables["COMMSDSL_WARN_AS_ERR"] = 'ON' if self.options.warn_as_err else 'OFF'
        tc.variables["COMMSDSL_USE_CCACHE"] = 'ON' if self.options.use_ccache else 'OFF'
        tc.variables["COMMSDSL_INSTALL_LIBRARY"] = 'ON' if self.options.install_lib else 'OFF'
        tc.variables["COMMSDSL_BUILD_COMMSDSL2COMMS"] = 'ON' if self.options.commsdsl2comms else 'OFF'
        tc.variables["COMMSDSL_BUILD_COMMSDSL2TEST"] = 'ON' if self.options.commsdsl2test else 'OFF'
        tc.variables["COMMSDSL_BUILD_COMMSDSL2TOOLS_QT"] = 'ON' if self.options.commsdsl2tools_qt else 'OFF'
        tc.variables["COMMSDSL_BUILD_COMMSDSL2SWIG"] = 'ON' if self.options.commsdsl2swig else 'OFF'
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

