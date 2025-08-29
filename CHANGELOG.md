# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased] - 2025-08-28

### Changed
- **BREAKING**: Updated Hugo version from v0.90.1 to v0.149.0
- Updated Netlify build configuration to use Hugo v0.149.0
- Updated GitHub Actions workflows to use Hugo v0.149.0
- Migrated from deprecated `paginate` config to new `pagination.pagerSize` format
- Updated minimum Hugo version requirement to v0.149.0
- Changed README to point to our BlueSky handle instead of Twitter/X

### Fixed
- Fixed template compatibility issues with Hugo v0.149.0:
  - Resolved `relURL` casting errors when `images` parameter is an array instead of string
  - Updated deprecated `site.DisqusShortname` references to `site.Params.disqusShortname`
  - Migrated deprecated `site.Social` and `site.Authors` to use `site.Params` equivalents
- Fixed Twitter meta tag generation to work with new parameter structure

### Technical Details

#### Configuration Files Updated
- `netlify.toml`: Updated `HUGO_VERSION` environment variable
- `config/_default/config.toml`: Updated pagination config and minimum Hugo version
- `.github/workflows/build.yml`: Updated Hugo version from v0.104.3 to v0.149.0
- `.github/workflows/pages.yml`: Updated Hugo version from v0.102.3 to v0.149.0

#### Template Files Updated
- `themes/logbook-hugo/layouts/_default/static.html`: Fixed image parameter handling
- `themes/logbook-hugo/layouts/_default/product.html`: Fixed image parameter handling  
- `themes/logbook-hugo/layouts/_default/single.html`: Fixed image parameter handling and Disqus config
- `themes/logbook-hugo/layouts/_default/video.html`: Fixed image parameter handling and Disqus config
- `themes/logbook-hugo/layouts/_default/single-notitle.html`: Fixed image parameter handling
- `themes/logbook-hugo/layouts/partials/datasets/og-twitter.html`: Updated social media parameter handling

#### Migration Notes
- The site now requires Hugo v0.149.0 or later
- All deprecated Hugo features have been updated to use current syntax
- Build time may vary due to Hugo performance improvements in newer versions
- No content changes were required - all fixes were at the template level