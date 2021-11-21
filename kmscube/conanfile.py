from conans import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake
from conan.tools.layout import cmake_layout


class AppConan(ConanFile):
    name = "kmscube"
    version = "0.1"
    generators = "CMakeToolchain", "CMakeDeps"
    requires = "opengles/system", "drm/system", "gbm/system", "egl/system"
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = "CMakeLists.txt", "src/*"

    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
