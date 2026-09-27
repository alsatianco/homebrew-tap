cask "binturong" do
  version "0.1.0"
  sha256 "6c9548a8bdca042e2071108a7462e457a68a46503381c2e377bd5506570b1bf5"

  url "https://github.com/alsatianco/binturong/releases/download/v#{version}/Binturong_#{version}_universal.dmg"
  name "Binturong"
  desc "Desktop tools for code, data, text, and images"
  homepage "https://play.alsatian.co/software/binturong.html"

  app "Binturong.app"

  caveats <<~EOS
    If macOS blocks this unnotarized app, see the macOS installation steps:
      https://github.com/alsatianco/binturong#macos-installation
    The release includes allow-binturong.sh for manual use after installation.
  EOS
end
