# Alsatian Homebrew tap

Personal macOS casks for Alsatian software.

After the first stable Binturong release has been published and the update workflow has run:

```bash
brew install --cask alsatianco/tap/binturong
```

Upgrade with `brew update && brew upgrade --cask binturong`.
Both Apple Silicon and Intel use the universal DMG. Homebrew verifies its SHA-256.
If macOS blocks the app, follow [Binturong's macOS instructions](https://github.com/alsatianco/binturong#macos-installation).
The tap never removes quarantine automatically.

## Publish this repository

Create an empty public `alsatianco/homebrew-tap` repository on GitHub, then:

```bash
cd ~/git/homebrew-tap
git add .
git commit -m "Set up Binturong Homebrew tap"
git push -u origin main
```

The repository is public at https://github.com/alsatianco/homebrew-tap.
The local repository already has the `origin` remote configured.
Enable GitHub Actions. The workflow uses only this repository's `GITHUB_TOKEN`
with contents-write permission; no personal token or app-repository secret is needed.
Its bot commits directly to main; if main is protected, allow the bot or adapt the
workflow to open pull requests.

The workflow checks the latest stable release on the initial push, every six hours,
or via **Actions → Update Binturong cask → Run workflow**. GitHub schedules can be
 delayed or disabled after prolonged inactivity; manual dispatch remains available.
It ignores prereleases and validates the asset name and checksum before generating
`Casks/binturong.rb`. No placeholder cask is shipped before real release assets exist.
A 404 (no public release, or a private/unavailable source repository) leaves the cask
unchanged; Binturong must be public for users to download it.

To refresh locally (Python 3.10+):

```bash
python3 scripts/update_binturong.py
ruby -c Casks/binturong.rb
```

SHA256SUMS is trusted as release metadata from the upstream repository. Protect
upstream release tags and this repository's write access. Only designate a newer
stable release as GitHub's latest release; this tap follows that designation.
