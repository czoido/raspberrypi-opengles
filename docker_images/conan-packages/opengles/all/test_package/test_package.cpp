#include <iostream>

bool init_context() { return true; }

#include <stdio.h>

#ifndef GL_ES_VERSION_2_0
#include <GLES2/gl2.h>
#endif
#include <GLES2/gl2ext.h>
#include <EGL/egl.h>
#include <EGL/eglext.h>


bool init_context();

int main()
{
    const char * gl_vendor = (const char *) glGetString(GL_VENDOR);
    const char * gl_renderer = (const char *) glGetString(GL_RENDERER);
    const char * gl_version = (const char *) glGetString(GL_VERSION);
    const char * gl_extensions = (const char *) glGetString(GL_EXTENSIONS);
    std::cout << "GL_VENDOR: " << (gl_vendor ? gl_vendor : "(null)") << std::endl;
    std::cout << "GL_RENDERER: " << (gl_renderer ? gl_renderer : "(null)") << std::endl;
    std::cout << "GL_VERSION: " << (gl_version ? gl_version : "(null)") << std::endl;
    std::cout << "GL_EXTENSIONS: " << (gl_extensions ? gl_extensions : "(null)") << std::endl;
    return 0;
}
