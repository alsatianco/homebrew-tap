#!/usr/bin/env python3
"""Refresh the cask from the latest stable Binturong GitHub release."""
import json
import os
from pathlib import Path
import re
from urllib.error import HTTPError
from urllib.request import Request, urlopen

REPO = 'alsatianco/binturong'
ROOT = Path(__file__).resolve().parents[1]


def fetch(url, authenticated=False):
    headers = {'User-Agent': 'alsatianco-homebrew-tap'}
    if authenticated and (token := os.environ.get('GH_TOKEN')):
        headers['Authorization'] = f'Bearer {token}'
    with urlopen(Request(url, headers=headers), timeout=60) as response:
        return response.read()


def render(release, checksums):
    tag = release['tag_name']
    if release['draft'] or release['prerelease'] or not re.fullmatch(r'v(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)', tag):
        raise ValueError('Expected a stable vX.Y.Z release')
    version = tag[1:]
    name = f'Binturong_{version}_universal.dmg'
    url = f'https://github.com/{REPO}/releases/download/{tag}/{name}'
    if not any(a['name'] == name and a['browser_download_url'] == url for a in release['assets']):
        raise ValueError(f'Missing expected release asset: {name}')
    matches = re.findall(r'^([a-f0-9]{64})  ' + re.escape(name) + r'$', checksums, re.MULTILINE)
    if len(matches) != 1:
        raise ValueError('Missing or duplicate DMG checksum')
    # v0.1.0 shipped before the app bundle included the CLI.
    cli_binary = ('\n  binary "#{appdir}/Binturong.app/Contents/MacOS/binturong-cli"'
                  if tuple(map(int, version.split('.'))) > (0, 1, 0) else '')
    return f'''cask "binturong" do
  version "{version}"
  sha256 "{matches[0]}"

  url "https://github.com/{REPO}/releases/download/v#{{version}}/Binturong_#{{version}}_universal.dmg"
  name "Binturong"
  desc "Desktop tools for code, data, text, and images"
  homepage "https://play.alsatian.co/software/binturong.html"

  app "Binturong.app"{cli_binary}

  caveats <<~EOS
    If macOS blocks this unnotarized app, see the macOS installation steps:
      https://github.com/{REPO}#macos-installation
    The release includes allow-binturong.sh for manual use after installation.
  EOS
end
'''


def main():
    try:
        release = json.loads(fetch(f'https://api.github.com/repos/{REPO}/releases/latest', True))
    except HTTPError as error:
        if error.code == 404:
            print('No public stable release yet; leaving the tap unchanged.')
            return
        raise
    # Validate the tag before interpolating it into a download URL.
    tag = release['tag_name']
    if not re.fullmatch(r'v(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)', tag):
        raise ValueError('Invalid stable release tag')
    checksum_url = f'https://github.com/{REPO}/releases/download/{tag}/SHA256SUMS'
    checksums = fetch(checksum_url).decode('utf-8')
    cask = render(release, checksums)
    (ROOT / 'Casks').mkdir(exist_ok=True)
    (ROOT / 'Casks/binturong.rb').write_text(cask)
    print(f'Updated Binturong to {tag}')


if __name__ == '__main__':
    main()
