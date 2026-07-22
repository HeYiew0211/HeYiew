import Cocoa
import WebKit

class AppDelegate: NSObject, NSApplicationDelegate {

    var window: NSWindow!
    var webView: WKWebView!

    func applicationDidFinishLaunching(_ notification: Notification) {
        // Create window
        let windowRect = NSRect(x: 0, y: 0, width: 540, height: 680)
        window = NSWindow(
            contentRect: windowRect,
            styleMask: [.titled, .closable, .miniaturizable],
            backing: .buffered,
            defer: false
        )
        window.title = "贪吃蛇"
        window.center()
        window.isReleasedWhenClosed = false

        // WKWebView configuration
        let config = WKWebViewConfiguration()
        let prefs = WKPreferences()
        prefs.tabFocusesLinks = false
        config.preferences = prefs

        // Create WKWebView
        webView = WKWebView(frame: window.contentView!.bounds, configuration: config)
        webView.autoresizingMask = [.width, .height]
        window.contentView?.addSubview(webView)

        // Load index.html from bundle
        if let htmlPath = Bundle.main.path(forResource: "index", ofType: "html") {
            let url = URL(fileURLWithPath: htmlPath)
            webView.loadFileURL(url, allowingReadAccessTo: url.deletingLastPathComponent())
        }

        window.makeKeyAndOrderFront(nil)
        NSApp.activate(ignoringOtherApps: true)
    }

    func applicationShouldTerminateAfterLastWindowClosed(_ sender: NSApplication) -> Bool {
        return true
    }
}
