[app]
title = SoR OS
package.name = soros
package.domain = com.zyro.sor
source.dir = .
source.include_exts = py,png,jpg,json
version = 1.0

requirements = python3,flet

orientation = portrait
fullscreen = 1

android.api = 34
android.minapi = 21
android.build_tools = 34.0.0
android.ndk = 26b
android.ndk_api = 21

android.permissions = INTERNET
android.release = 0

[buildozer]
log_level = 2
warn_on_root = 1
