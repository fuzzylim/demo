#!/bin/bash
# Script to help manage GitHub Actions artifacts and prevent storage quota issues

echo "GitHub Actions Artifact Management"
echo "================================="

# Check if gh CLI is available
if ! command -v gh &> /dev/null; then
    echo "GitHub CLI (gh) is not installed. Please install it to manage artifacts."
    echo "Visit: https://cli.github.com/"
    exit 1
fi

# Function to list artifacts
list_artifacts() {
    echo "Listing current artifacts..."
    gh api repos/:owner/:repo/actions/artifacts --paginate
}

# Function to delete old artifacts (older than 1 day)
cleanup_old_artifacts() {
    echo "This would clean up artifacts older than 1 day..."
    echo "Note: This is a dry-run. Actual cleanup requires additional permissions."
    
    # Note: Actual artifact deletion requires workflow_write permissions
    # gh api repos/:owner/:repo/actions/artifacts/{artifact_id} -X DELETE
}

# Show current storage usage
show_storage_info() {
    echo "Storage Information:"
    echo "==================="
    echo "GitHub Actions storage quota information:"
    echo "- Free accounts: 500 MB storage"
    echo "- Usage is recalculated every 6-12 hours"
    echo "- Artifacts are automatically deleted after 90 days (or custom retention)"
    echo ""
    echo "To check current usage, visit:"
    echo "https://github.com/settings/billing"
}

# Main menu
case "$1" in
    "list")
        list_artifacts
        ;;
    "cleanup")
        cleanup_old_artifacts
        ;;
    "info")
        show_storage_info
        ;;
    *)
        echo "Usage: $0 {list|cleanup|info}"
        echo ""
        echo "Commands:"
        echo "  list    - List current artifacts"
        echo "  cleanup - Clean up old artifacts (dry-run)"
        echo "  info    - Show storage information"
        ;;
esac