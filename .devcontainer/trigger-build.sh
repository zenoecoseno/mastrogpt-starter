TAG=$(grep 'image: sciabarracom/mastrogpt-starter' docker-compose.yml | awk -F: '{print $3}')
git commit -m "trigger build for $TAG" -a
git tag $TAG
echo Ready for $TAG - run 'git  push origin main --tags'
