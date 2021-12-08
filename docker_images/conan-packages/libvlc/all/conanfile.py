from conans import ConanFile, tools
from conans.errors import ConanException
from conans.errors import ConanInvalidConfiguration


class SysConfigVLCConan(ConanFile):
    name = "libvlc"
    version = "system"
    description = "cross-platform virtual conan package for libvlc support"
    topics = ("conan", "libvlc")
    url = "https://github.com/conan-io/conan-center-index"
    homepage = "https://code.videolan.org/videolan/vlc"
    license = "LGPLv2"
    settings = "os", "arch"

    def package_id(self):
        self.info.header_only()

    def _fill_cppinfo_from_pkgconfig(self, name):
        pkg_config = tools.PkgConfig(name)
        if not pkg_config.provides:
            raise ConanException("libvlc development files aren't available, give up")
        libs = [lib[2:] for lib in pkg_config.libs_only_l]
        lib_dirs = [lib[2:] for lib in pkg_config.libs_only_L]
        ldflags = [flag for flag in pkg_config.libs_only_other]
        include_dirs = [include[2:] for include in pkg_config.cflags_only_I]
        cflags = [flag for flag in pkg_config.cflags_only_other if not flag.startswith("-D")]
        defines = [flag[2:] for flag in pkg_config.cflags_only_other if flag.startswith("-D")]

        self.cpp_info.system_libs.extend(libs)
        self.cpp_info.libdirs.extend(lib_dirs)
        self.cpp_info.sharedlinkflags.extend(ldflags)
        self.cpp_info.exelinkflags.extend(ldflags)
        self.cpp_info.defines.extend(defines)
        self.cpp_info.includedirs.extend(include_dirs)
        self.cpp_info.cflags.extend(cflags)
        self.cpp_info.cxxflags.extend(cflags)

    def system_requirements(self):
        packages = []
        if tools.os_info.is_linux and self.settings.os == "Linux":
            if tools.os_info.with_apt:
                packages = ['libvlc-dev']
            else:
                self.output.warn("Don't know how to install libvlc for your distro.")
        if packages:
            package_tool = tools.SystemPackageTool(conanfile=self, default_mode='verify')
            for p in packages:
                package_tool.install(update=True, packages=p)

    def package_info(self):
        # TODO: Workaround for #2311 until a better solution can be found
        self.cpp_info.filenames["cmake_find_package"] = "libvlc_system"
        self.cpp_info.filenames["cmake_find_package_multi"] = "libvlc_system"
        self.cpp_info.includedirs = []
        self.cpp_info.libdirs = []
        self._fill_cppinfo_from_pkgconfig('libvlc')
