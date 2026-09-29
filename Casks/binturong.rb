cask "binturong" do
  version "0.1.1"
  sha256 "20b378f90db2682baf99a864f0c46526dec61446eeb02ff404ad995380dc9ade"

  url "https://github.com/alsatianco/binturong/releases/download/v#{version}/Binturong_#{version}_universal.dmg"
  name "Binturong"
  desc "Desktop tools for code, data, text, and images"
  homepage "https://play.alsatian.co/software/binturong.html"

  app "Binturong.app"
  binary "#{appdir}/Binturong.app/Contents/MacOS/binturong-cli"

  caveats <<~EOS
    If macOS blocks this unnotarized app, see the macOS installation steps:
      https://github.com/alsatianco/binturong#macos-installation
    The release includes allow-binturong.sh for manual use after installation.
  EOS
end
