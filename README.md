# Minimalist Jekyll Job Board

A static Jekyll job board centered on a minimalist grey outline design and strict Google `JobPosting` JSON-LD schema.

## Setup

1. Update `url` in `_config.yml` to your GitHub Pages site URL.
2. Add jobs to the `_jobs/` folder using the example file.
3. Preview locally with:

```bash
bundle exec jekyll serve
```

## Deployment

1. In `_config.yml`, set `url:` to your GitHub Pages URL, for example `https://USERNAME.github.io`.
2. Commit and push the repository to GitHub.
3. In the repository Settings > Pages, select the branch `main` and the `/ (root)` folder.
4. If you use a custom domain, add it in the Pages settings and update `url:` in `_config.yml` accordingly.

This site uses only GitHub Pages-safe Jekyll configuration and no unsupported plugins.

## Validation

Validate the rendered job detail page using Google Rich Results Test or Structured Data Testing Tool.
