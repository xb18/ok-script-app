# Packaging and Release

## Release Files

- `.github/workflows/build.yml`: watches `v*` tags, tests, syncs updates, packages, and creates a GitHub Release.
- `pyappify.yml`: defines the app name, entry point, icon, Python version, and update repositories.
- `pyproject.toml`: defines the Qt and documentation dependency profiles; `web` is a desktop compatibility alias.
- `requirements.txt`: compiled installation lock; `requirements-web.txt` includes the same lock for compatibility.
- `deploy.txt`: lists files copied to a dedicated update repository.
- `.github/workflows/mirrorchyan_*.yml`: optional MirrorChyan upload and release-note workflows.

## Adapt the Build Workflow

Before the first release, update `.github/workflows/build.yml`:

- Replace the Git identity.
- Replace source and update repository URLs.
- Replace installer names and Release download links.
- Configure required GitHub Actions secrets.
- Remove unused CNB, file-hosting, or other template-specific content.

## MirrorChyan

### With MirrorChyan

Keep and update:

- `.github/workflows/mirrorchyan_uploading.yml`
- `.github/workflows/mirrorchyan_release_note.yml`

Replace `owner`, `repo`, `mirrorchyan_rid`, and installer filenames. Keep the dispatch step in `build.yml` and configure `MirrorChyanUploadToken`.

PyAppify adds the release version to installer names, for example
`ok-script-app-win32-China-setup-1.1.3.exe`. MirrorChyan matches
`ok-script-app-win32-China-setup-*.exe` within the selected release.

### Without MirrorChyan

Delete both MirrorChyan workflow files and remove the `Trigger MirrorChyanUploading` step from `build.yml`.

## Push a Version Tag

Commit and push the initialized project, then create a tag matching `v*`:

```bash
git add .
git commit -m "Initialize project"
git push origin HEAD
git tag v0.1.0
git push origin v0.1.0
```

GitHub Actions runs the tests, packages the EXE, and creates a matching GitHub Release. Search `.github/workflows` once more for stale template repositories, names, or missing secrets before release.

After changing dependencies, recompile the locks with the project virtual environment:

```powershell
python -m piptools compile --extra qt --strip-extras --no-header --output-file requirements.txt pyproject.toml
python -m piptools compile --extra docs --strip-extras --no-header --output-file requirements-docs.txt pyproject.toml
```

The Qt lock is installed with `--no-deps`. ok-script 3 uses `ok-pyside-minimal`;
no manual removal of PySide6 dependencies is needed. Keep
`requirements-web.txt` as an include of `requirements.txt`.
