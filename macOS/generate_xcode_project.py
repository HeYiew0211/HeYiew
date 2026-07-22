#!/usr/bin/env python3
"""Generate a valid Xcode 26 project for the Snake Game macOS app."""

import os
import hashlib

def make_uuid(seed):
    """Generate a deterministic 24-char hex UUID from a seed string."""
    return hashlib.sha256(seed.encode()).hexdigest()[:24].upper()

# Generate all UUIDs deterministically
names = [
    "project_obj", "main_group", "snakegame_group", "products_group",
    "product_ref", "native_target",
    "main_swift_fileref", "main_swift_buildfile",
    "appdelegate_swift_fileref", "appdelegate_swift_buildfile",
    "info_plist_fileref", "info_plist_buildfile",
    "index_html_fileref", "index_html_buildfile",
    "assets_fileref", "assets_buildfile",
    "sources_phase", "resources_phase", "frameworks_phase",
    "project_debug_config", "project_release_config",
    "project_config_list",
    "target_debug_config", "target_release_config",
    "target_config_list",
]
uuids = {n: make_uuid(n) for n in names}

# Helper: quote a string for pbxproj (escape quotes and backslashes)
def q(s):
    return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'

# Build the pbxproj content using Python's triple-quoted string with .format()
T = '\t'  # pbxproj REQUIRES tabs for indentation

