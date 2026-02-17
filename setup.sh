#!/bin/bash
# PRD Generator Setup Script
# Initializes the knowledge folder structure and templates for a new project

set -e  # Exit on error

echo "🚀 Setting up PRD Generator for your project..."
echo ""

# Check if knowledge folder exists
if [ ! -d "knowledge" ]; then
    echo "✅ Creating knowledge/ folder structure..."
    mkdir -p knowledge/{company,product,regulatory,user-research,validation,custom}
else
    echo "ℹ️  knowledge/ folder already exists"
fi

# Check if manifest exists
if [ ! -f "knowledge/CONTEXT_MANIFEST.md" ]; then
    echo "✅ Creating Context Manifest from template..."
    cp templates/CONTEXT_MANIFEST.template.md knowledge/CONTEXT_MANIFEST.md
else
    echo "ℹ️  Context Manifest already exists"
fi

# Ask if user wants example files
echo ""
read -p "📝 Copy example context files to knowledge/? (y/n) " -n 1 -r
echo ""
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "✅ Copying example files..."
    cp templates/examples/mission-example.md knowledge/company/mission.md
    cp templates/examples/personas-example.md knowledge/user-research/personas.md
    cp templates/examples/prohibited-terms-example.md knowledge/regulatory/prohibited-terms.md
    echo "   📄 mission.md → knowledge/company/"
    echo "   📄 personas.md → knowledge/user-research/"
    echo "   📄 prohibited-terms.md → knowledge/regulatory/"
else
    echo "⏭️  Skipping example files"
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "📚 Next steps:"
echo "1. Edit knowledge/CONTEXT_MANIFEST.md to map your context files"
echo "2. Add your company/product context to knowledge/ folders"
echo "3. Invoke the PRD orchestrator: Use skill or direct invocation"
echo ""
echo "💡 Tips:"
echo "- Not all context is required - the system gracefully degrades"
echo "- Start with mission.md and personas.md for best results"
echo "- See templates/examples/ for guidance on each context type"
echo ""
