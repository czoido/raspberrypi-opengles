cmake_minimum_required(VERSION 3.1)

project(kmscube)

find_package(drm REQUIRED)
find_package(gbm REQUIRED)
find_package(opengles REQUIRED)
find_package(egl REQUIRED)
find_package(Threads REQUIRED)

set(SOURCES src/common.c
            src/cube-shadertoy.c
            src/cube-smooth.c
            src/cube-tex.c
            src/drm-atomic.c
            src/drm-common.c
            src/drm-legacy.c
            src/esTransform.c
            src/frame-512x512-NV12.c
            src/frame-512x512-RGBA.c
            src/kmscube.c
            src/perfcntrs.c)

add_executable(kmscube ${SOURCES})

target_link_libraries(${PROJECT_NAME} drm::drm gbm::gbm opengles::opengles egl::egl Threads::Threads m)

install(TARGETS kmscube DESTINATION "."
        RUNTIME DESTINATION bin
        ARCHIVE DESTINATION lib
        LIBRARY DESTINATION lib)