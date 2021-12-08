#include <iostream>

#include <vlc/vlc.h>

int main()
{
    libvlc_instance_t*  vlc = libvlc_new(0, nullptr);
    libvlc_release(vlc);
    return 0;
}
