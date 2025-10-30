cmake_minimum_required(VERSION 3.25)
project(swift LANGUAGES CXX)

# Python + NumPy
find_package(Python COMPONENTS Interpreter Development.Module NumPy REQUIRED)

Python_add_library(phys MODULE swift/core/phys.cpp WITH_SOABI)
target_compile_features(phys PRIVATE cxx_std_17)
target_include_directories(phys PRIVATE
    ${Python_NumPy_INCLUDE_DIRS}
    ${CMAKE_CURRENT_SOURCE_DIR}/swift/core
)
target_link_libraries(phys PRIVATE Python::Module Python::NumPy)
install(TARGETS phys LIBRARY DESTINATION swift)

