# Alsatian Homebrew tap

macOS applications from [Alsatian](https://github.com/alsatianco).

## Install

```bash
brew tap alsatianco/tap
```

Install Binturong:

```bash
brew install --cask alsatianco/tap/binturong
```

Update with `brew update && brew upgrade --cask binturong`.
The universal DMG supports both Apple Silicon and Intel. Homebrew verifies its
SHA-256 checksum. If macOS blocks the app, follow
[Binturong's installation instructions](https://github.com/alsatianco/binturong#macos-installation).
The tap never removes quarantine automatically.

## Maintenance

The **Update Binturong cask** workflow follows the latest stable Binturong release.
It checks every six hours or can be run manually from the Actions tab. Schedules
may be delayed or disabled after prolonged inactivity.

The updater validates the release tag, DMG asset name, and published SHA256SUMS
before generating `Casks/binturong.rb`. Prereleases are ignored. Before a public
stable release exists, the workflow leaves the tap unchanged.

For a local refresh (Python 3.10+):

```bash
python3 scripts/update_binturong.py
ruby -c Casks/binturong.rb
```

The workflow commits cask updates directly to `main`. Keep branch protection
compatible with that behavior, or adapt the workflow to propose pull requests.
Protect upstream release tags and designate only a newer stable version as the
latest release.

Additional apps can share this tap: add one cask per app under `Casks/`.
