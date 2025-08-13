# GitHub Actions Configuration

This directory contains GitHub Actions workflows and configuration to optimize artifact storage and prevent quota issues.

## Artifact Storage Optimization

To address artifact storage quota limits, this repository implements the following strategies:

### 1. Automatic Cleanup (`cleanup-artifacts.yml`)
- Runs daily at 2 AM UTC
- Deletes artifacts older than 7 days
- Can be triggered manually via GitHub Actions UI
- Helps maintain storage within quota limits

### 2. Short Retention Periods
- All workflows use `retention-days: 1` for artifacts
- This significantly reduces storage usage
- Artifacts are still available for debugging recent runs

### 3. Minimal Artifact Creation
- Only essential artifacts are uploaded
- Test results and logs use minimal retention
- Non-essential debug data is not stored as artifacts

## Manual Cleanup

If immediate cleanup is needed:
1. Go to the Actions tab in GitHub
2. Find the "Cleanup Old Artifacts" workflow
3. Click "Run workflow" to trigger manual cleanup

## Storage Monitoring

GitHub provides storage usage information at:
- Repository Settings > Actions > General
- Organization/User Settings > Billing & plans

## Best Practices

- Use `retention-days: 1` for debug artifacts
- Use `retention-days: 7` only for important build outputs
- Avoid uploading large files as artifacts
- Consider using GitHub Releases for long-term file storage