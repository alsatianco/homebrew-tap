cask "binturong" do
  version "0.1.2"
  sha256 "271ee032171aa53ecee7360a32f504220a8634560d5ae6eccc99e83d9c6811e5"

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
