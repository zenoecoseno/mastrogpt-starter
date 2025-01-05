TAG=$(jq -r .image <devcontainer.json | awk -F: '{print $2}')
git commit -m "trigger build for $TAG" -a
git tag $TAG
echo Ready for $TAG - run 'git  push origin main --tags'