pbxproj = f"""// !$*UTF8*$!
{{
{T}archiveVersion = 1;
{T}classes = {{
{T}}};
{T}objectVersion = 77;
{T}objects = {{

{T}/* Begin PBXBuildFile section */
{T}{T}{uuids["main_swift_buildfile"]} /* main.swift in Sources */ = {{isa = PBXBuildFile; fileRef = {uuids["main_swift_fileref"]} /* main.swift */; }};
{T}{T}{uuids["appdelegate_swift_buildfile"]} /* AppDelegate.swift in Sources */ = {{isa = PBXBuildFile; fileRef = {uuids["appdelegate_swift_fileref"]} /* AppDelegate.swift */; }};
{T}{T}{uuids["index_html_buildfile"]} /* index.html in Resources */ = {{isa = PBXBuildFile; fileRef = {uuids["index_html_fileref"]} /* index.html */; }};
{T}{T}{uuids["assets_buildfile"]} /* Assets.xcassets in Resources */ = {{isa = PBXBuildFile; fileRef = {uuids["assets_fileref"]} /* Assets.xcassets */; }};
{T}/* End PBXBuildFile section */

{T}/* Begin PBXFileReference section */
{T}{T}{uuids["product_ref"]} /* 贪吃蛇.app */ = {{isa = PBXFileReference; explicitFileType = wrapper.application; includeInIndex = 0; path = {q("贪吃蛇.app")}; sourceTree = BUILT_PRODUCTS_DIR; }};
{T}{T}{uuids["main_swift_fileref"]} /* main.swift */ = {{isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = main.swift; sourceTree = "<group>"; }};
{T}{T}{uuids["appdelegate_swift_fileref"]} /* AppDelegate.swift */ = {{isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = AppDelegate.swift; sourceTree = "<group>"; }};
{T}{T}{uuids["info_plist_fileref"]} /* Info.plist */ = {{isa = PBXFileReference; lastKnownFileType = text.plist.xml; path = Info.plist; sourceTree = "<group>"; }};
{T}{T}{uuids["index_html_fileref"]} /* index.html */ = {{isa = PBXFileReference; lastKnownFileType = text.html; path = index.html; sourceTree = "<group>"; }};
{T}{T}{uuids["assets_fileref"]} /* Assets.xcassets */ = {{isa = PBXFileReference; lastKnownFileType = folder.assetcatalog; path = Assets.xcassets; sourceTree = "<group>"; }};
{T}/* End PBXFileReference section */

{T}/* Begin PBXFrameworksBuildPhase section */
{T}{T}{uuids["frameworks_phase"]} /* Frameworks */ = {{
{T}{T}{T}isa = PBXFrameworksBuildPhase;
{T}{T}{T}buildActionMask = 2147483647;
{T}{T}{T}files = (
{T}{T}{T});
{T}{T}{T}runOnlyForDeploymentPostprocessing = 0;
{T}{T}}};
{T}/* End PBXFrameworksBuildPhase section */

{T}/* Begin PBXGroup section */
{T}{T}{uuids["main_group"]} = {{
{T}{T}{T}isa = PBXGroup;
{T}{T}{T}children = (
{T}{T}{T}{T}{uuids["index_html_fileref"]} /* index.html */,
{T}{T}{T}{T}{uuids["snakegame_group"]} /* SnakeGame */,
{T}{T}{T}{T}{uuids["products_group"]} /* Products */,
{T}{T}{T});
{T}{T}{T}sourceTree = "<group>";
{T}{T}}};
{T}{T}{uuids["snakegame_group"]} /* SnakeGame */ = {{
{T}{T}{T}isa = PBXGroup;
{T}{T}{T}children = (
{T}{T}{T}{T}{uuids["main_swift_fileref"]} /* main.swift */,
{T}{T}{T}{T}{uuids["appdelegate_swift_fileref"]} /* AppDelegate.swift */,
{T}{T}{T}{T}{uuids["info_plist_fileref"]} /* Info.plist */,
{T}{T}{T}{T}{uuids["assets_fileref"]} /* Assets.xcassets */,
{T}{T}{T});
{T}{T}{T}path = SnakeGame;
{T}{T}{T}sourceTree = "<group>";
{T}{T}}};
{T}{T}{uuids["products_group"]} /* Products */ = {{
{T}{T}{T}isa = PBXGroup;
{T}{T}{T}children = (
{T}{T}{T}{T}{uuids["product_ref"]} /* 贪吃蛇.app */,
{T}{T}{T});
{T}{T}{T}name = Products;
{T}{T}{T}sourceTree = "<group>";
{T}{T}}};
{T}/* End PBXGroup section */

{T}/* Begin PBXNativeTarget section */
{T}{T}{uuids["native_target"]} /* SnakeGame */ = {{
{T}{T}{T}isa = PBXNativeTarget;
{T}{T}{T}buildConfigurationList = {uuids["target_config_list"]} /* Build configuration list for PBXNativeTarget "SnakeGame" */;
{T}{T}{T}buildPhases = (
{T}{T}{T}{T}{uuids["sources_phase"]} /* Sources */,
{T}{T}{T}{T}{uuids["frameworks_phase"]} /* Frameworks */,
{T}{T}{T}{T}{uuids["resources_phase"]} /* Resources */,
{T}{T}{T});
{T}{T}{T}buildRules = (
{T}{T}{T});
{T}{T}{T}dependencies = (
{T}{T}{T});
{T}{T}{T}name = SnakeGame;
{T}{T}{T}packageProductDependencies = (
{T}{T}{T});
{T}{T}{T}productName = SnakeGame;
{T}{T}{T}productReference = {uuids["product_ref"]} /* 贪吃蛇.app */;
{T}{T}{T}productType = {q("com.apple.product-type.application")};
{T}{T}}};
{T}/* End PBXNativeTarget section */

{T}/* Begin PBXProject section */
{T}{T}{uuids["project_obj"]} /* Project object */ = {{
{T}{T}{T}isa = PBXProject;
{T}{T}{T}attributes = {{
{T}{T}{T}{T}BuildIndependentTargetsInParallel = 1;
{T}{T}{T}{T}LastSwiftUpdateCheck = 2600;
{T}{T}{T}{T}LastUpgradeCheck = 2600;
{T}{T}{T}{T}TargetAttributes = {{
{T}{T}{T}{T}{T}{uuids["native_target"]} = {{
{T}{T}{T}{T}{T}{T}CreatedOnToolsVersion = 26.0;
{T}{T}{T}{T}{T}}};
{T}{T}{T}{T}}};
{T}{T}{T}}};
{T}{T}{T}buildConfigurationList = {uuids["project_config_list"]} /* Build configuration list for PBXProject "SnakeGame" */;
{T}{T}{T}compatibilityVersion = {q("Xcode 14.0")};
{T}{T}{T}developmentRegion = {q("zh-Hans")};
{T}{T}{T}hasScannedForEncodings = 0;
{T}{T}{T}knownRegions = (
{T}{T}{T}{T}en,
{T}{T}{T}{T}Base,
{T}{T}{T}{T}{q("zh-Hans")},
{T}{T}{T});
{T}{T}{T}mainGroup = {uuids["main_group"]};
{T}{T}{T}productRefGroup = {uuids["products_group"]} /* Products */;
{T}{T}{T}projectDirPath = {q("")};
{T}{T}{T}projectRoot = {q("")};
{T}{T}{T}targets = (
{T}{T}{T}{T}{uuids["native_target"]} /* SnakeGame */,
{T}{T}{T});
{T}{T}}};
{T}/* End PBXProject section */

{T}/* Begin PBXResourcesBuildPhase section */
{T}{T}{uuids["resources_phase"]} /* Resources */ = {{
{T}{T}{T}isa = PBXResourcesBuildPhase;
{T}{T}{T}buildActionMask = 2147483647;
{T}{T}{T}files = (
{T}{T}{T}{T}{uuids["index_html_buildfile"]} /* index.html in Resources */,
{T}{T}{T}{T}{uuids["assets_buildfile"]} /* Assets.xcassets in Resources */,
{T}{T}{T});
{T}{T}{T}runOnlyForDeploymentPostprocessing = 0;
{T}{T}}};
{T}/* End PBXResourcesBuildPhase section */

{T}/* Begin PBXSourcesBuildPhase section */
{T}{T}{uuids["sources_phase"]} /* Sources */ = {{
{T}{T}{T}isa = PBXSourcesBuildPhase;
{T}{T}{T}buildActionMask = 2147483647;
{T}{T}{T}files = (
{T}{T}{T}{T}{uuids["main_swift_buildfile"]} /* main.swift in Sources */,
{T}{T}{T}{T}{uuids["appdelegate_swift_buildfile"]} /* AppDelegate.swift in Sources */,
{T}{T}{T});
{T}{T}{T}runOnlyForDeploymentPostprocessing = 0;
{T}{T}}};
{T}/* End PBXSourcesBuildPhase section */

{T}/* Begin XCBuildConfiguration section */
{T}{T}{uuids["project_debug_config"]} /* Debug */ = {{
{T}{T}{T}isa = XCBuildConfiguration;
{T}{T}{T}buildSettings = {{
{T}{T}{T}{T}ALWAYS_SEARCH_USER_PATHS = NO;
{T}{T}{T}{T}ASSETCATALOG_COMPILER_GENERATE_SWIFT_ASSET_SYMBOL_EXTENSIONS = YES;
{T}{T}{T}{T}CLANG_ANALYZER_NONNULL = YES;
{T}{T}{T}{T}CLANG_CXX_LANGUAGE_STANDARD = {q("gnu++20")};
{T}{T}{T}{T}CLANG_ENABLE_MODULES = YES;
{T}{T}{T}{T}CLANG_ENABLE_OBJC_ARC = YES;
{T}{T}{T}{T}COPY_PHASE_STRIP = NO;
{T}{T}{T}{T}DEBUG_INFORMATION_FORMAT = dwarf;
{T}{T}{T}{T}ENABLE_STRICT_OBJC_MSGSEND = YES;
{T}{T}{T}{T}ENABLE_TESTABILITY = YES;
{T}{T}{T}{T}GCC_DYNAMIC_NO_PIC = NO;
{T}{T}{T}{T}GCC_OPTIMIZATION_LEVEL = 0;
{T}{T}{T}{T}GCC_PREPROCESSOR_DEFINITIONS = (
{T}{T}{T}{T}{T}{q("DEBUG=1")},
{T}{T}{T}{T}{T}{q("$(inherited)")},
{T}{T}{T}{T});
{T}{T}{T}{T}MACOSX_DEPLOYMENT_TARGET = 26.0;
{T}{T}{T}{T}MTL_ENABLE_DEBUG_INFO = INCLUDE_SOURCE;
{T}{T}{T}{T}ONLY_ACTIVE_ARCH = YES;
{T}{T}{T}{T}SDKROOT = macosx;
{T}{T}{T}{T}SWIFT_ACTIVE_COMPILATION_CONDITIONS = DEBUG;
{T}{T}{T}{T}SWIFT_OPTIMIZATION_LEVEL = {q("-Onone")};
{T}{T}{T}}};
{T}{T}{T}name = Debug;
{T}{T}}};
{T}{T}{uuids["project_release_config"]} /* Release */ = {{
{T}{T}{T}isa = XCBuildConfiguration;
{T}{T}{T}buildSettings = {{
{T}{T}{T}{T}ALWAYS_SEARCH_USER_PATHS = NO;
{T}{T}{T}{T}ASSETCATALOG_COMPILER_GENERATE_SWIFT_ASSET_SYMBOL_EXTENSIONS = YES;
{T}{T}{T}{T}CLANG_ANALYZER_NONNULL = YES;
{T}{T}{T}{T}CLANG_CXX_LANGUAGE_STANDARD = {q("gnu++20")};
{T}{T}{T}{T}CLANG_ENABLE_MODULES = YES;
{T}{T}{T}{T}CLANG_ENABLE_OBJC_ARC = YES;
{T}{T}{T}{T}COPY_PHASE_STRIP = NO;
{T}{T}{T}{T}DEBUG_INFORMATION_FORMAT = {q("dwarf-with-dsym")};
{T}{T}{T}{T}ENABLE_NS_ASSERTIONS = NO;
{T}{T}{T}{T}ENABLE_STRICT_OBJC_MSGSEND = YES;
{T}{T}{T}{T}GCC_OPTIMIZATION_LEVEL = s;
{T}{T}{T}{T}MACOSX_DEPLOYMENT_TARGET = 26.0;
{T}{T}{T}{T}MTL_ENABLE_DEBUG_INFO = NO;
{T}{T}{T}{T}SDKROOT = macosx;
{T}{T}{T}{T}SWIFT_COMPILATION_MODE = wholemodule;
{T}{T}{T}{T}SWIFT_OPTIMIZATION_LEVEL = {q("-O")};
{T}{T}{T}{T}VALIDATE_PRODUCT = YES;
{T}{T}{T}}};
{T}{T}{T}name = Release;
{T}{T}}};
{T}{T}{uuids["target_debug_config"]} /* Debug */ = {{
{T}{T}{T}isa = XCBuildConfiguration;
{T}{T}{T}buildSettings = {{
{T}{T}{T}{T}ASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;
{T}{T}{T}{T}CODE_SIGN_STYLE = Automatic;
{T}{T}{T}{T}COMBINE_HIDPI_IMAGES = YES;
{T}{T}{T}{T}CURRENT_PROJECT_VERSION = 1;
{T}{T}{T}{T}ENABLE_HARDENED_RUNTIME = YES;
{T}{T}{T}{T}GENERATE_INFOPLIST_FILE = NO;
{T}{T}{T}{T}INFOPLIST_FILE = SnakeGame/Info.plist;
{T}{T}{T}{T}LD_RUNPATH_SEARCH_PATHS = (
{T}{T}{T}{T}{T}{q("$(inherited)")},
{T}{T}{T}{T}{T}{q("@executable_path/../Frameworks")},
{T}{T}{T}{T});
{T}{T}{T}{T}MARKETING_VERSION = 1.0;
{T}{T}{T}{T}PRODUCT_BUNDLE_IDENTIFIER = com.snakegame.app;
{T}{T}{T}{T}PRODUCT_NAME = {q("贪吃蛇")};
{T}{T}{T}{T}SWIFT_EMIT_LOC_STRINGS = YES;
{T}{T}{T}{T}SWIFT_VERSION = 5.0;
{T}{T}{T}}};
{T}{T}{T}name = Debug;
{T}{T}}};
{T}{T}{uuids["target_release_config"]} /* Release */ = {{
{T}{T}{T}isa = XCBuildConfiguration;
{T}{T}{T}buildSettings = {{
{T}{T}{T}{T}ASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;
{T}{T}{T}{T}CODE_SIGN_STYLE = Automatic;
{T}{T}{T}{T}COMBINE_HIDPI_IMAGES = YES;
{T}{T}{T}{T}CURRENT_PROJECT_VERSION = 1;
{T}{T}{T}{T}ENABLE_HARDENED_RUNTIME = YES;
{T}{T}{T}{T}GENERATE_INFOPLIST_FILE = NO;
{T}{T}{T}{T}INFOPLIST_FILE = SnakeGame/Info.plist;
{T}{T}{T}{T}LD_RUNPATH_SEARCH_PATHS = (
{T}{T}{T}{T}{T}{q("$(inherited)")},
{T}{T}{T}{T}{T}{q("@executable_path/../Frameworks")},
{T}{T}{T}{T});
{T}{T}{T}{T}MARKETING_VERSION = 1.0;
{T}{T}{T}{T}PRODUCT_BUNDLE_IDENTIFIER = com.snakegame.app;
{T}{T}{T}{T}PRODUCT_NAME = {q("贪吃蛇")};
{T}{T}{T}{T}SWIFT_EMIT_LOC_STRINGS = YES;
{T}{T}{T}{T}SWIFT_VERSION = 5.0;
{T}{T}{T}}};
{T}{T}{T}name = Release;
{T}{T}}};
{T}/* End XCBuildConfiguration section */

{T}/* Begin XCConfigurationList section */
{T}{T}{uuids["project_config_list"]} /* Build configuration list for PBXProject "SnakeGame" */ = {{
{T}{T}{T}isa = XCConfigurationList;
{T}{T}{T}buildConfigurations = (
{T}{T}{T}{T}{uuids["project_debug_config"]} /* Debug */,
{T}{T}{T}{T}{uuids["project_release_config"]} /* Release */,
{T}{T}{T});
{T}{T}{T}defaultConfigurationIsVisible = 0;
{T}{T}{T}defaultConfigurationName = Release;
{T}{T}}};
{T}{T}{uuids["target_config_list"]} /* Build configuration list for PBXNativeTarget "SnakeGame" */ = {{
{T}{T}{T}isa = XCConfigurationList;
{T}{T}{T}buildConfigurations = (
{T}{T}{T}{T}{uuids["target_debug_config"]} /* Debug */,
{T}{T}{T}{T}{uuids["target_release_config"]} /* Release */,
{T}{T}{T});
{T}{T}{T}defaultConfigurationIsVisible = 0;
{T}{T}{T}defaultConfigurationName = Release;
{T}{T}}};
{T}/* End XCConfigurationList section */
{T}}};
{T}rootObject = {uuids["project_obj"]} /* Project object */;
}}
"""

# Write the pbxproj
os.makedirs("SnakeGame.xcodeproj", exist_ok=True)
with open("SnakeGame.xcodeproj/project.pbxproj", "w") as f:
    f.write(pbxproj)

print("✅ Generated SnakeGame.xcodeproj/project.pbxproj")
print(f"   File size: {len(pbxproj)} bytes")
