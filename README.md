# Demo Repository

This repository contains a mathematical computation agent and demonstrates solutions for GitHub Actions artifact storage quota issues.

## Contents

- **mcp-math/**: A Python-based mathematical computation agent that responds in Spanish
- **.github/**: GitHub Actions workflows and configuration to prevent artifact storage quota issues

## The Artifact Storage Quota Issue

GitHub Actions has storage limits for artifacts:
- Free accounts: 500 MB storage limit
- Usage is recalculated every 6-12 hours
- When the quota is exceeded, new artifact uploads fail

## Solution Implemented

This repository demonstrates several strategies to prevent and resolve artifact storage quota issues:

### 1. Workflow Configuration
- **Conditional artifact uploads**: Only upload artifacts when necessary
- **Short retention periods**: Set to 1 day instead of default 90 days
- **Failure-only uploads**: Upload artifacts only when jobs fail for debugging
- **Environment variables**: Control artifact behavior via configuration

### 2. File Management
- **`.gitignore`**: Prevents unnecessary files from being tracked
- **Compression**: Maximum compression levels for any uploaded artifacts
- **Selective paths**: Only upload specific files that are actually needed

### 3. Monitoring and Management
- **Management script**: `.github/scripts/manage-artifacts.sh` for artifact cleanup
- **Documentation**: Clear guidance on troubleshooting storage issues
- **Configuration files**: Centralized settings in `.github/actions.env`

## Usage

### Running the Math Agent
```bash
cd mcp-math
pip install -r requirements.txt
python mcp_math_agent.py
```

### Managing Artifacts
```bash
.github/scripts/manage-artifacts.sh info    # Show storage information
.github/scripts/manage-artifacts.sh list    # List current artifacts
.github/scripts/manage-artifacts.sh cleanup # Clean up old artifacts
```

## Key Files

- **`.github/workflows/ci.yml`**: Lightweight CI workflow without excessive artifact uploads
- **`.github/workflows/copilot-swe.yml`**: Copilot SWE agent workflow with artifact management
- **`.github/actions.env`**: Configuration for artifact behavior
- **`.gitignore`**: Prevents temporary files from being tracked
- **`mcp-math/requirements.txt`**: Python dependencies

## Troubleshooting

If you encounter artifact storage quota issues:

1. **Wait**: Usage is recalculated every 6-12 hours
2. **Check billing**: Visit GitHub settings to see current storage usage
3. **Clean up**: Use the management script to remove old artifacts
4. **Optimize**: Review workflows to minimize artifact creation
5. **Upgrade**: Consider a paid GitHub plan for more storage if needed

This implementation ensures that GitHub Actions workflows can run successfully without hitting storage quotas while maintaining necessary functionality for development and debugging.