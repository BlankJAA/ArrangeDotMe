[app]

# (str) Title of your application
title = Arrange.ME

# (str) Package name
package.name = Arrange.Me

# (str) Package domain (needed for android/ios packaging)
package.domain = org.ArrangeDotMe

# (str) Directory containing the source code of your application
source.dir = /home/styx/Desktop/ChatGPT/ArrangeDotMe

# (str) Version number (instance.version is a string)
version = 0.1

# (int) Minimum API level for the Android version you are targeting
android.api = 21

# (str) Path to the Android NDK
# android.ndk_path =

# (list) Python for android (formerly python-for-android) whitelist
# android.p4a_whitelist =

# (bool) If True, then skip trying to update the Android SDK
# This can be useful to avoid excess SDK downloading or parsing
# android.skip_update = False

# (str) Android entry point, default is ok for Kivy-based app
# android.entrypoint = org.renpy.android.PythonActivity

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you do not need, since extra jars can slow
# down the build process. Allows wildcards matching, for example:
# OUYA-ODK/libs/*.jar
# android.add_jars = foo.jar,bar.jar,path/to/more/*.jar

# (list) List of Java files to add to the android project (can be java or a
# directory containing the files)
# android.add_src =

# (str) Python-for-android fork to use, defaults to upstream (kivy)
# python.for_android_fork = kivy

# (str) android.add_bundles =
#
# (list) Android application meta-data to set (key=value format)
# android.meta_data =

# (list) Android library project to add (will be added in the
# project.properties automatically.)
# android.library_references =

# (str) Android logcat filters to use
# android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
# python.copy_libs = 1

# (str) The Android arch to build for, defaults to armeabi-v7a
#
# choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = armeabi-v7a

# (int) overrides automatic detection of sdl2 version to use
#
# set to 16 for android-16 (for android-9 set to 9 etc.)
# sdl2.version = 16

# (str) Python-for-android branch to use, defaults to stable
# python.for_android_branch = stable

# (str) OSX architecture to build for
# osx.arch = i386

# (str) comma separated list of dependencies
# comma separated list of dependencies
# 
# e.g. requirements = kivy,python3,kivy-garden
requirements = python3,kivy==2.1.0

