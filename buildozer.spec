[app]
title = SoR OS
package.name = soros
package.domain = com.zyro.sor
source.dir = .
source.include_exts = py,png,jpg,json
version = 26.0
requirements = python3,flet
orientation = portrait
fullscreen = 1
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 23
android.manifest.intent_filters = [{"name": "android.intent.action.MAIN", "actions": ["android.intent.action.MAIN"], "categories": ["android.intent.category.HOME", "android.intent.category.DEFAULT"]}]
android.release = 0

[buildozer]
log_level = 2
warn_on_root = 1
